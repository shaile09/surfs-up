import datetime as dt
import numpy as np
import pandas as pd
import app

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d'
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(y,m,d):
    prev_year=dt.date(y,m,d)
    prev_year=dt.date(y,m,d)-dt.timedelta(days=365)
    results=[]
    results=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=prev_year).all()
    df=pd.DataFrame(results, columns=[‘date’,‘precipitation’])
    df.set_index(df[‘date’], inplace=True)
    df=df.sort_index()
    return df.describe()