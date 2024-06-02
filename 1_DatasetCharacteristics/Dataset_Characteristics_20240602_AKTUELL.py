###     Deskriptive Statistik erstellen     ###

# import libraries bpipefore start
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as stats
import numpy as np
import seaborn as sns

# laden der Trainingsdaten

train_data = pd.read_csv("https://raw.githubusercontent.com/FabsenMc/bakery_prediction/main/0_DataPreparation/train_data.csv")
print(train_data.head())

### Basic Eigenschaften ###

train_data.columns
train_data.shape
train_data.info()
train_data.describe() # machen nur bei einigen Variablen Sinn

train_data["Umsatz"].describe()
train_data["Warengruppe"].describe()

### Visualisierung ###

## HISTOGRAMME ##
# Temperatur
plt.hist(train_data['Temperatur'].dropna(), bins=30)
# Hinzufügen von Titeln und Labels
plt.title('Histogramm Temperatur')
plt.xlabel('Temperatur')
plt.ylabel('Häufigkeit')
plt.show()

# Umsatz
plt.hist(train_data['Umsatz'].dropna(), bins=30)
# Hinzufügen von Titeln und Labels
plt.title('Histogramm Umsatz')
plt.xlabel('Umsatz')
plt.ylabel('Häufigkeit')
plt.show()

# -> Daten sehen linksschief verteilt aus. Umsatz soll geschätzt werden. Grundannahme von linearen Modellen liegt nicht vor. Daten müssen evtl. transformiert werden.


# Warengruppe
plt.hist(train_data['Warengruppe'].dropna(), bins=30)
# Hinzufügen von Titeln und Labels
plt.title('Histogramm Warengruppe')
plt.xlabel('Warengruppe')
plt.ylabel('Häufigkeit')
plt.show()

# Windgeschwindigkeit
plt.hist(train_data['Windgeschwindigkeit'].dropna(), bins=30)
# Hinzufügen von Titeln und Labels
plt.title('Histogramm Windgeschwindigkeit')
plt.xlabel('Windgeschwindigkeit')
plt.ylabel('Häufigkeit')
plt.show()

# Wettercode
plt.hist(train_data['Wettercode'].dropna(), bins=30)
# Hinzufügen von Titeln und Labels
plt.title('Histogramm Wettercode')
plt.xlabel('Wettercode')
plt.ylabel('Häufigkeit')
plt.show()

## SCATTERPLOTS
#Temperatur vs. Umsatz
plt.figure(figsize=(8, 6))
plt.scatter(train_data['Temperatur'], train_data['Umsatz'], label='Daten')
plt.xlabel('Temperatur')
plt.ylabel('Umsatz')
plt.title('Scatterplot Temperatur vs Umsatz')
plt.show()












# ab hier alte Sachen von Fabian, eventuell oben integrieren



# train_data Dataframe beschnitten um nur Werte anzuzeigen die mit einer Kieler Woche korreliert werden können und zu denen Umsatzdaten vorliegen
kiwo_df = train_data[(train_data["KielerWoche"] == 1) & (train_data["Umsatz"].notnull())]
kiwo_df.head()
kiwo_df.describe()

###        Visualisierung erstellen         ###

# Histogram und Grundparameter Statistik für Wettervariablen erstellen
# Liste der Wettervariablen
weather_variables = ['Bewoelkung', 'Temperatur', 'Windgeschwindigkeit', 'Wettercode']

    # Schleife über jede Wettervariable über das gesamte Jahr
    for var in weather_variables:
        # Histogramm erstellen
        plt.hist(train_data[var], bins=95, color='skyblue', edgecolor='black')
        plt.xlabel(var)
        plt.ylabel('Häufigkeit')
        plt.title(f'Histogramm der {var}')
        plt.grid(True)
        plt.show()
        
        # Grundlegende Parameter berechnen
        mean_var = train_data[var].mean()
        median_var = train_data[var].median()
        min_var = train_data[var].min()
        max_var = train_data[var].max()
        std_var = train_data[var].std()
        
        # Statistische Grundparameter ausgeben
        print(f"\nStatistische Grundparameter für {var}:")
        print("Mittlerer Wert:", mean_var)
        print("Median:", median_var)
        print("Minimum:", min_var)
        print("Maximum:", max_var)
        print("Standardabweichung:", std_var)
        print("-----------------------------")

    # Schleife über jede Wettervariable für die Umsatzwerte existieren über das gesamte Jahr

    for var in weather_variables:
        # Histogramm erstellen
        plt.hist(umsatz_df[var], bins=95, color='skyblue', edgecolor='black')
        plt.xlabel(var)
        plt.ylabel('Häufigkeit')
        plt.title(f'Histogramm der {var}')
        plt.grid(True)
        plt.show()
        
        # Grundlegende Parameter berechnen
        mean_var = umsatz_df[var].mean()
        median_var = umsatz_df[var].median()
        min_var = umsatz_df[var].min()
        max_var = umsatz_df[var].max()
        std_var = umsatz_df[var].std()
        
        # Statistische Grundparameter ausgeben
        print(f"\nStatistische Grundparameter für {var}:")
        print("Mittlerer Wert:", mean_var)
        print("Median:", median_var)
        print("Minimum:", min_var)
        print("Maximum:", max_var)
        print("Standardabweichung:", std_var)
        print("-----------------------------")
        
    # Schleife über jede Wettervariable über die Zeit der Kiwo
    kiwo_train_data = train_data[train_data["KielerWoche"] == 1] # Filter train_data train_datarame for KielerWoche

    for var in weather_variables:
        # Histogramm erstellen
        plt.hist(kiwo_train_data[var], bins=95, color='skyblue', edgecolor='black')
        plt.xlabel(var)
        plt.ylabel('Häufigkeit')
        plt.title(f'Histogramm der {var}')
        plt.grid(True)
        plt.show()
        
        # Grundlegende Parameter berechnen
        mean_var = kiwo_train_data[var].mean()
        median_var = kiwo_train_data[var].median()
        min_var = kiwo_train_data[var].min()
        max_var = kiwo_train_data[var].max()
        std_var = kiwo_train_data[var].std()
        
        # Statistische Grundparameter ausgeben
        print(f"\nStatistische Grundparameter für {var}:")
        print("Mittlerer Wert:", mean_var)
        print("Median:", median_var)
        print("Minimum:", min_var)
        print("Maximum:", max_var)
        print("Standardabweichung:", std_var)
        print("-----------------------------")
    
# Histogram und Grundparameter Statistik für Warengruppen erstellen

    # Histogramm erstellen für gesamtes Jahr
    plt.hist(umsatz_df["Warengruppe"], bins=6, color='green', edgecolor='black')
    plt.xlabel("Warenguppe")
    plt.ylabel('Häufigkeit')
    plt.title(f'Histogramm der {"Warenguppe"}')
    plt.grid(True)
    plt.show()
    
    # Histogramm erstellen für Kiwozeit
    plt.hist(kiwo_train_data["Warengruppe"], bins=5, color='green', edgecolor='black')
    plt.xlabel("Warenguppe")
    plt.ylabel('Häufigkeit')
    plt.title(f'Histogramm der {"Warenguppe"}')
    plt.grid(True)
    plt.show()