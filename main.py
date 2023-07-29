import os
import sys
from sensor.exception import CustomException
from sensor.logger import logging
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.components.data_ingestion import DataIngestion
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__=='__main__':
   try:
            train_pipeline= TrainPipeline()
            train_pipeline.run_pipeline()
   except Exception as e:
         raise CustomException(e, sys)