import pandas as pd

#data_path = ".\Data\"

charging_data = pd.read_csv(r'Data\charging_sessions.csv')
weather_data = pd.read_csv(r'Data\weather_burbank_airport.csv')

#check column names, typers and null values
print(charging_data.info())
print(weather_data.info())

# Check fist rows
print(charging_data.head())
print(weather_data.head())


##Missing Data
#Identify missing data
charging_missing_data = charging_data.isnull().sum()
print(charging_missing_data[charging_missing_data > 0])

weather_missing_data = weather_data.isnull().sum()
print(weather_missing_data[weather_missing_data > 0])

#Handle missing vlues

##Errorous Data
#Outliers
#Inconsistancies

##Final Review
