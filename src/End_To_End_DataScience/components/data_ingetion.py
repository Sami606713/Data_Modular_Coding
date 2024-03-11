# Read the data form database
# convert the read data into csv file called raw data inside the data folder
# convert the raw data into 2 parts i)train.csv ii)test.csv inside the data folder
import os,sys
import pandas as pd
from src.End_To_End_DataScience.logger import logging
from src.End_To_End_DataScience.exception import Custom_Exception
from src.End_To_End_DataScience.utils import read_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
# set the train and test data and raw data patgh

@dataclass
class DataIngestion_Config:
    raw_data_path:str=os.path.join("data",'raw_data.csv')
    test_data:str=os.path.join("data",'test_data.csv')
    train_data:str=os.path.join("data",'train_data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestion_Config()
    
    def initisate_data_ingestion(self):
        try:
            # read the data from database
            logging.info("Reading the data from data source")

            data=read_data()

            logging.info("saving the raw data into raw data")
            # make the folder where data should be save
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path))

            data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Spliting the raw data")
            test_data,train_data=train_test_split(data,test_size=0.2,random_state=43)

            logging.info("saving the test data")
            test_data.to_csv(self.ingestion_config.test_data,index=False,header=True)

            logging .info("saving the train data")
            train_data.to_csv(self.ingestion_config.train_data,index=False,header=True)

            return (
                self.ingestion_config.train_data,
                self.ingestion_config.test_data
            )

        except Exception as e:
            raise Custom_Exception(e,sys)