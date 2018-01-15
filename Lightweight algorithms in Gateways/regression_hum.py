import pandas as pd
from sklearn import linear_model

data = pd.read_csv('Data_HumOutput.csv')


# define the data/predictors as the pre-set feature names  
df = pd.DataFrame(data=data, columns=data.columns)
print(df)

# Put the target in another DataFrame
target = pd.DataFrame(data=data, columns=["Hum"])

x =df[["Horaires","Ordi","nbEleves","HumExt"]]
y =target["Hum"]


lm = linear_model.LinearRegression()
model = lm.fit(x,y)

predictions = lm.predict(x)

print(lm.coef_)
print(predictions)
print (lm.intercept_)

