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

# Scatterplot 
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
# Klassifizierung der Temperaturdaten in 5-Schritten
bin_edges = range(-30, 41, 5)
labels = ['-30--25', '-25--20', '-20--15', '-15--10', '-10--5', '-5-0', '0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40']
merged_df['Temperaturklasse'] = pd.cut(merged_df['Temperatur'], bins=bin_edges, labels=labels[:-1])

# Feature Engineering: Hinzufügen der Jahreszeit
merged_df['Datum'] = pd.to_datetime(merged_df['Datum'])
merged_df['Jahreszeit'] = merged_df['Datum'].dt.month.apply(lambda x: 'Winter' if x in [12, 1, 2] else 'Frühling' if x in [3, 4, 5] else 'Sommer' if x in [6, 7, 8] else 'Herbst')

# Modellbildung
X = pd.get_dummies(merged_df[['Temperaturklasse', 'Jahreszeit']], drop_first=True)
X = sm.add_constant(X)
y = merged_df['Umsatz']
model = sm.OLS(y, X).fit()

# Modellbewertung
print(model.summary())

# Grafische Darstellung der Vorhersagen im Vergleich zu den tatsächlichen Umsätzen
plt.figure(figsize=(10, 6))
plt.scatter(model.fittedvalues, model.resid)
plt.xlabel('Vorhergesagte Werte')
plt.ylabel('Residuen')
plt.title('Residuenplot')
plt.axhline(y=0, color='r', linestyle='-')
plt.show()
