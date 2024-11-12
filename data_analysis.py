import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Daten laden
charging_data = pd.read_csv(r'Data\charging_sessions.csv')
weather_data = pd.read_csv(r'Data\weather_burbank_airport.csv')



# Konvertiere "connectionTime" und "disconnectTime" in Datetime-Format, falls noch nicht geschehen
charging_data['connectionTime'] = pd.to_datetime(charging_data['connectionTime'])
charging_data['disconnectTime'] = pd.to_datetime(charging_data['disconnectTime'])

# Ladezeit in Minuten berechnen
charging_data['charging_duration'] = (charging_data['disconnectTime'] - charging_data['connectionTime']).dt.total_seconds() / 60

# Histogramm der Ladezeiten
sns.histplot(data=charging_data, x='charging_duration', bins=30, kde=True)
plt.title("Distribution of Charging Session Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()


# Neue Spalten für Stunde und Wochentag
charging_data['hour'] = charging_data['connectionTime'].dt.hour
charging_data['weekday'] = charging_data['connectionTime'].dt.day_name()

# Durchschnittliche Anzahl der Ladungen pro Stunde
plt.figure(figsize=(12, 6))
sns.countplot(data=charging_data, x='hour')
plt.title("Charging Sessions by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Sessions")
plt.show()

# Durchschnittliche Anzahl der Ladungen pro Wochentag
plt.figure(figsize=(12, 6))
sns.countplot(data=charging_data, x='weekday', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title("Charging Sessions by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Sessions")
plt.show()



# Durchschnittlich gelieferte Energie (kWh) pro Stunde
hourly_kwh = charging_data.groupby('hour')['kWhDelivered'].mean()

plt.figure(figsize=(12, 6))
sns.lineplot(x=hourly_kwh.index, y=hourly_kwh.values)
plt.title("Average kWh Delivered per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average kWh Delivered")
plt.show()




# Daten zusammenführen (Merge) auf Basis von Datum und Stunde
charging_data['date'] = charging_data['connectionTime'].dt.date
charging_data['hour'] = charging_data['connectionTime'].dt.hour
weather_data['date'] = pd.to_datetime(weather_data['date']).dt.date
merged_data = pd.merge(charging_data, weather_data, on=['date', 'hour'], how='inner')

# Beispiel: Temperatur gegen Anzahl Ladesessions
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='temperature', y='kWhDelivered')
plt.title("Temperature vs. kWh Delivered")
plt.xlabel("Temperature (°C)")
plt.ylabel("kWh Delivered")
plt.show()
