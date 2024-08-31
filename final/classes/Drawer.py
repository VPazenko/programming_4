import pandas as pd
import matplotlib.pyplot as plt
import json
import datetime
import warnings

from classes.DrawingDataTransformations import DrawingDataTransformations
from classes.DataTransformer import DataTransformer
from classes.AddToLogFile import AddToLogFile


class Drawer:
    """
    Class for creating and saving an image
    """
    config_path = './config/application.json'


    def __init__(self, df):
        self.df = df
        self.df_set_index()
        self.img_folder, self.sensors_of_interest = self.open_config_data()

        # plt function not in the main loop, that triggers a user warning
        warnings.filterwarnings('ignore')

        for sensor in self.sensors_of_interest:
            if sensor in DataTransformer.features:
                self.plot_sensor(sensor)
            else:
                print(f"Check sensors in the 'application.json' file! Unable to display the {sensor}. " 
                      "Note that sensors 15, 50, 51 have been excluded from processing.")
            

    def df_set_index(self):
        '''
        Function sets time as an index for better display on the graph
        '''
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df = self.df.set_index('timestamp')


    def plot_sensor(self, sensor):
        '''
        Function for creating and saving an image
        '''
        # preprocessing data
        data = DrawingDataTransformations(self.df)
        
        plot = plt.figure(figsize=(20,5))
        plot = plt.plot(data.recovery[sensor], linestyle='none', marker='o', color='blue', markersize=7, label='recovering')
        plot = plt.plot(self.df[sensor], color='grey')
        plot = plt.plot(data.broken[sensor], linestyle='none', marker='X', color='black', markersize=15, label = 'broken')
        
        # Highlight all areas where clusters (more than 10 elements) of predicted breakdowns are found 
        # (high probability of breakdowns in this areas)
        i = 0
        for border in data.list_of_borders:
            # if label= start with '_' - not applicable
            # will only apply at i == 0
            name = "_" * i + f"intervals ({len(data.list_of_borders)} in total) with a high probability of breakdown(recovering)"
            plot = plt.axvspan(border[0], border[1], alpha=0.8, color='orange', label=name)
            i += 1

        plot = plt.plot(data.modeling[sensor], linestyle='none', marker='o', color='red', markersize=2, label='modeling problems')
        plot = plt.title(sensor)
        plot = plt.legend()

        now = datetime.datetime.now()
        # create a name with unique timestamp
        name = self.img_folder + '/' + sensor + '_' + now.strftime("%d-%m-%Y_%H-%M") + '.png'

        AddToLogFile.add_new_line(f'Saving image {name}')
        plt.savefig(name)  


    def open_config_data(self):
        '''
        Function return a dictionary from directory file

        Output: two directories from (config file)
        '''
        with open(self.config_path) as file:
            data = json.load(file)
        return data['img_directory'], data['sensors_of_interest']