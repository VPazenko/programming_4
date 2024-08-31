# imports
import time
from classes.PubMed_references import PubMed_references
import yaml #enable to process configuration.yaml file.

# the next two lines are needed to create an environment in which the 
# ssl doesn't complain about non-existing public keys...
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def open_config_yaml(directory):
    '''
    Input: 1. directory - config.yaml file

    Function return a dictionary from directory file

    Output: dictionary from (config file)
    '''
    with open(directory, 'r') as config_info:
        config_dict = yaml.safe_load(config_info)
    return config_dict


def main():
    dict = open_config_yaml('config.yaml')
    new_refs = PubMed_references(dict['article_id'], dict['api_key'], dict['email'])

    start = time.time() 
    new_refs.save_first_n_refs_xml_with_mp(n = 10)
    time_with_mp = time.time() - start 
    
    start = time.time() 
    new_refs.save_first_n_refs_xml_without_mp(n = 10)
    time_without_mp = time.time() - start 
    
    print(f'Time with multiprocessing = {time_with_mp:.3f} s.')
    print(f'Time without multiprocessing = {time_without_mp:.3f} s.')


if __name__ == '__main__':
    main()
