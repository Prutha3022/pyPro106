
import pandas as pd
import plotly.express as px
import csv
import numpy as np

df = pd.read_csv('Student Marks vs Days Present.csv')

fig= px.scatter(df,x= "Marks In Percentage", y="Days Present")

fig.show()


def getDataSource(dataPath):
    present=[]
    marks=[]
    
    with open(dataPath) as csvFile:
        csvReader=csv.DictReader(csvFile)
        for row in csvReader:
            present.append(float(row['Days Present']))
            marks.append(float(row['Marks In Percentage']))
            
    return {"x": marks,'y':present}

def findCorrelation(datasource):
    coRrelation= np.corrcoef(datasource['x'], datasource['y'])
    print("Correlation between the Days Present and Marks In Percentage:  ",coRrelation[0,1])
    
def main():
    dataPath= './Student Marks vs Days Present.csv'
    dataSource= getDataSource(dataPath)
    
    findCorrelation(dataSource)
    
main()
