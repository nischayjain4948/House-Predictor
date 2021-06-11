import numpy as np
import warnings
import pandas as pd
warnings.filterwarnings('ignore') 
import matplotlib.pyplot as plt
df = pd.read_csv('housing.csv')
from sklearn.model_selection import train_test_split
x=df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']]
y=df['Price']
xtrain , xtest ,ytrain , ytest = train_test_split(x,y,test_size=0.25,random_state=10)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain,ytrain)
model.coef_
print('%.1f%%'%(model.score(xtest,ytest)*100))
ypred = model.predict(xtest)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(ytest,ypred))
100*mean_absolute_error(ytest,ypred)/ypred[0]
final_model=model
pd.to_pickle(final_model,'HousePricePredictor')



