from ..data.statistics import DataStatistics
from pyspark.sql import functions as F
from datetime import datetime
import pandas as pd
import pytz

class FeaturesScoresStatistics(DataStatistics):
    """ Compute average Features value based on model scores.
    
    Attributes
    ----------
    :TIMEZONE: Europe/Berlin Timezone
    :LOG_DATE: Log date as string
    :dataframe: Input spark or pandas dataframe. Joined features scores table
    :features_dict: Dictionary with used features
    :n_features: Number of selected features. Default: 10
    """
    TIMEZONE = pytz.timezone("Europe/Berlin")
    LOG_DATE = datetime.strftime(datetime.now(TIMEZONE).date(), "%Y-%m-%d")
    def __init__(self, dataframe, features_list:list=None, features_dict:dict=None, n_features:int=10):
        super().__init__(dataframe)
        self.features_dict = features_dict
        if features_list is None:
            self.features_list = list(self.features_dict.keys())
        else:
            self.features_list = features_list
        self.n_features = n_features
    
    def get_top_n_features(self):
        """ Return list of top n features."""
        return self.features_list[:self.n_features]
    
    def features_statistics(self, summary:list=[]):
        """ Return features statistics summary as Pyspark dataframe.
        
        Parameters
        ----------
        :summary: List with types of statistics summary. Options: 'mean', 'null', 'count', 'stddev', 'min' and 'max'

        Returns 
        -------
        :features_summary: Spark dataframe with statistical summary
        """
        features_summary = self.get_data_summary(self.features_list).withColumn("Datum", F.lit(self.LOG_DATE))
        if summary != []:
           return features_summary.where(F.col("summary").isin(summary))
        else:
            return features_summary
    
    def get_avg_feature_by_group(self, group_by:str, top_features_only:bool=False, join_type="inner"):
        """ Aggregate data on certain group (column) and 
        compute average feature value for this group.

        Parameters
        ----------
        :group_by: Column for data aggregation
        :top_features_only: Determination whether statistics for all or only top n features should be computed. Default: 'False'
        :join_type: Type of join. Default: 'inner'. Options: 'left', 'right', 'full', 'leftanti'

        Returns
        -------
        Spark dataframe
        """
        if top_features_only:
            list_of_features = self.get_top_n_features()
        else:
            list_of_features = self.features_list
        avg_feature_group = self._avg_feature_by_group(group_by=group_by, feature=list_of_features[0])
        for _, ft in enumerate(list_of_features[1:]):
            avg_feature_group = avg_feature_group.join(self._avg_feature_by_group(group_by, ft), on=group_by, how=join_type)
        return avg_feature_group.withColumn("Datum", F.lit(self.LOG_DATE))
    
    def _avg_feature_by_group(self, group_by:str, feature:str):
        """ Compute average feature value by group."""
        return self.dataframe.groupBy(group_by).agg(F.avg(feature).alias(f"avg_{feature}"))
