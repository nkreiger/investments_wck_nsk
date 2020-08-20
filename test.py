import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('pg.csv', parse_dates=['ACTDATS','FPEDATS'])
df = pd.DataFrame(df)
print(df)

pd.to_datetime(df['ACTDATS'], format='%Y/%m/%d')
pd.to_datetime(df['FPEDATS'], format='%Y/%m/%d')
pd.to_numeric(df['VALUE'], downcast='float')


df = df.pivot_table(values=['VALUE'],
                    index=['FPEDATS', 'ACTDATS'],
                    columns=['ESTIMATOR', 'ANALYS'],
                    dropna=True)
print(df)
df.replace('NaN', np.nan, inplace=True)
df = df.groupby(level='FPEDATS').fillna(method='ffill')
df = df['VALUE'].fillna(method='backfill')
df['Mean'] = df.mean(axis=1)
df['Max'] = df.max(axis=1)
df['Min'] = df.min(axis=1)
df['Count'] = df.count(axis=1)
df['Stdev'] = df.std(axis=1)

df3 = df['Mean']
df3 = pd.DataFrame(df3)


df3 = pd.DataFrame(df3).reset_index()
df3 = pd.pivot_table(data=df3, values='Mean', index='ACTDATS', columns='FPEDATS')

df3 = df3.apply(lambda series: series.loc[:series.last_valid_index()].ffill())

pd.to_datetime(df3.index, infer_datetime_format=True)


df3 = df3.resample('W').last()
df3 = df3.apply(lambda series: series.loc[:series.last_valid_index()].ffill())
print(df3)


weight_1H = 0.25
weight_1Y = 0.75
weight_2Y = 0.25

RoC_1H = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=31).multiply(weight_1H))
RoC_1Y = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=52).multiply(weight_1Y))
RoC_2Y = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=42).multiply(weight_2Y))

Score = (RoC_1H).add(RoC_1Y).add(RoC_2Y)
Score['Mean'] = Score.mean(axis=1)
print(Score)
Score.plot(legend=False)
plt.show()
Score = pd.DataFrame(data=Score, columns=['ACTDATS','Mean'])
Score.plot()
plt.show()
print(Score)

RoC_1H = Score['Mean'].apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=31).multiply(weight_1H))
RoC_1Y = Score['Mean'].apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=52).multiply(weight_1Y))
RoC_2Y = Score['Mean'].apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=42).multiply(weight_2Y))
D2 = (RoC_1H).add(RoC_1Y).add(RoC_2Y)
Score['2D'] = D2.mean(axis=1)
Score.plot(legend=True)
plt.show()