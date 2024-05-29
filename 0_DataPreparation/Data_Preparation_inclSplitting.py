###          Data preparation          ###

# import libraries bpipefore start
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as stats
import numpy as np
import seaborn as sns


# Einlesen der Daten als URL
url1 = "https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/kiwo.csv"
url2 = "https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/umsatzdaten_gekuerzt.csv"
url3 = "https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/wetter.csv"
url4 = "https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/0_DataPreparation/Wettercodes.csv"
url5 = "https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/0_DataPreparation/Feiertage%20SH.csv"
url6 = "https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/0_DataPreparation/thw-kiel-spieltage.csv"

# Überführen der Daten in DataFrames
daten = pd.read_csv(url1) # Daten der Kiwo
umswar = pd.read_csv(url2) # Umsätze der Warengruppen
wetter = pd.read_csv(url3) # Wetterdaten der Kiwos
wetterc = pd.read_csv(url4) # Wettercodes
thw = pd.read_csv(url6) # THW Kiel Spieltage
ferien = pd.read_csv(url6) # Feriendaten

# Anzeige der ersten Zeilen der DataFrames
print(daten.head()) # Ausgabe der ersten 5 Zeilen
print(umswar.head()) # Ausgabe der ersten 5 Zeilen 
print(wetter.head()) # Ausgabe der ersten 5 Zeilen
print(wetterc.head()) # Ausgabe der ersten 5 Zeilen
print(thw.head()) # Ausgabe der ersten 5 Zeilen
print(ferien.head()) # Ausgabe der ersten 5 Zeilen



# Die 3 DataFrames zusammenführen (mergen) in einen neuen gemeinsamen DataFrame mit der Methode "outer"
dataf = daten.merge(umswar, on="Datum", how = "outer") \
             .merge(wetter, on="Datum", how = "outer") \
             .merge(wetterc, on="Wettercode", how = "outer") \
             .merge(ferien, on="Datum", how = "outer") \
             .merge(thw, on="Datum", how = "outer")

# Ausgabe der ersten 5 Zeilen des neuen DataFrames
print(dataf.head())

## Featureengineering

# Hinzufügen einer zusätzlichen Spalte Regen ja/nein
dataf["Regen"] = dataf["Beschreibung"].str.contains("Regen", case=False, na=False)
dataf["Regen"] = dataf["Regen"].map({True: 1, False: 0})

# Hinzufügen einer zusätzlichen Spalte mit den Wochentagen
dataf["Datum"] = pd.to_datetime(dataf["Datum"])
dataf["Wochentag"] = dataf["Datum"].dt.weekday
dataf["Wochentag"] = dataf["Wochentag"].map({0: "Montag", 1: "Dienstag", 2: "Mittwoch", 3: "Donnerstag", 4: "Freitag", 5: "Samstag", 6: "Sonntag"}) #-> der ML Algorythmus kann ja nur mit Zahlen umgehen

# Hinzufügen einer zusätzlichen Spalte mit den Wochenenden
dataf["Wochenende"] = dataf["Wochentag"].map({"Montag": 0, "Dienstag": 0, "Mittwoch": 0, "Donnerstag": 0, "Freitag": 0, "Samstag": 1, "Sonntag": 1})

# Hinzufügen einer zusätzlichen Spalte mit den Jahreszeiten Frühling Sommer Herbst und Winter (FSHW) in Abhängigkeit des Datums
dataf["Jahreszeit_FSHW"] = dataf["Datum"].dt.month
dataf["Jahreszeit_FSHW"] = dataf["Datum"].dt.month.map({1: 4, 2: 4, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 4})

# Ausgabe der ersten 5 Zeilen des gemergten DataFrames
print(dataf.head())


### Splitting des Datensatzes####
# Laden des Dataframes -> Gibt es hier ein bessere Version?

#DF nach Datum sortieren
dataf = dataf.sort_values(by='Datum')

# Definieren der Datumsgrenzen
train_start_date = '2013-07-01'
train_end_date = '2017-07-31'
validation_end_date = '2018-07-31'

# Spliten der Daten basierend auf den Datumsgrenzen
train_data = dataf[(dataf['Datum']>= train_start_date) & (dataf['Datum'] <= train_end_date)]
validation_data = dataf[(dataf['Datum'] > train_end_date) & (dataf['Datum'] <= validation_end_date)]

# Überprüfen der Dimensionen der Datensätze
print("Training dataset dimensions:", train_data.shape)
print("Validation dataset dimensions:", validation_data.shape)

#Abspeichern der Datensätze als CSV
dataf.to_csv('dataf.csv', index=False)
train_data.to_csv ('train_data.csv', index=False)
validation_data.to_csv('validation_data.csv', index=False)