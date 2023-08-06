from pyspark.sql import functions as F, SparkSession
import mlflow

spark = SparkSession.builder.master("local[4]").appName("DcgAnalytikLog").getOrCreate()

class MLflowMetaTable:
    """ Load logged meta table using mlflow.

    Attributes
    ----------
    :experiment_name: Path to current experiment for pulling tracked parameters
    :experiment_id: ID of current experiment
    :params_columns: mlflow tracked parameters
    """
    def __init__(self, experiment_name):
        self.experiment_name = experiment_name
        self.experiment_id  = self.mlflow_get_experiment_id()
        self.params_columns = self.get_log_params_columns()
        self.metrics_columns = self.get_log_metrics_columns()
        
    def mlflow_spark_meta_table(self, log_object:str="param"):
        """ Get meta table from mlflow tracking runs.
        
        Parameters
        ----------
        :log_object: Kind of logged data. Default: 'param'. Options: 'metric'.
        """
        meta_table = self._mlflow_spark_meta_table(log_object)
        for column in self.yield_from_iterable(meta_table.columns):
            meta_table = meta_table.withColumnRenamed(column, self.string_replacement(column, f"{log_object}.", ""))
        return meta_table
            
    def _mlflow_spark_meta_table(self, log_object:str="param"):
        """ Create mlflow meta table based on logged objects.
        
        Parameters
        ----------
        :log_object: Kind of logged data. Default: 'param'. Options: 'metric'.
        """
        assert log_object.lower() in ["param", "metric"], f"Given {log_object} is not allowed. Options: 'param' or 'metric'."
        if log_object == "param":
            return spark.createDataFrame(self.mlflow_get_runs_by_experiment()[self.params_columns])
        else:
            return spark.createDataFrame(self.mlflow_get_runs_by_experiment()[self.metrics_columns])
            
    def mlflow_get_experiment_id(self):
        return mlflow.get_experiment_by_name(self.experiment_name).experiment_id
    
    def mlflow_get_runs_by_experiment(self):
        return mlflow.search_runs(self.experiment_id)
    
    def get_log_params_columns(self):
        """ Returns list of mlflow tracked parameters and runs time."""
        return [column for column in self.mlflow_get_runs_by_experiment().columns if "start_time" in column or "params" in column]
    
    def get_log_metrics_columns(self):
        """ Returns list of mlflow tracked metrics and runs time."""
        return [column for column in self.mlflow_get_runs_by_experiment().columns if "start_time" in column or "metrics" in column]

    @staticmethod
    def string_replacement(string, to_replace, replacement):
        return string.replace(to_replace, replacement)
    
    @staticmethod
    def yield_from_iterable(iterable):
        yield from iterable

    @staticmethod
    def convert_datatype(dataframe, column_types:dict):
        """ Convert column types for input dataframe.

        Parameters
        ----------
        :dataframe: Input spark dataframe
        :column_types: Dictionary with columns and expected data types
        """
        for column, datatype in column_types.items():
            dataframe = dataframe.withColumn(column, F.col(column).cast(datatype))
        return dataframe
        