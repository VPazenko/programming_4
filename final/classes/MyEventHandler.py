import os
import pandas as pd
from watchdog.events import FileSystemEventHandler
from classes.AddToLogFile import AddToLogFile


class MyEventHandler(FileSystemEventHandler):
    '''
    This class is a watchdog class, designed to track and respond to events
    '''
    def __init__(self, main_function):
        self.main = main_function


    def on_created(self, event):
        '''
        This method responds to the creation (moving to the folder) of a file.
        The file is loaded, the main function is executed and the file is deleted.
        '''
        AddToLogFile.add_new_line('Found new data file')
        df = pd.read_csv(event.src_path)
        self.main(df)
        os.remove(event.src_path)
        

    def on_deleted(self, event):
        '''
        This method responds to the deletion of a file.
        '''
        AddToLogFile.add_new_line('Resuming listening')
        print('Resuming listening')

