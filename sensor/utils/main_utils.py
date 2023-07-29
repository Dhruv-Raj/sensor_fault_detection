from sensor.exception import CustomException
from sensor.logger import logging
import sys, os
import dill
import yaml
import numpy as np

## Rading the yaml file from config--> schema.yaml

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e, sys)
    

def write_yaml_file(file_path: str, content: object, replace: bool= False) -> None:

    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok= True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            

    except Exception as e:
        raise CustomException(e, sys)
    

def save_numpy_array_data(file_path: str, array: np.array) -> np.array:
    '''
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    
    '''
    try:
        logging.info('Entered the save_numpy_array_data method of main_utils class')
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok= True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)

        logging.info('Excited the save_numpy_array_data method of main_utils class')
    except Exception as e:
        raise CustomException(e, sys)
    
def load_numpy_array_data(file_path: str, array: np.array) -> np.array:
    '''
    Load numpy array data to file
    file_path: str location of file to load
    array: np.array data loaded
    
    '''
    try:
        logging.info('Entered the load_numpy_array_data method of main_utils class')
        
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)

        logging.info('Excited the load_numpy_array_data method of main_utils class')
    except Exception as e:
        raise CustomException(e, sys)
    

    
def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info('Entered the save_object method of main_utils class')
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok= True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info('Excited the save_object method of main_utils class')
    except Exception as e:
        raise CustomException(e, sys)
