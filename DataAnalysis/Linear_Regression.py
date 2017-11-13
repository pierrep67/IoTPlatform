# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
def regLin(dataset,trainingSetLength,testSetLength):
    # Load CSV and columns
    df = pd.read_csv(dataset)
     
    Y = df['Y']
    X = df['X']
     
    X=X.reshape(len(X),1)
    Y=Y.reshape(len(Y),1)
     
    # Split the data into training/testing sets
    X_train = X[:trainingSetLength]
    X_test = X[testSetLength:]
     
    # Split the targets into training/testing sets
    Y_train = Y[:trainingSetLength]
    Y_test = Y[testSetLength:]
    
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    

    # Plot outputs
    plt.scatter(X_test, Y_test,  color='black')
    plt.title('Test Data')
    plt.xlabel('Time')
    plt.ylabel('Temperature')   
    plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
    plt.show()
    
    print(regr.coef_)

regLin("./Sample/dataset2.CSV",3600,5)


