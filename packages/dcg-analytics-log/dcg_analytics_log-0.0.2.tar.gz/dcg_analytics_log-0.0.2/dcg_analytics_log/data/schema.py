from pyspark.sql.types import BooleanType, ByteType, DateType, DecimalType, DoubleType, FloatType, IntegerType, LongType, ShortType, StringType, TimestampType
from pyspark.sql import functions as F, SparkSession
from pyspark.sql.functions import udf

import pandas as pd
import pyspark

spark = SparkSession.builder.master("local[4]").appName("DcgAnalytikLog").getOrCreate()

class DataFrame:
    """ Class for verifying the type of dataframe.
    
    Attributes
    ----------
    :dataframe: Spark or pandas dataframe.
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe
        if dataframe is not None:
            assert isinstance(self.dataframe, pd.DataFrame) or isinstance(self.dataframe, pyspark.sql.dataframe.DataFrame), f"Dataframe has invalid type! ({type(self.dataframe)})"
            if isinstance(self.dataframe, pd.DataFrame):
                self.dataframe = spark.createDataFrame(self.dataframe)            
        else:
            self.dataframe = None
                
    def get_dataframe(self):
        """ Return dataframe."""
        return self.dataframe

# Die folgenden zwei Funktionen müssen außerhalt der Klasse definiert werden, 
# damit sie als Pyspark UDF angewendet werden können.
def concat_date_string(date_string:str, string_sep:str="-"):
    """ Remove seperator from date fomat.
    Eg.: '2022-01-01' --> '20220101'
    
    Parameters
    ----------
    :date_string: Input date string
    :string_sep: Seperator of date string. Default: '-'
    """
    # assert type(date_string) == str, f"{date_string} has {type(date_string)}!"
    assert string_sep in date_string, f"{string_sep} not in input string!"
    try:
        return "".join(date_string.split(string_sep))
    except TypeError:
        return None


def string_to_date_format(string:str, date_sep:str="-", year_first:bool=True):
    """ Transform string to date string format.
    Eg.: '20220101' --> '2022-01-01'
    
    Parameters
    ----------
    :string: Input date as string
    :date_sep: Seperator for converting date format as string. Default: '-'
    :year_first: Boolean. Default:True
    
    Returns
    -------
    Transformed date format
    """
    try:
        string_chars = list(string)
        if not year_first:
            string_chars.insert(2, date_sep)
            string_chars.insert(5, date_sep)
        else:
            string_chars.insert(4, date_sep)
            string_chars.insert(7, date_sep)
            return "".join(string_chars)
    except TypeError:
        return None


class DataSchema(DataFrame):
    """ Get schema of input dataframe.
    
    Attributes
    ----------
    :dataframe: Pandas or Spark dataframe
    :DECIMAL_TYPES: List of decimal data types 
    :STRING_TYPES: List of string data types
    :INT_TYPES: List of integer data types
    :BOOL_TYPES: List of boolean data types
    :DATETIME_TYPES: List of datetime and timestamp data types
    """
    
    DECIMAL_TYPES = [FloatType().simpleString(), DoubleType().simpleString(), DecimalType().simpleString()]
    STRING_TYPES = [StringType().simpleString()]
    INT_TYPES = [ShortType().simpleString(), LongType().simpleString(), IntegerType().simpleString()]
    BOOL_TYPES = [BooleanType().simpleString(), 1, 0]
    DATETIME_TYPES = [DateType().simpleString(), TimestampType().simpleString()]
    
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.columns = self.get_columns()
        
    def get_columns(self):
        """ Return all columns in dataframe as list."""
        return self.dataframe.columns
    
    def get_number_of_columns(self):
        return len(self.columns)
    
    def get_dataframe_schema(self):
        """ Create dictionary of column name and data type."""
        return {column.simpleString().split(":")[0] : column.simpleString().split(":")[1]
                for column in self.dataframe.schema.fields
        }
    
    def get_string_columns(self, ignores:list=[]):
        """ Create list of columns with type string.
        
        Parameters
        ----------
        :ignores: List of columns to be ignored. Default: []
        
        Returns
        -------
        List of columns names 
        """
        return [column for column, dtype in self.get_dataframe_schema().items() if dtype in self.STRING_TYPES and column not in ignores]
    
    def get_numeric_columns(self, ignores:list=[]):
        """Create list of columns with type string.
        
        Parameters
        ----------
        :ignores: List of columns to be ignored. Default: []
        
        Returns
        -------
        List of columns names 
        """
        return [column for column, dtype in self.get_dataframe_schema().items() if dtype in self.DECIMAL_TYPES or dtype in self.INT_TYPES and column not in ignores]
    
    def get_boolean_columns(self, ignores:list=[]):
        """Create list of columns with type string.
        
        Parameters
        ----------
        :ignores: List of columns to be ignored. Default: []
        
        Returns
        -------
        List of columns names 
        """
        return [column for column, dtype in self.get_dataframe_schema().items() if dtype in self.BOOL_TYPES and column not in ignores]
    
    def get_timestamp_columns(self, ignores:list=[]):
        """ Create list of columns with type string.
        
        Parameters
        ----------
        :ignores: List of columns to be ignored. Default: []
        
        Returns
        -------
        List of columns names 
        """
        return [column for column, dtype in self.get_dataframe_schema().items() if dtype in self.DATETIME_TYPES and column not in ignores]
    
    def date_column_to_string(self, column:str, sep:str="-", suffix=""):
        """
         Parameters
        ----------
        :column: Column for date format conversion
        :sep: Seperator for date format. Default: '-'
        :suffix: Suffix for new column. Origional column will be kept if '' is given. Default: ''
        
        Returns
        -------
        Dataframe with new date format.
        """
        udf_function = udf(lambda string: concat_date_string(string, sep) if not string is None else None, StringType())
        spark_column = udf_function(F.col(column))
        return spark_column.alias(f"{column}{suffix}")
    
    def column_date_string_format(self, column:str, suffix="", sep="-", year_first=True):
        """ Transform string to date format.
        
        Parameters
        ----------
        :column: Column for date format conversion
        :suffix: Suffix for new column. Origional column will be kept if '' is given. Default: ''
        :sep: Seperator for date format. Default: '-'
        :year_first: Bool. Default: True
        
        Returns
        -------
        Dataframe with new date format.
        """
        udf_function = udf(lambda string: string_to_date_format(string, sep, year_first) if not string is None else None, StringType())
        spark_column = udf_function(F.col(column))
        return spark_column.alias(f"{column}{suffix}")
        