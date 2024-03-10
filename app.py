from src.End_To_End_DataScience.logger import logging
from src.End_To_End_DataScience.exception import Custom_Exception
import sys

if __name__=='__main__':
   logging.info('Excution Start....')
   try:
      a='sami'/10
   except Exception as e:
      logging.info("Custom Exception in action")
      raise Custom_Exception(e,sys)