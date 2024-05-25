###     Deskriptive Statistik erstellen     ###

# Basic Eigenschaften

dataf.columns
dataf.shape
dataf.info()
dataf.describe() # machen nur bei einigen Variablen Sinn

dataf["Umsatz"].describe()
dataf["Warengruppe"].describe()


# dataf Dataframe beschnitten um nur Werte anzuzeigen die mit einer Kieler Woche korreliert werden können und zu denen Umsatzdaten vorliegen
kiwo_df = dataf[(dataf["KielerWoche"] == 1) & (dataf["Umsatz"].notnull())]
kiwo_df.head()
kiwo_df.describe()

# dataf Dataframe beschnitten um nur Werte anzuzeigen zu denen Umsatzdaten vorliegen
umsatz_df = dataf[(dataf["Umsatz"].notnull())]
umsatz_df.head()
umsatz_df.describe()


###        Visualisierung erstellen         ###

# Histogram und Grundparameter Statistik für Wettervariablen erstellen
# Liste der Wettervariablen
weather_variables = ['Bewoelkung', 'Temperatur', 'Windgeschwindigkeit', 'Wettercode']

    # Schleife über jede Wettervariable über das gesamte Jahr
    for var in weather_variables:
        # Histogramm erstellen
        plt.hist(dataf[var], bins=95, color='skyblue', edgecolor='black')
        plt.xlabel(var)
        plt.ylabel('Häufigkeit')
        plt.title(f'Histogramm der {var}')
        plt.grid(True)
        plt.show()
        
        # Grundlegende Parameter berechnen
        mean_var = dataf[var].mean()
        median_var = dataf[var].median()
        min_var = dataf[var].min()
        max_var = dataf[var].max()
        std_var = dataf[var].std()
        
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
    kiwo_dataf = dataf[dataf["KielerWoche"] == 1] # Filter dataf DataFrame for KielerWoche

    for var in weather_variables:
        # Histogramm erstellen
        plt.hist(kiwo_dataf[var], bins=95, color='skyblue', edgecolor='black')
        plt.xlabel(var)
        plt.ylabel('Häufigkeit')
        plt.title(f'Histogramm der {var}')
        plt.grid(True)
        plt.show()
        
        # Grundlegende Parameter berechnen
        mean_var = kiwo_dataf[var].mean()
        median_var = kiwo_dataf[var].median()
        min_var = kiwo_dataf[var].min()
        max_var = kiwo_dataf[var].max()
        std_var = kiwo_dataf[var].std()
        
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
    plt.hist(kiwo_dataf["Warengruppe"], bins=5, color='green', edgecolor='black')
    plt.xlabel("Warenguppe")
    plt.ylabel('Häufigkeit')
    plt.title(f'Histogramm der {"Warenguppe"}')
    plt.grid(True)
    plt.show()