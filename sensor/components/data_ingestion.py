from sensor.exception import CustomException
from sensor.logger import logging
import os, sys
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sensor.data_access.sensor_data import SensorData

class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:

            self.data_ingestion_config= data_ingestion_config
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def export_data_into_feature_store(self) -> DataFrame:
        '''
        Export MongoDB collection record as DataFrame into feature store ---> as sensor.csv
        
        '''
        try:
            logging.info('Exporting Data from MongoDb')
            sensor_data= SensorData()
            dataframe= sensor_data.export_collection_as_dataframe(collection_name= self.data_ingestion_config.collection_name)
            feature_store_file_path= self.data_ingestion_config.feature_store_file_path

            # Creating folder --> feature store

            dir_path= os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok= True)

            ## Saving data as ---> sensor.csv
            dataframe.to_csv(feature_store_file_path, index= False, header= True)
            return dataframe
            logging.info('Exporting Done sensor.csv file created')
        except Exception as e:
            raise CustomException(e, sys)
        
    def split_data_as_train_test(self, dataframe= DataFrame) -> None:
        '''
        Feature store dataset will be split into train and test file ----> as train.csv & test.csv
        
        '''
        try:
            train_set, test_set= train_test_split(dataframe, test_size= self.data_ingestion_config.train_test_split_ratio)

            logging.info('Performaed train test split on dataframe')

            logging.info('Exited split_data_as_train_test method of data_ingestion class')


            dir_path= os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok= True)
            
            logging.info(f'Exporting train and test file path.')

            train_set.to_csv(self.data_ingestion_config.training_file_path, index= False, header= True)

            test_set.to_csv(self.data_ingestion_config.testing_file_path, index= False, header= True)

            logging.info('Exported train and test  file path completed.')

        except Exception as e:
            raise CustomException(e, sys)

    
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        try:
            dataframe= self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe= dataframe)
            data_ingestion_artifact= DataIngestionArtifact(train_file_path= self.data_ingestion_config.training_file_path, 
                                  test_file_path= self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)
