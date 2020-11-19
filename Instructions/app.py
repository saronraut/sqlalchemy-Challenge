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

#Save reference(s)
measurement = Base.classes.measurement
station = Base.classes.station

#create a db session object
session = Session(engine)

##############################
# Flask Setup
##############################
app = Flask(__name__)

#Flask Routes 
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
#Saving the list into a dictionary format for JSON
    prcptn = {date: prcp for date, prcp in db_retrieve}
    return jsonify(prcptn)

@app.route("/api/v1.0/stations")
def stations():
    sttn_result = session.query(station.station).all()
#A 1-D array, containing the elements of the input, is returned
    sttn = list(np.ravel(sttn_result))
    return jsonify(stations = sttn)

@app.route("/api/v1.0/tobs")
def temperature():
#straight up copied the code from jupyter notebook for data retrieve
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

#Most Active Station was calculated in ipynb: climate_starter
    results = session.query(measurement.tobs).filter(measurement.station =="USC00519281").\
    filter(measurement.date >= year_ago).all()

#numpy ravel to return an array list
    tobs = list(np.ravel(results))
    return jsonify(Temps = tobs)

# Needed assistant on this apporach. The direction was very vague
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def average(start=None,end=None):
#select statemnt will be used to call from the DB to get the min,avg, and max
    select = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

# if End not provided, the result will be for >= start
    if not end: 
        results = session.query(*select).filter(measurement.date >= start).all()
        tobs = list(np.ravel(results))
        return jsonify(Temps = tobs)

# If both start and end are provided then is query will run
    results = session.query(*select).\
        filter(measurement.date >= start).filter(measurement.date <= end).all()
    tobs = list(np.ravel(results))
    return jsonify(Temps = tobs)

if __name__ == '__main__':
    app.run(debug=True)