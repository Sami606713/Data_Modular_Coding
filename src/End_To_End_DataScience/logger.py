# import the logger and os and datetime
# set the log to the current time with month,date and year and hour min and sec.
# make the folder using os and inside the make folder add the log file.
import logging,os
from datetime import datetime

log_file=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"

log_path=os.path.join(os.getcwd(),'logs',log_file)
os.makedirs(log_path,exist_ok=True)

final_path=os.path.join(log_path,log_file)

# set the logging config use google
logging.basicConfig(level=logging.INFO,
                    format="[ %(asctime)s] %(lineno)s -%(levelname)s - %(message)s" ,
                    filename=final_path
                )