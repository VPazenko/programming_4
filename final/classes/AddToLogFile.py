import datetime


class AddToLogFile:
    '''
    This class add new information to the log-file
    '''
    def add_new_line(text):
        '''
        It's a @classmethod BB: Yes, so why don't annotate it as such 🤔?
        Method add a text line with current timestamp to the log-file
        '''
        now = datetime.datetime.now()
        # don't concatenate strings if you can help it.
        text_to_add = now.strftime("%Y-%m-%d %H:%M:%S") + ' ' + text
        with open('log_file.txt', 'a') as file:
            file.write(text_to_add + '\n')
