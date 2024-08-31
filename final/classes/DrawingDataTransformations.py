import pandas as pd


class DrawingDataTransformations:
    """
    Class for data preprocessing data before working with the plt
    """
    def __init__(self, df):
        self.broken, self.recovery, self.modeling = self.highlight_problem_spots(df)
        self.list_of_borders = self.working_on_df()


    def highlight_problem_spots(self, df):
        '''
        Method selects rows with certain labels
        '''
        broken_rows = df[df['machine_status']=='BROKEN']
        recovery_rows = df[df['machine_status']=='RECOVERING']
        modeling_problems = df[(df['new_status']=='BROKEN') | (df['new_status']=='RECOVERING')]
        
        return broken_rows, recovery_rows, modeling_problems


    def working_on_df(self):
        '''
        The method extracts all the predicted problems, clusters them, and highlights the cluster boundaries.

        Output: list of lists. [[left_border_of_claster, right_border], [left, right],...]
        '''
        df_new = self.modeling.copy(deep=True)
        # count timedifference
        df_new['time_td'] = df_new.index.to_series().diff().dt.seconds.div(60, fill_value=0)
        
        # Select all rows with a difference greater than 10 (Starting new cluster)
        df_new_areas = df_new[df_new['time_td'] > 10]
        
        list_of_borders = self.find_areas_borders(self.manual_clustering(df_new, df_new_areas))
        
        return list_of_borders


    def manual_clustering(self, total_df, df_areas):
        '''
        Input: 1. total_df = self.modeling (df with predicted problems)
               2. df_areas = df with all rows with a difference greater than 10 
                    (list of rows from which a new cluster starts)

        The method divides the dataframe into several depending on the list 
        
        Output: df_list = list of dataframes divided into clusters
        '''
        index_list = list(df_areas.index)
        df_list = []

        for elem in index_list:
            df_ = pd.DataFrame
            df_ = total_df.loc[:elem,:]
            df_ = df_.iloc[:-1]

            total_df = total_df.loc[elem:,:]
            df_list.append(df_)

        df_list.append(total_df)
        return df_list


    def find_areas_borders(self, df_list):
        '''
        Input: df_list = list of dataframes divided into clusters

        The method highlights the cluster boundaries (only if cluster contain more then 10 members)

        Output: list of lists. [[left_border_of_claster, right_border], [left, right],...]
        '''
        border_list = []
        for elem in df_list:
            if len(elem) > 10:
                left = list(elem.index)[0]
                right = list(elem.index)[-1]
                border_list.append([left, right])
        return border_list