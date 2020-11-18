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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect DB into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)


#Save a reference 
measurement = Base.classes.measurement
station = Base.classes.station

#create a db session object
session = Session(engine)

##############################
# Flask Setup
##############################
app = Flask(__name__)

#define  Flask Routes 

@app.route("/")
def home():
    return(
        f"Home Page <br/>"
        f"Available Routes: <br/>"
        f"____________________________ <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/temp/start-end <br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
# Calculate the date 1 year ago from the last data point in the database
#straight up copied the code from jupyter notebook for data retrieve
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
    db_retrieve = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago).all()

    db = {date: prcp for date, prcp in db_retrieve}
    return jsonify(db)


if __name__ == '__main__':
    app.run(debug=True)