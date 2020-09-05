import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

est_CQ32020 = pd.read_excel('Estimates Data Master_SPX.xlsx',sheet_name='CQ32020',index_col='Date',parse_dates=True)

y = est_CQ32020['NYSE:MMM']
plt.plot(y)
plt.xlabel('Date',fontsize=10)
plt.ylabel('Estimate',fontsize=10)
print(plt.show())
print(est_CQ32020.describe())
print(est_CQ32020['NYSE:MMM'])

test_df = est_CQ32020[:, 0:1]
test_df = pd.DataFrame(test_df)
test_df.replace('NaN', np.nan, inplace=True)
test_df = test_df.groupby(level='Date').fillna(method='ffill')
print(test_df)

df3 = test_df

weight_1M = 0.04
weight_2M = 0.06
weight_3M = 0.08
weight_1Q = 0.12
weight_1H = 0.13
weight_9M = 0.15
weight_1Y = 0.32
weight_2Y = 0.10

RoC_1M = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=4).multiply(weight_1M))
RoC_2M = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=8).multiply(weight_2M))
RoC_3M = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=12).multiply(weight_3M))
RoC_1Q = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=16).multiply(weight_1Q))
RoC_1H = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=31).multiply(weight_1H))
RoC_9M = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=40).multiply(weight_9M))
RoC_1Y = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=52).multiply(weight_1Y))
RoC_2Y = df3.apply(lambda series: series.loc[:series.last_valid_index()].pct_change(periods=104).multiply(weight_2Y))

Score = RoC_1M.add(RoC_2M).add(RoC_3M).add(RoC_1Q).add(RoC_1H).add(RoC_9M).add(RoC_1Y)
Score['Mean'] = Score.mean(axis=1)
print(Score)
Score.plot(legend=False)
print(plt.show())


