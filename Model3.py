import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# limit on the end date, loc the ffill stop location based on that parameter

# Step 1: Read in the Esimates Data Master
# Step 2: Create function to add each tab, aka sheet name, to a dataframe - I think it would need to be labeled and use grouby in pandas to accomplish
# if nan turn that into a temp variable to backfill, would not forward fill
# search for limit varaible, then set a forward fill from bottom value
# find the first data point using loc or something similar, set that as a max fill parameter or something
x = ['CQ12020', 'CQ22020']

# applying ffill() method to fill the missing values
# df.ffill(axis = 1)
# df = pd.read_excel('Estimates Data Master_SPX.xlsx', sheet_name=None)
#pd.DataFrame(df)
# print(df)
# df = df.groupby()
# df.to_csv('test.csv')

# Each Excel sheet in a Python dictionary
workbook = pd.ExcelFile('Estimates Data Master_SPX.xlsx')
dictionary = {}
for sheet_name in workbook.sheet_names:
    df = workbook.parse(sheet_name)
    dictionary[sheet_name] = df
dictionary.to_csv('test.csv')
print(dictionary)