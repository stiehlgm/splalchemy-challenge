# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify 



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(engine, reflect = True)

# Save references to each table
station = base.classes.station
measurement = base.classes.measurement 

# Create our session (link) from Python to the DB
session = session(engine)

#################################################
# Flask Setup
#################################################
app = flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")

def Homepage():
    " All available routes "
    return (
        f"Available Routes"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    rain_fall = sessiom.query(measurement.prcp, measurement.date)
    filter(measurement.date > '2016-08-23').order_by(measurement.date).all()

    prcp_dict = { 
        date: x for date, x in rain_fall 
    }

    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def station():
    stations = session.query(station.station).all()
    station_list = list(np.ravel(stations))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs = session.query(measurement.tobs)
        filter(measurement.station == 'USC00519281')
        filter(measurement.date >= '2017-8-23').all
    tobs_list = list(np.ravel(tobs))
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    start_temp = calculate_start
    

