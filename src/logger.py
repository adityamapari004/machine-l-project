import logging
import os
from datetime import datetime
import logging

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(os.path.dirname(log_path),exist_ok=True)



LOG_FILE_PATH=os.path.join(os.getcwd(),"logs",LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO

)

if __name__=="__main__":
    logging.info("Logging has started.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.info("Logging has ended.")