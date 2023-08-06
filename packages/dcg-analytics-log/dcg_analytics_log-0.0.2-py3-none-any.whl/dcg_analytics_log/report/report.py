from pyspark.sql import functions as F
from datetime import datetime
from .delta import DeltaStatistics
from .full_data import FullDataStatistics
from .features import FeaturesScoresStatistics
from .scores import ScoresStatistics, valid_scores_io
from .nbo import  NBORecommendations, NBOGroupSum


def convert_columns_to_datatype(dataframe, columns:list, data_type):
    """ Convert data type of dataframe columns
    
    Parameters
    ----------
    :dataframe: Pyspark dataframe
    :columns: Columns for converting data type
    :data_type: New data type
    """
    dataframe_cp = dataframe
    for _,column in enumerate(columns):
        dataframe_cp = dataframe_cp.withColumn(column, F.col(column).cast(data_type))
    return dataframe_cp

def number_of_customers(scores_table, features_table):
    """ Compare number of customers between scores and features table.
    Return number of customers if equal. Otherwise: 0.

    Parameters
    ----------
    :scores_table: Spark dataframe
    :features_table: Spark dataframe
    """
    if valid_scores_io(scores_table, features_table):
        return features_table.count()
    else:
        return 0


class UpdateDeltaReport(DeltaStatistics):
    """ Update delta report table.

    Attributes
    ----------
    :delta_table: Input delta table
    :report_table: Input current report table
    """
    def __init__(self, delta_table, report_table=None):
        super().__init__(delta_table)
        self.report_table = report_table
    
    def update_report(self, *columns, **kwargs):
        """ Create or update actual report table.

        Parameters
        ----------
        *columns: Input columns as strings
        **kwargs: Keyword arguments of update_log_dict() method from DeltaStatistics

        Returns
        -------
        Report table as spark dataframe
        """
        self.update_log_dict(*columns, **kwargs)
        current_report = self.dictionary_to_report_table()
        if self.report_table == None:
            return current_report
        else:
            return self.report_table.unionByName(current_report, True)


class UpdateDataReport(FullDataStatistics):
    """ Update delta report table.

    Attributes
    ----------
    :data_table: Input full data table
    :report_table: Input actual report table
    """
    def __init__(self, data_table, report_table=None):
        super().__init__(data_table)
        self.report_table = report_table
    
    def update_report(self, *columns, **kwargs):
        """ Create or update existing full data report table.

        Parameters
        ----------
        *columns: Input columns as strings
        **kwargs: Keyword arguments of update_log_dict() method from FullDataStatistics

        Returns
        -------
        Report table as spark dataframe        
        """
        self.update_log_dict(*columns, **kwargs)
        current_report = self.dictionary_to_report_table()
        if self.report_table == None:
            return current_report
        else:
            return self.report_table.unionByName(current_report, True)


class UpdateFeatureScoresReport(FeaturesScoresStatistics):
    """ Update features scores report table.

    Attributes
    ----------
    :features_scores_table: Joined spark features scores table
    :features_dict: Dictonary of features and features gain weights (or other statistical weights)
    :n_features: Number of top features
    :report_table: Actual report table
    """
    def __init__(self, report_table=None, **kwargs):
        super().__init__(**kwargs)
        self.report_table = report_table
        self.top_n_features = self.get_top_n_features()
        
    def update_report(self, all_features:bool=True, features_report=None, summary:list=[], group_by:str=None, top_features_only:bool=False):
        """ Create or update current features or features score report.

        Parameters
        ----------
        :all_features: Boolean input to calculate statistics for all features. Default: 'True'
        :features_report: Existing features statistics report table
        :summary: List with types of statistics summary. Options: 'mean', 'null', 'count', 'stddev', 'min' and 'max'
        :group_by: Column for aggregating features score table
        :top_features_only: Determination whether statistics for all or only top n features should be computed. Default: 'False'

        Returns
        -------
        Report table as spark dataframe
        """
        if all_features:
            current_report = self.features_statistics(summary)
            if features_report is not None:
                return features_report.unionByName(current_report, True)
            else:
                return current_report
        elif group_by is not None:
            current_report = self.get_avg_feature_by_group(group_by, top_features_only).sort(group_by)
            if self.report_table is not None:
                return self.report_table.unionByName(current_report, True)
            else:
                return current_report
        else:
            raise Exception("At leat a column for data aggregation should be specified!")
            

class UpdateScoresReport(ScoresStatistics):
    """ Update current scores report table.

    Attributes
    ----------
    :score_table: Actual machine learning scores table
    :report_table: Current report table 
    """
    def __init__(self, score_table, report_table=None):
        super().__init__(score_table)
        self.report_table = report_table
        
    def update_report(self, group_by, column, suffix=""):
        """
        Parameters
        ----------
        :group_by: Column for aggregating data
        :column: Score column for calculating average value
        :suffix: Column suffix 
        """
        current_report = self.get_scores_group_statistics(group_by, column, suffix).sort(group_by)
        if self.report_table == None:
            return current_report
        else:
            return self.report_table.unionByName(current_report, True)
