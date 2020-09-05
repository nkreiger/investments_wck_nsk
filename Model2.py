import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import pymongo

# limit on the end date, loc the ffill stop location based on that parameter

# Step 1: Read in the Esimates Data Master
# Step 2: Create function to add each tab, aka sheet name, to a dataframe - I think it would need to be labeled and use grouby in pandas to accomplish
# if nan turn that into a temp variable to backfill, would not forward fill
# search for limit varaible, then set a forward fill from bottom value
# find the first data point using loc or something similar, set that as a max fill parameter or something
x = ['CQ12020']

# applying ffill() method to fill the missing values
# df.ffill(axis = 1)
client = pymongo.MongoClient(
    "mongodb+srv://Chaz:Chaz@eps-estimates.3emue.azure.mongodb.net/sample_airbnbtrue&w=majority")
db = client.test
mydb = client["eedb"]
estimates = mydb["estimates"]
print(mydb.list_collection_names())


class Connect(object):
    @staticmethod
    def get_connection():
        return pymongo.MongoClient("mongodb+srv://Chaz:Chaz@eps-estimates.3emue.azure.mongodb.net/eedb&w=majority")


connection = Connect.get_connection()


def function(x):
    df = pd.DataFrame()
    for i in x:
        df = pd.read_excel('Estimates Data Master_SPX.xlsx', sheet_name=x, index_col='Date', parse_dates=True)
    print(df)
    return df



df = function(x)
estimates.insert_one(df)
df.to_csv('test.csv')

