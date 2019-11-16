# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:35:39 2019

@author: ktjgu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

dataset = pd.read_csv("amzn_history.csv")
#dataset['open'].plot(figsize=(8,4))

dataset['close: 30 Day Mean'] = dataset['close'].rolling(window=30).mean()
#dataset[['close','close: 30 Day Mean']].plot(figsize=(16,6))

dates = np.arange(dataset.shape[0])
training_set=dataset['open']
training_set=pd.DataFrame(training_set)
print (dataset)
dataset["new_date"] = dates;
plt.plot(dataset["new_date"], dataset["open"], color = 'red')

sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
y_train = []
for i in range(60, len(training_set_scaled)):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)


# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
print (X_train)
print (X_train.shape)

regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

# Adding a second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units = 1))


regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)


X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
predicted_stock_price = regressor.predict(X_train)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
predicted_stock_price=pd.DataFrame(predicted_stock_price)
print (predicted_stock_price)
print (predicted_stock_price[0])
plt.plot(np.arange(60, len(training_set_scaled)), predicted_stock_price[0], color = 'blue')
plt.show()

X_test = []
for i in range(len(X_train), len(X_train) + 2):
    X_test.append(training_set_scaled[i-60:i, 0])
    
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

print (X_train)
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
print("YEEEEt")
print (predicted_stock_price)