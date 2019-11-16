# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 02:19:56 2019

@author: ktjgu
"""

import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data

import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

def nlp():
    df2 = pd.read_csv("Combined_News_DJIA.csv")
    print (df2)
    print (df2.sort_values(by="Date", ascending=False))

iextoken = data["token"]

start = datetime(2018, 10, 31)
end = datetime.now()

df = get_historical_data("TXN", start=start, end=end, output_format='pandas', token = iextoken)
print(df)

dates = np.arange(df.shape[0])
close_vals = df['close'].values
plt.plot(dates, close_vals)

Mat = np.zeros((len(dates), 2))
Mat[:, 0] = np.ones(len(dates))
Mat[:, 1] = dates

model = LinearRegression().fit(Mat, close_vals)
coeffs = model.coef_
intercept = model.intercept_

a = np.linspace(0, len(dates))
b = model.intercept_ + coeffs[1]*a
plt.plot(dates, close_vals, color ='b')
plt.plot(a, b, color='r')