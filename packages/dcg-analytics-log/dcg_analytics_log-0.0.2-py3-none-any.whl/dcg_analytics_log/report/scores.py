from ..data.statistics import DataStatistics
from pyspark.sql import functions as F
from datetime import datetime
import pandas as pd
import pyspark
import pytz


def valid_scores_io(scores_table, features_table):
    """ Return True if number of entries in scores data equals 
    the number of reference features dataframe.
    """
    assert isinstance(scores_table, pd.DataFrame) or isinstance(scores_table, pyspark.sql.dataframe.DataFrame), f"Scores table has invalid type! ({type(scores_table)})"
    assert isinstance(features_table, pd.DataFrame) or isinstance(features_table, pyspark.sql.dataframe.DataFrame), f"Scores table has invalid type! ({type(features_table)})"
    if scores_table.count != features_table.count():
        return False
    else:
        return True
    
class ScoresStatistics:
    TIMEZONE = pytz.timezone("Europe/Berlin")
    LOG_DATE = datetime.strftime(datetime.now(TIMEZONE).date(), "%Y-%m-%d")
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    def get_scores_group_statistics(self, group_by:str=None, column:str=None, suffix=""):
        """ Aggregate scores data by given group and compute statistics for specified column.
        
        Parameters
        ----------
        :group_by: Column for aggregating scores data
        :column: Data column for computing descriptive statistics
        :suffix: Input suffix for aggregated columns as string

        Returns
        -------
        Spark dataframe of aggregated data
        """
        assert column != None, "At least a column must be specified!"
        if group_by is None:
            groupby = self.dataframe.groupBy()
        else:
            groupby = self.dataframe.groupBy(group_by)
        return groupby.agg(F.count(column).alias("Count" + suffix),
                           F.avg(column).alias("Avg" + suffix)
                          ).withColumn("Datum", F.lit(self.LOG_DATE))
                          