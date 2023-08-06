from pyspark.sql import functions as F
from ..data.schema import DataSchema
import numpy as np


class DataStatistics(DataSchema):
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.columns = self.get_columns()
    # TODO: Eventually add a function for numerical data distributionn

    def get_columns_distribution(self, columns:list):
        """ Return categorical distribution for specified columns.
        
        Paramters
        ---------
        :columns: List of columns with categorical data (String)
        
        Returns
        -------
        :data_distributions: Dictionary of columns data distribution
        """
        data_distributions = {}
        for column in columns:
            data_distributions.update(self.get_category_distribution(column))
        return data_distributions

    def get_category_distribution(self, column:str):
        """ Return categories distrbution as dictionary.
        
        Parameters
        ----------
        :column: Dataframe column
        
        Returns
        -------
        Dictionary of data distribution
        """
        assert column in self.columns, f"{column} is not a known column. Expected: {self.columns}"
        assert column in self.get_string_columns(), f"{column} does not contain 'String' as data type."
        return {column: {
                          row[0]:row[1] for i, row in enumerate(
                                                                self.dataframe.groupBy(column).count().collect()
                                                              )
                       }
             }
    
    def get_category_values(self, column:str):
        """ Return a dictionary with column name as key and a 
        list of distinct column entries as list.
        
        Parameters
        ----------
        :column: Column name as string
        
        Returns
        -------
        Dictionary with column and entries. 
        Eg.:
        {'column': ['entry1', 'entry2']}
        """
        assert column in self.columns, f"{column} is not a known column. Expected: {self.columns}"
        assert column in self.get_string_columns(), f"{column} does not contain 'String' as data type."
        return {column: [
                         row[0] for row in self.dataframe.select(column).distinct().collect()
                       ]
             }
    
    def get_column_statistics(self, column:str, statistic:str="mean"):
        """ Return statistic value for given column.
        
        Parameters
        ----------
        :column: Column name from statistics dictionary
        :statistic: Statistic value to return
        
        Returns
        -------
        Statistic value as integer
        """
        return self.get_summary_dictionary()[column][statistic]
     
    def get_summary_dictionary(self):
        return self.summary_as_dictionary()
    
    def summary_as_dictionary(self):
        """ Return a dictionary of data statistics.
        
        Returns
        -------
        Dictionary with data summary information. Eg.:
        {'column': {'stat1': value,
                    'stat2': value2,
                    'stat3': value3
                },
         'column2': {'stat1': value,
                     'stat2': value2,
                     'stat3': value3
                 }
        }
        """
        statistics_dict = {}
        sub_dict = {}
        summary_array = np.array(
                                 [
                                     list(row) for row in self.get_data_summary().collect()
                                ]
                           )
        for i,column in enumerate(self.columns):
            summaries = list(summary_array[:,0])
            statistics = list(summary_array[:, i+1])
            for j,_ in enumerate(summaries):
                try:
                    if "." not in statistics[j]:
                        statistics[j] = int(statistics[j])
                    else:
                        statistics[j] = float(statistics[j])
                except (AttributeError, TypeError, ValueError):
                    statistics[j]
                sub_dict[summaries[j]] = statistics[j]
            statistics_dict[column] = sub_dict
            sub_dict = {}
        return statistics_dict
    
    def propotion_nulls(self):
        """ Calculate the propotion of null values for each column 
        using data statistics.
        
        Returns
        -------
        :nulls_propotion: Dictionary with column as key and null percentage as value
        """
        nulls_propotion = {}
        for column, statistics in self.summary_as_dictionary().items():
            try:
                nulls_propotion.update(
                                       {f"Nulls-Anteil {column}" : round(statistics["null"] / (statistics["count"] + statistics["null"]), 2)}
                                    )
            except TypeError:
                nulls_propotion.update(
                                       {f"Nulls-Anteil {column}" : 0.0}
                                    )
        return nulls_propotion
    
    def get_column_counted_nulls(self, column):
        """ Retrieve number of nulls for given column as integer."""
        return int(self.count_nulls().select(column).collect()[0][0])

    def count_nulls(self):
        """ Count number of null-values in column."""
        nulls_dataframe = self.dataframe.agg(*[F.count(F.when(F.isnull(column), column)).alias(column) for column in self.columns])\
                             .withColumn("summary", F.lit("null"))
        return nulls_dataframe.select("summary", *self.columns)
      
    def count_distinct_values(self, column:str):
        """ Count total number of distinct entries in given column.
        
        Parameters
        ----------
        :column: Column for counting distinct values
        
        Returns
        -------
        Number of distinct items
        """
        return self.dataframe.agg(F.countDistinct(column)).collect()[0][0]
    
    def get_data_summary(self, columns:list=None):
        """ Compute descriptive statistics for columns using describe().
        Complement results with number of null-values.
        
        Parameters
        ----------
        :columns: List of selected columns

        Returns
        -------
        Statistics summary as spark dataframe
        """
        if columns is not None:
            return self.dataframe.select(columns).describe().unionByName(self.count_nulls(), True)
        return self.dataframe.describe().unionByName(self.count_nulls(), True)


class StatisticsDeviation:
    """
    Determine values deviation between current and reference data statistics.
    
    Attributes
    ----------
    :current_stat: Statistic value of current data
    :ref_stat: Statistic value of reference data
    """
    
    def __init__(self, current_stat:int, ref_stat:int):
        self.current_stat = current_stat
        self.ref_stat = ref_stat
    
    def verify_low_devition_rate(self, max_ratio:float=0.05):
        """ Verification, that deviation rate is below maximum ratio.
        
        Parameters
        ----------
        :max_ratio: Maximum deviation ratio
        """
        if self.compute_difference() <= max_ratio:
            return True 
        else:
            False
        
    def devition_rate(self):
        """ Compute deviation ratio between current and reference statistic."""
        return  abs(1- (float(self.current_stat) / float(self.ref_stat)))
