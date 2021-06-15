import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marksinpercentage = []
    dayspresent = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            marksinpercentage.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))
    return {"x": marksinpercentage, "y": dayspresent}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between marks in persentage verses days present: \n--->", correlation[0,1])

def setup():
    data_path = "school.csv"
    datasource = getDataSource(data_path)
    findcorrelation(datasource)

setup()