import logging
import os,sys
from datetime import datetime

LOG_DIR = "logs"
#main working dir ke andar loga create karange.
LOG_DIR = os.path.join(os.getcwd(),LOG_DIR) #join current working dir (Delivery Time Prediction) and logs dir

os.makedirs(LOG_DIR,exist_ok=True)

#.log log_2023
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#output: log_2024_04_25_11_58

log_file_path = os.path.join(LOG_DIR,file_name)

#final step Logs create
logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
