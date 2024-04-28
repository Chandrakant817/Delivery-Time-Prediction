from flask import Flask
from src.logger import logging
from src.exception import CustomeException
import os,sys

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    try:
        raise Exception("We are testing our Exception file") # Error
    
    except Exception as e:
        ML = CustomeException(e,sys)
        logging.info(ML.error_message)
        
        logging.info("We are testing out Logging file")

        return "Welcome to Machine Learning Project"

if __name__ == "__main__":
    app.run(debug=True) #deafult post number:5000