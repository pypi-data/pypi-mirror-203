from ..data.statistics import DataStatistics
from pyspark.sql import SparkSession
from datetime import datetime
import pandas as pd
import pytz

spark = SparkSession.builder.master("local[4]").appName("DcgAnalytikLog").getOrCreate()

class DeltaStatistics(DataStatistics):
    TIMEZONE = pytz.timezone("Europe/Berlin")
    LOG_DATE = datetime.strftime(datetime.now(TIMEZONE).date(), "%Y-%m-%d")
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.log_dict = {"Datum": self.LOG_DATE}
    
    def dictionary_to_report_table(self):
        """ Convert report dictionary to pyspark dataframe."""
        data_log_df = pd.DataFrame.from_dict(self.log_dict, "index").transpose()
        return spark.createDataFrame(data_log_df)
        
    def update_log_dict(self, *columns):
        """ Update logging dictionary with delta values.
        
        Parameters
        ----------
        *columns: Input columns as strings
        """
        for column in columns:
            for count_dict in self.count_distinct_delta_column(column):
                self.log_dict.update(count_dict)
            for nulls_dict in self.count_nulls_delta_column(column):
                self.log_dict.update(nulls_dict)
    
    def count_nulls_delta_column(self, column):
        yield {f"Nulls_{column}": self.get_column_counted_nulls(column)}
    
    def count_distinct_delta_column(self, column:str):
        """ Returns number of distinct column entry as dictionary.
        
        Parameters
        ----------
        :column: Input column
        """
        yield {f"Anz_{column}": self.count_distinct_values(column)}
