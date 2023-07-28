import pymongo
import sys
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.exception import CustomException
import certifi
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url=  os.getenv(MONGODB_URL_KEY)  # "mongodb://localhost:27017/"  -- mongo_db_url
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) ## MongoDB Compas 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)  ## MongoDB Atlas
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise CustomException(e, sys)
        