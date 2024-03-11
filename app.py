from src.End_To_End_DataScience.logger import logging
from src.End_To_End_DataScience.exception import Custom_Exception
from src.End_To_End_DataScience.components.data_ingetion import DataIngestion
from src.End_To_End_DataScience.components.data_ingetion import DataIngestion_Config

import sys

if __name__=='__main__':
   logging.info('Excution Start....')
   try:
      logging.info('data ingestion....')
      data_ingestion=DataIngestion()
      data_ingestion.initisate_data_ingestion()
   except Exception as e:
      logging.info("Custom Exception in action")
      raise Custom_Exception(e,sys)