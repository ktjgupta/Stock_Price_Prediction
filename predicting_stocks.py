# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:25:55 2019

@author: ktjgu
"""
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR 
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web


def predictLinear(ticker, start_date, days_in_future):
    start = start_date
    end = datetime.now()
    
    df = web.DataReader(ticker, "yahoo", start, end)
    
    dates = np.arange(df.shape[0])
    close_vals = df['Close'].values
    #plt.plot(dates, close_vals)
    
    Mat = np.zeros((len(dates), 2))
    Mat[:, 0] = np.ones(len(dates))
    Mat[:, 1] = dates
    
    model = LinearRegression().fit(Mat, close_vals)
    coeffs = model.coef_
    intercept = model.intercept_
    
    a = np.linspace(0, len(dates))
    b = model.intercept_ + coeffs[1]*a
    #plt.plot(dates, close_vals, color ='b')
    #plt.plot(a, b, color='r')
    predicted_val = intercept + coeffs[1]*(len(Mat)+days_in_future)
    
    return predicted_val


start_date = datetime(2016, 11, 2)

ticker = input("Enter ticker: ")
start_date  = input("Enter in date: ")
start_date = datetime.strptime(start_date, '%m-%d-%Y')
days_in_future = int(input("Enter how many days in the future you want to predict: "))
predicted_val = predictLinear(ticker, start_date, days_in_future)
'''
df2 = pd.DataFrame()
df2["date"] = dates;
df2["price"] = close_vals;

df2.to_csv("yeet.csv", index=False)
'''

'''
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
dates3 = np.reshape(dates,(len(dates), 1))
svr_dates = dates.reshape(-1,1)
svr_rbf.fit(svr_dates, close_vals)
'''

'''
plt.plot(svr_dates, svr_rbf.predict(svr_dates), c='g')
'''
print ("The predicted value for " + ticker + " in " 
       + str(days_in_future) + " days is $" + str(round(predicted_val, 2)))

#print (svr_rbf.predict([[len(Mat) + 5]]))




