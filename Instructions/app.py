##############################
#import SqlAlchemy#
##############################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base()
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

##############################
#import modules
##############################
import pandas as pd
import numpy as np
import datetime as dt

##############################
# import FLASK
##############################
from flask import Flask, jsonify





#create an app
app = Flask(__name__)

#define Routes 

@app.route("/")
def home():
    return("Home Page")




if __name__ == '__main__':
    app.run(debug=True)