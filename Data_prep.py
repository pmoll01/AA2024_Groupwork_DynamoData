import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

##data visualisation
#sns.histplot(data=charging_data, x='connectionTime', bins=30, kde=True)
#plt.title("Distribution of Charging Session Durations")
#plt.xlabel("Duration (minutes)")
#plt.ylabel("Frequency")
#plt.show()