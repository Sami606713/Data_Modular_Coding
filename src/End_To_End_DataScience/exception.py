# import logging that we make in logging and sys for traking the error detail
import sys
from src.End_To_End_DataScience.logger import logging

# Fun for get the error detail
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"""error occur in python script name [{file_name}] line nbr [{exc_tb.tb_lineno}] error message [{str(error)}]"""
    return error_message
# Make a Custom Exception
class Custom_Exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message