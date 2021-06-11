import pandas as pd

model = pd.read_pickle('HousePricePredictor')
model

cols=['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']
income=eval(input('Enter the income :'))
house_age = eval(input('Enter the house age :'))
rooms = eval(input('Enter the rooms :'))
population = eval(input('Enter the polpulation :'))
query = pd.DataFrame({'Avg. Area Income':[income],'Avg. Area House Age':[house_age],
                      'Avg. Area Number of Rooms':[rooms],'Area Population':[population]})

query
model.predict(query)[0]
print('Price for the house can be: %.1f$'%(model.predict(query)[0]))
