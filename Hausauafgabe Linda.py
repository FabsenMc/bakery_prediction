import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.multicomp import MultiComparison
from scipy.stats import t

## Zusammenführen der drei Datensätze in einem Dataframe
#Pfade zuteilen
pfad_1 = 'kiwo.csv'
pfad_2 = 'umsatzdaten_gekuerzt.csv'
pfad_3 = 'wetter.csv'

# Einlesen der CSVs
daten_1 = pd.read_csv(pfad_1, usecols=['Datum', 'KielerWoche'])
daten_2 = pd.read_csv(pfad_2, usecols=['Datum', 'Warengruppe', 'Umsatz'])
daten_3 = pd.read_csv(pfad_3, usecols=['Datum', 'Temperatur', 'Windgeschwindigkeit', 'Bewoelkung', 'Windgeschwindigkeit', 'Wettercode'])

#Zusammenführen der df
# Datensätze zusammenführen mit Outer Join
merged_df = pd.merge(daten_1, daten_2, how='outer', on='Datum')
merged_df = pd.merge(merged_df, daten_3, how='outer', on='Datum')

merged_df.shape
print(merged_df)
print(merged_df)


# Print the first 5 rows of the merged DataFrame
print(merged_df.head())



print(merged_df.info())

print(merged_df.describe())

print(merged_df['KielerWoche'].value_counts())
print(merged_df['Warengruppe'].value_counts())
print(merged_df['Windgeschwindigkeit'].value_counts())

print(merged_df['Umsatz'].kurtosis())
print(merged_df['Umsatz'].skew())

print(merged_df['Bewoelkung'].kurtosis())
print(merged_df['Bewoelkung'].skew())

print(merged_df['Temperatur'].kurtosis())
print(merged_df['Temperatur'].skew())

print(merged_df['Windgeschwindigkeit'].kurtosis())
print(merged_df['Windgeschwindigkeit'].skew())

merged_df['Warengruppe'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Verteilung der Warengruppen')
plt.ylabel('')
plt.show()

# Scatterplot mit Trendlinie
plt.figure(figsize=(8, 6))

# Scatterplot der Daten
plt.scatter(merged_df['Temperatur'], merged_df['Umsatz'], label='Daten')


# Umsatz im Verhältnis zur Temperatur
plt.title('Umsatz in Bezug zur Temperatur')
plt.xlabel('Temperatur')
plt.ylabel('Umsatz')
plt.legend()
plt.grid(True)
plt.show()
