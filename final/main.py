import json
import time
from watchdog.observers import Observer

from classes.Model import Model
from classes.Drawer import Drawer
from classes.AddToLogFile import AddToLogFile
from classes.MyEventHandler import MyEventHandler


def open_config_data(config_path = './config/application.json'):
    '''
    Input: 1. config_path - directory of config.json file

    Function return a dictionary from directory file

    Output: dictionary from (config file)
    '''
    with open(config_path) as file:
        data = json.load(file)
    return data


def main(df):
    AddToLogFile.add_new_line('Loaded the file')

    model = Model()
    df['new_status'] = model.prediction(df)
    AddToLogFile.add_new_line('Received predictions')

    df_data_list = [str(df.iloc[0,1]), str(df.iloc[-1,1])]
    data = open_config_data()
    # don't concatenate strings if you can help it. Use formatted strings.
    name = data['output_directory'] + '/' + df_data_list[0].split()[0] + '_to_' + df_data_list[1].split()[0] + '.csv'
    
    # Save data with predictions in starting format
    df.iloc[:,1:].to_csv(name)
    AddToLogFile.add_new_line('Saving predictions')

    # You make a new drawer every time; I *think* this will be a problem eventually for
    # the garbage collector (same with the Model at the beginning of this method).
    draw = Drawer(df)


if __name__ == "__main__":
    data = open_config_data()
    path = data['input_directory']
    event_handler = MyEventHandler(main)
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(data["watchdog_interval_sec"])
    finally:
        observer.stop()
        observer.join()