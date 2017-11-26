# -*- coding: utf-8 -*-

# line plot of time series
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
import numpy

# Shows data on a chart
def showDatas(dataset):
    # load dataset
    series = Series.from_csv(dataset, header=0)
    # display first few rows
    print(series.head(20))
    # line plot of dataset
    series.plot()
    pyplot.show()

# Splits data to get a learn dataset and a test dataset
def splitData(dataset2):
        
    series = Series.from_csv(dataset2, header=0)
    split_point = len(series) - 7
    dataset, validation = series[0:split_point], series[split_point:]
    print('Dataset %d, Validation %d' % (len(dataset), len(validation)))
    dataset.to_csv('./Sample/dataset.csv')
    validation.to_csv('./Sample/validation.csv')


# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = float(dataset[i]) - float(dataset[i - interval])
		diff.append(value)
	return numpy.array(diff)


# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]


 

# Forecast the temperature of next day
def execute(dataset):
    # load dataset
    splitData(dataset)
    series = Series.from_csv('./Sample/dataset.csv', header=None)
    series_validation = Series.from_csv('./Sample/validation.csv', header=None)
    # Set X with the value in the CSV
    X = series.values
    Y = series_validation.values
    # Set the value of the cycle
    days_in_year = 365 
    # Create a list with temperature difference
    differenced = difference(X, days_in_year)
    # fit model
    model = ARIMA(differenced, order=(7,0,1))
    model_fit = model.fit(disp=0)
    # one-step out-of sample forecast
    forecast = model_fit.forecast()[0]
    # invert the differenced forecast to something usable
    forecast = inverse_difference(X, forecast, days_in_year)
    print('Forecast: %f' % forecast)
    print('Real: %f' % Y[0])

execute('./Sample/daily-minimum-temperatures.csv')