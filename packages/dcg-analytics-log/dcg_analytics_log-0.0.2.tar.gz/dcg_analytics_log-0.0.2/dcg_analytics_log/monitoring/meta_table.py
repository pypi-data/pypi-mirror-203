from pyspark.sql import functions as F, SparkSession
from datetime import datetime, timedelta
from ..data.reader import DataReader
import pandas as pd
import json
import os

spark = SparkSession.builder.master("local[4]").appName("DcgAnalytikLog").getOrCreate()

class MetaTable(DataReader):
    """ Build intern monitoring meta table for machine learning model.

    Attributes
    ----------
    :result_table: Scored machine learning table
    :path_meta: Path to existing meta table as string
    :table_format: File format for exporting meta table
    """
    def __init__(self, result_table, path_meta:str, table_format:str=None, **kwargs):
        self.result_table = result_table
        self.table_format = table_format
        if os.path.exists(path_meta):
            if "/dbfs" in path_meta:
                path_meta = path_meta.replace("/dbfs", "")
                super().__init__(path_meta)
            self.meta_table = self.read_data(self.table_format, **kwargs)
        else:
            self.meta_table = None       
    
    def update_meta_table(self, **kwargs):
        """ Create or update an existing meta table
        
        Parameters
        ----------
        Refer: create_meta_dictionary()

        Returns
        -------
        :meta_table: Spark dataframe
        """
        current_table = spark.createDataFrame(pd.DataFrame.from_dict(self.create_meta_dictionary(**kwargs)))
        if self.meta_table is not None:
            meta_table = self.meta_table.unionByName(current_table, True)
        else:
            meta_table = current_table
        return meta_table
    
    def create_meta_dictionary(self, column:str, run_id:int, date_diff:int, model_name:str, statistics_dict:dict=None):
        """ Create Python dictionary with standard model run information. 
        There is also a possibility for expanding the dictionary.

        Paramerters
        -----------
        :column: Input data column as string
        :run_id: ID of latest run as integer
        :date_diff: Dates until next run as integer
        :model_name: Input name of scoring model
        :statistics_dict: Optional. Addtional statistics dictionary for table expansion
        """
        if self.meta_table is not None:
            current_run_id = self.get_current_run_id(self.meta_table, run_id)
        else:
            current_run_id = 0
        # Standard meta information
        meta_dictionary = {"Run_ID": self.next_run_id(current_run_id),
                           "Customer": self.extract_spark_cluster_value(key="customer"),
                           "Model": model_name,
                           "Environment": self.extract_spark_cluster_value(key="environment", pos=1),
                           "Run_Date": self.get_current_run_date(),
                           "Next_Run":  self.get_next_run_date(date_diff),
                           f"Distinct_{column}": self.count_distinct_value(column),
                           "N_Rows": self.count_all()
                        }
        if statistics_dict is not None: 
            meta_dictionary.update(statistics_dict)
        return meta_dictionary
            
    def count_distinct_value(self, column:str):
        return self.result_table.select(column).distinct().count()
    
    def count_all(self):
        return self.result_table.count()
    
    @staticmethod
    def get_current_run_date():
        return datetime.now().date().strftime("%Y-%m-%d")
    
    @staticmethod
    def get_next_run_date(date_diff:int):
        """ Determine next run date based on current date and date difference. 
        
        Parameter
        ---------
        :date_diff: Number of days until next run as integer.
        """
        return (datetime.now().date() + timedelta(date_diff)).strftime("%Y-%m-%d") 
    
    @staticmethod
    def get_current_run_id(dataframe, id_column):
        """ Current run Id is the max value of id column.
        
        Parameters
        ---------
        :dataframe: Input spark dataframe
        :id_column: Column name of run ID
        """
        return dataframe.groupBy().agg(F.max(id_column)).collect()[0][0]    
    
    @staticmethod
    def next_run_id(current_id):
        """ Add 1 to current current_id.
        
        Paramter
        --------
        :current_step: Current run ID
        """
        return current_id + 1
    
    @staticmethod
    def extract_spark_cluster_value(key="customer", split_by="-", pos=0):
        """ Extract given key from cluster tags ('spark.databricks.clusterUsageTags.clusterAllTags').
        
        Parameters
        ----------
        :key: Tag key for extracting value from tag. Default: 'Vendor'. 
        Options: ['Creator', 'ClusterName', 'ClusterId', 'customer', 'environment']
        :split_by: Special character for splitting string value. Default: '-'
        :pos: Position of splitted value. Default: 0
        """
        for tag in json.loads(spark.conf.get("spark.databricks.clusterUsageTags.clusterAllTags")):
            if tag["key"] == key:
                yield tag["value"].split(split_by)[pos]
