from pyspark.sql import functions as F
from ..data.schema import DataFrame
from datetime import datetime
import pytz

class NBOGroupSum(DataFrame):
    """ Group feed dataframe and compute the sum for given column.
        
    Attributes
    ----------
    :TIMEZONE: Europe/Berlin Timezone
    :LOG_DATE: Log date as string
    :group_by: Column for aggregating data
    :column: -
    :alias: Output column name. Default: 'Sum'
    """
    TIMEZONE = pytz.timezone("Europe/Berlin")
    LOG_DATE = datetime.strftime(datetime.now(TIMEZONE).date(), "%Y-%m-%d")
    def __init__(self, dataframe, group_by, column, alias="Sum"):
        super().__init__(dataframe)
        self.group_by = group_by
        self.column = column
        self.alias = alias
        
    def get_data_sum(self):
        return self.sum_data_by_group(self.dataframe, self.group_by, self.column, self.alias)
    
    @staticmethod
    def sum_data_by_group(dataframe, group_by, column, alias):
        return dataframe.groupBy(group_by).agg(F.sum(column).alias(alias))
    
class NBORecommendations(DataFrame):
    """
    Attributes
    ----------
    :TIMEZONE: Europe/Berlin Timezone
    :LOG_DATE: Log date as string
    :dataframe: Dataframe with recommended items
    """
    TIMEZONE = pytz.timezone("Europe/Berlin")
    LOG_DATE = datetime.strftime(datetime.now(TIMEZONE).date(), "%Y-%m-%d")
    def __init__(self, dataframe):
        super().__init__(dataframe)
        
    def get_number_of_recommendations_per_item(self, column_labels:list, alias:str=None):
        """ Return spark dataframe with number of recommendations for each item.
        
        Parameters
        ----------
        :column_labels: Names of recommendation columns
        :alias: Name of new column

        Returns
        -------
        Spark dataframe
        """
        joined_recommendation = self.join_counted_recommendations(*column_labels)
        # Die erste Spalte der Join-Tabelle sollte die Join-Spalte sein. Deshalb [1:]
        recommendation_columns = joined_recommendation.columns[1:]
        if alias is None:
            alias = "Sum"
        return joined_recommendation.withColumn(alias, sum([F.col(column) for column in recommendation_columns]))\
                                    .withColumn("Datum", F.lit(self.LOG_DATE))
    
    def join_counted_recommendations(self, *column_labels):
        """
        Parameters
        ----------
        :column_labels: Names of recommendation columns
        
        Returns
        -------
        :joined_recommendation: Spark dataframe with joined recommendation items and number of counts
        """
        agg_recommendations = self.get_agg_recommendations_dictionary(*column_labels)
        list_of_recommendation_groups = self.get_list_of_keys(agg_recommendations)
        joined_recommendation = agg_recommendations[list_of_recommendation_groups[0]]
        for _,key in enumerate(list_of_recommendation_groups[1:]):
            joined_recommendation = joined_recommendation.join(agg_recommendations[key], on="Recommendation", how="full").fillna(0)
        return joined_recommendation
        
    def get_agg_recommendations_dictionary(self, *column_labels):
        """ Return dictionary with aggregated recommendation spark dataframe.
        
        Parameters
        ----------
        :column_labels: Names of recommendation columns as string
        
        Returns 
        -------
        :recommendations_dict: Dictionary of nth recommendation and spark dataframe
        Eg.: {'Reco1': DataFrame, 
              'Reco2': DataFrame},
              ...,
              'Reco_n': DataFrame
             }  
        """
        recommendations_dict = {}
        for i, column in enumerate(column_labels):
            recommendations_dict[f"Recommendation_{i+1}"] = self.dataframe.select(F.col(column).alias("Recommendation"))\
                                                                          .groupBy("Recommendation").agg(F.count("Recommendation").alias(f"N_Recommendation_{i+1}"))
        return recommendations_dict
    
    def column_to_rows(self, *columns, alias="Article"):
        """ Transpose dataframe columns to rows.
        
        Parameters
        ----------
        :alias: Alias of column name
        
        Returns
        -------
        :dataframe_transposed: Spark dataframe with transposed columns
        """
        dataframe_transposed = self.dataframe.select(F.col(columns[0]).alias(alias))
        for _,column in enumerate(columns[1:]):
            dataframe_transposed = dataframe_transposed.union(self.dataframe.select(F.col(column).alias(alias)))
        return dataframe_transposed
    
    def get_top_n_product_groups(self, dataframe, dataframe2, group_by, on, columns:list=[], how="inner", top=50):
        """ Get top n recommended items."""
        return self.dataframe_joiner(dataframe, dataframe2, group_by, on, columns, how=how).limit(top)
    
    @staticmethod
    def dataframe_joiner(dataframe, dataframe2, group_by, on, columns:list=[], how="inner"):
        """ Method to join two dataframes and aggregate joined table by group.
        
        Parameters
        ----------
        :dataframe: First input dataframe
        :dataframe2: To join input dataframe
        :group_by: Column for aggregating data 
        :on: Column for joining data
        :columns: List of columns for selecting data
        :how: Default 'inner'. Options: 'lef', 'right', 'full', 'leftanti'

        Returns
        -------
        Spark dataframe
        """
        if columns == []:
            columns = ["*"] # Select all if input columns list is empty
        return dataframe.join(dataframe2.select(columns).distinct(), on=on, how=how).groupBy(group_by).count().sort("count", ascending=False)
    
    @staticmethod
    def get_list_of_keys(dictionary:dict):
        return list(dictionary.keys())
        