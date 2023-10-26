""" Import required libraries"""

import pandas as pd
from datetime import datetime
from datetime import date
import csv
import os
import glob
import sqlalchemy as sa
from sqlalchemy import create_engine

#Connection to Database
print("Connecting Database")
connection_string = (
    'Driver=ODBC Driver 17 for SQL Server;'
    'Server=newagedbrpt.newage.local;'
    'Database=NewAge_Demand_Planning_DB;'
    'UID=Nikhil.Gupta;'
    'PWD=Demandplanning@2023;'
    'Trusted_Connection=no;'
)
connection_url = sa.engine.URL.create(
    "mssql+pyodbc", 
    query=dict(odbc_connect=connection_string)
)
engine = sa.create_engine(connection_url, fast_executemany=True)
print("Connection to DataBase Successfull!!")



