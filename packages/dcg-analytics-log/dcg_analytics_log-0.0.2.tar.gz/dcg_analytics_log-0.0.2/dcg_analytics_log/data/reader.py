from pyspark.sql import SparkSession
from datetime import datetime
import shutil
import pytz
import os

spark = SparkSession.builder.master("local[4]").appName("DcgAnalytikLog").getOrCreate()

class PathReader:
    """   
    Attributes
    -----------
    :TIMEZONE: Default timezone for Germany
    :CURRENT_DATE: Current date for storing data 
    :path: Path for reading files or showing folders on Databricks
    """
        
    def __init__(self, path:str=None):
        self.path = path
        if self.path is None:
            self.list_path_contents = []
        else:
            if os.path.exists(self.path):
                self.list_path_contents = [file for file in os.listdir(self.path)]
            else:
                self.list_path_contents = []
        
    def extract_files_from_path(self, sub_paths:list=None):
        """ Create list of files from path.
        
        Parameters
        ----------
        :sub_path: List of sub paths, folders or files
        """
        if sub_paths is None:
            return self.list_path_contents
        else:
            return [file for sub_path in sub_paths for file in os.listdir(self.path + sub_path)]
        
    def unpack_zip_files(self, paths_list:list=None, target_path:str=None, sub_path:str=None):
        """ Method for unpacking zip files to given target path.
        
        Paramters
        ----------
        :paths_list: List of files paths
        :target_path: Target path for unpacking zip files 
        :sub_path: Optional. 
        """
        TIMEZONE = pytz.timezone("Europe/Berlin")
        CURRENT_DATE = datetime.strftime(datetime.now(TIMEZONE).date(), "%Y%m%y")

        if sub_path is not None:
            target_path = f"{target_path}/{sub_path}/{CURRENT_DATE}"
        else:
            target_path = f"{target_path}/{CURRENT_DATE}"
        for _, path in enumerate(paths_list):
            for path in self._correct_string_from_path(path):
                shutil.unpack_archive(path, target_path, "zip")
    
    @staticmethod
    def empty_files_paths(files_paths:list):
        """ Return True if input list of paths to files is empty.
        
        Parameters
        ----------
        :delta_paths: List of paths to data
        """
        if files_paths == []:
            return True
        return False 
    
    @staticmethod
    def _correct_string_from_path(path, string:str=None, correction:str=None):
        """
        Parameters
        -----------
        :string: String to be replaced
        :correction: String replacement        
        """
        yield path.replace(string, correction)

    
class DataReader(PathReader):
    def __init__(self, path:str=None):
        super().__init__(path)
       
    def get_paths_contents(self):
        return self.list_path_contents
    
    def get_path(self):
        return self.path
    
    def read_data(self, table_format:str="csv", sub_path:str=None, **kwargs):
        """ Read data with given table format. 
        
        Parameters
        ----------
        :table_format: Input table format as string. Default: 'csv'. Options: 'parquet', 'hive' and 'avro'
        :sub_path: Input sub path to file as string
        **kwargs: Keyword arguments of csv_reader() to read csv file
        """
        table_format = table_format.lower()
        assert table_format in ["csv", "parquet", "hive", "avro"], f"Error while readling path. Invalid data format. Expected: ['csv', 'parquet', 'hive', 'avro']. Got: {table_format}"
        if self.path is not None:
            if sub_path is not None:
                path = self.path + sub_path
            else:
                path = self.path
            if "/dbfs" in self.path:
                path = path.replace("/dbfs", "")
            if table_format == "csv":
                return self.csv_reader(path, **kwargs)
            if table_format == "parquet":
                return self.parquet_reader(path)
            if table_format == "hive":
                return self.hive_reader(path)
            if table_format == "avro":
                return self.avro_reader(path)
        else:
            raise TypeError("None type can not be read!")
                
    @staticmethod
    def csv_reader(path, header=True, infer_schema=True, delimiter=",", encoding="UTF-8"):
        """ Read csv data.

        Parameters
        ----------
        :header: Boolean indication, whether table header should be displayed. Default: True
        :infer_schema: Boolean value for infering data schema. Default: True
        :delimiter: Columns delimiter as string. Default: ','
        :encoding: Data encoding. Default: "UTF-8"
        """
        return spark.read.format("csv")\
                         .option("header", header)\
                         .option("inferSchema", infer_schema)\
                         .option("delimiter", delimiter)\
                         .option("encoding", encoding)\
                         .load(path)
            
    @staticmethod
    def parquet_reader(path):
        """ Read parquet data."""
        return spark.read.format("parquet").load(path)
        
    @staticmethod
    def hive_reader(path):
        """ Read hive table using SQL."""
        return spark.sql(f"SELECT * FROM {path}")
        
    @staticmethod
    def avro_reader(path):
        """ Read avro table."""
        return spark.read.format("avro").load(path)
        