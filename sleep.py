import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x": coffee, "y": sleep}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between amount of coffee you drink verses how much sleep you get: \n--->", correlation[0,1])

def setup():
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    findcorrelation(datasource)

setup()