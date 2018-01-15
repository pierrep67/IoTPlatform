import pandas as pd
from sklearn import linear_model

data = pd.read_csv('Data_TempOutput.csv')


# define the data/predictors as the pre-set feature names  
df = pd.DataFrame(data=data, columns=data.columns)
# Put the target in another DataFrame
target = pd.DataFrame(data=data, columns=["Temp"])

x =df[["Horaires","Ordi","nbEleves","TempExt"]]
y =target["Temp"]


lm = linear_model.LinearRegression()
model = lm.fit(x,y)

predictions = lm.predict(x)

print df
print(predictions)
print lm.coef_
print lm.intercept_

