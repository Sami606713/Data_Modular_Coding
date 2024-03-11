import os,sys
import pandas as pd
from src.End_To_End_DataScience.logger import logging
from src.End_To_End_DataScience.exception import Custom_Exception
import pymysql
from dotenv import load_dotenv

# load the environment variable
load_dotenv()

# get the environment variable
host=os.getenv("host")
user_name=os.getenv("user_name")
password=os.getenv("password")
database=os.getenv("database")

# read the data from data base
def read_data():
    # make the connnection pointer
    logging.info("setting the connection")
    try:
        conn=pymysql.connect(
            host=host,
            user=user_name,
            password=password,
            database=database
        )
        logging.info("connection successfully",conn)
        logging.info("reading the data")
        df=pd.read_sql_query("""
                select * from exams
                """,con=conn)
        print(df.head())
        return df
        
    except Exception as e:
        raise Custom_Exception(e,sys)