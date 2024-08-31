import pandas as pd
import json
import pickle

from sklearn.neighbors import KNeighborsClassifier  
from classes.DataTransformer import DataTransformer
from classes.AddToLogFile import AddToLogFile


class Model:
    """
    These class create/download and store the model 

    config_path == path to "application.json" file
    """
    model_path = './training_data/model.pkl'
    config_path = './config/application.json'


    def __init__(self):
        self.model_path = './training_data/model.pkl'
        
        # Try to open an existing model, if not, creates a new one and saves the model.
        try:
            self.model = self.load_model()
        except:
            self.training_data = self.open_training_data()
            self.model = self.train_model()
            self.save_model()


    def open_training_data(self):
        '''
        Function return a training df (should be contained in the folder)

        Output: df
        '''
        with open(self.config_path) as file:
            data = json.load(file)
        df = pd.read_csv(data['training_file'])
        return df


    def train_model(self):
        '''
        Function create a model

        Output: model
        '''
        KNN_model = KNeighborsClassifier(n_neighbors=50)
        data_trans = DataTransformer(self.training_data)
        KNN_model.fit(data_trans.X, data_trans.y)
        return KNN_model


    def save_model(self):
        '''
        Method saving the model in pickle format
        '''
        with open(Model.model_path,'wb') as file:
            pickle.dump(self.model, file)


    def load_model(self):
        '''
        Method loading the model in pickle format

        Output: model
        '''       
        with open(Model.model_path, 'rb') as file:
            model = pickle.load(file)
        return model


    def prediction(self, df):
        '''
        Input: df = raw df

        Method give a prediction data based on model and raw df

        Output: new_status = array with predicted labels
        '''
        # transform data
        data_trans = DataTransformer(df)
        AddToLogFile.add_new_line('Received transformed data')
        # use model method predict
        new_status = self.model.predict(data_trans.X)
        return new_status