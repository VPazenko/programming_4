from sklearn.preprocessing import StandardScaler
import pandas as pd


class DataTransformer:
    """
    These class store and transform pandas df to appropriate data set for further using in the model.
    
    As features we use only 49 sensors. Reasons:
    In modeling file missing values for sensors 15 and 51 more than 10%
    sensor_50 is not represented in the test data (for July and August)
    
    self.X - matrix with 49 features (columns)
    self.y - array with labels 
    """
    features = ['sensor_' + str(x).zfill(2) for x in list(range(15)) + list(range(16, 50))]
    label = 'machine_status'
    

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.X, self.y = self.transform()


    def transform(self):
        '''
        Function transform data and return matrix with 49 features and array with labels
        '''
        self.data_frame['timestamp'] = pd.to_datetime(self.data_frame['timestamp'])
        self.data_frame = self.data_frame.set_index('timestamp')

        X = self.data_frame[self.features]
        # Conversion to numpy is needed to speed up further model calculations
        X = X.fillna(X.mean()).to_numpy()

        X = StandardScaler().fit_transform(X)
        y = self.data_frame[self.label].values
        return X, y