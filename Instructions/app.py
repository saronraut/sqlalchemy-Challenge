##############################
#import SqlAlchemy#
##############################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
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

##############################
#Create an engine for sqlite DB
##############################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)

#Reflect DB into ORM classes
Base = automap_base()
Base.prepare(engine,Reflect=True)
Base.classes.keys()

#Save a reference 
measurement = Base.classes.measurement
station = Base.classes.station

#create a db session object
session = Session(engine)



##############################
# Flask Setup
##############################
app = Flask(__name__)

#define Routes 

@app.route("/")
def home():
    return("Home Page <br/>")






if __name__ == '__main__':
    app.run(debug=True)