# Dataset Characteristics

Das Notebook Dataset_Characteristics enthält eine eingehende Analyse des Datensatzes, der für die Vorhersage des Umsatzes einer Bäckerei in Kiel verwendet wurde. Das Verständnis des Datensatzes ist entscheidend für die Erstellung genauer und zuverlässiger Modelle für maschinelles Lernen. Diese Analyse umfasst einen Überblick über den Datensatz, die Identifizierung fehlender Werte, die Untersuchung von Merkmalsverteilungen und die Analyse von Korrelationen zwischen Merkmalen.

## Dataset Overview

Im ersten Schritt wollten wir hier ein besseres Verständniss über unseren gesamten Datensatz bekommen und haben den Umfang des Datensatzes betrachtet. 
Der von uns erstellte Datensatz enthielt Umsatz-Daten vom 1. Juli 2013 bis zum 30.Juli 2018. Die von uns hinzugefügten Datens umfassten jedoch einen etwas größeren Bereich mit Start im Jahr 2012. Insgesamt umfasst der finale Datensatz somit 10437 Zeilen sowie 23 Spalten / Variablen. Die wichtigsten Variablen sind im Folgenden kurz dargestellt (unvollständige liste)

| Spalte                  | Beschreibung                                                                             | Datentyp   |
|-------------------------|------------------------------------------------------------------------------------------|------------|
| Datum                   | Das Datum der aufgezeichneten Verkäufe                                                   | Objekt     |
| KielerWoche             | Indikator dafür, ob das Datum in die Kieler Woche fällt                                  | Kategorie  |
| Warengruppe             | Kategorie des Backwarenprodukts                                                          | Kategorie  |
| Umsatz                  | Verkaufszahlen                                                                           | Float64    |
| Bewoelkung              | Bewölkung                                                                                | Float64    |
| Temperatur              | Temperatur am gegebenen Datum                                                            | Float64    |
| Windgeschwindigkeit     | Windgeschwindigkeit                                                                      | Float64    |
| Wettercode              | Wettercode, der bestimmte Wetterbedingungen darstellt                                    | Float64    |
| FerienSH                | Indikator dafür, ob das Datum in die Schulferien in Schleswig-Holstein fällt             | Kategorie  |
| Feiertag                | Indikator dafür, ob das Datum ein Feiertag ist                                           | Kategorie  |
| Umschlag                | Indikator dafür, ob das Datum auf den Umschlag in Kiel fiel                              | Kategorie  |
| Weihnachtsmarkt         | Indikator dafür, ob das Datum in die Weihnachtsmarktzeit fällt                           | Kategorie  |
| Verbraucherpreisindex   | Verbraucherpreisindex                                                                    | Float64    |
| Regen                   | Indikator für Regentag                                                                   | Kategorie  |
| Schnee                  | Indikator für Schneetag                                                                  | Kategorie  |
| Wochentag_MDMDFSS       | Wochentag                                                                                | Kategorie  |
| Wochenende              | Indikator für Wochenenden                                                                | Kategorie  |
| Jahreszeit_FSHW         | Jahreszeit                                                                               | Kategorie  |
| Temperatur_Kategorie    | Kategorie für Temperaturbereiche                                                         | Objekt     |
| THW_heimspiel           | Indikator dafür, ob ein Heimspiel der THW Kiel Handballmannschaft stattfindet            | Kategorie  |


## Missing Values

Die Identifizierung fehlender Werte ist entscheidend, um die Genauigkeit unserer Modelle sicherzustellen. Zu Beginn unseres Projekts hatten wir viele fehlende Werte, insbesondere bei kategorialen Variablen. Dies lag daran, dass die Umwandlung der Variablenklassen zwar in der Datenvorbereitung erfolgte, aber nicht in jedem Skript wiederholt wurde. Beim Neuladen des Datensatzes aus einer CSV-Datei wurden kategoriale Variablen als Objekte gespeichert und fehlende Werte als NaN interpretiert.

Nach Korrektur dieses Fehlers verbesserten sich unsere Daten erheblich. Auch zu beachten bei Betrachtung der Null-Werte von Umsatz und Warengruppe ist, dass der vorliegende Datensatz etwas früher im Jahr 2012 beginnt, wo keine Umsatzdaten vorliegen. Diese Werte werden im späteren Verlauf sowieso herausgenommen. Zur Visualisierung der fehlenden Werte haben wir neben der reinen Wertausgabe auch einen Matrix-Plot, ein Balkendiagramm und ein Dendrogramm erstellt. Im Folgenden ist die Tabelle der fehlenden Werte zur kurzen Übersicht dargestellt:

| Spalte                  | Fehlende Werte |
|-------------------------|----------------|
| Warengruppe             | 1103           |
| Umsatz                  | 1103           |
| Bewoelkung              | 389            |
| Temperatur              | 334            |
| Windgeschwindigkeit     | 334            |
| Wettercode              | 2856           |
| FerienSH                | 38             |
| Feiertag                | 38             |
| Verbraucherpreisindex   | 30             |
| Temperatur_Kategorie    | 335            |


## Feature Distributions 

In diesem Abschnitt haben wir die Verteilung der einzelnen Variablen betrachtet. Zunächst erstellten wir für jede Variable ein Histogramm oder Säulendiagramm für die reine Häufigkeit der jeweiligen Variablen. In einem zweiten Schritt erstellten wir weitere Säulendiagramme der Variablen in Relation zum Umsatz, unserer Zielvariable und berechneten jeweils auch das 95%ige Konfidenzintervall.
Im Notebook sind die Ergebnisse nach Variable aufgeteilt zu finden. 

## Correlations

Zuletzt erstellten wir eine Korrelationsmatrix für unsere Variablen. Die Korrelationsmatrix bietet einen Überblick über die Beziehungen zwischen den verschiedenen Variablen im Datensatz. Hierbei werden die Korrelationen mit Werten zwischen -1 und 1 dargestellt, wobei 1 eine perfekte positive Korrelation und -1 eine perfekte negative Korrelation anzeigt. Ein Wert von 0 bedeutet, dass keine Korrelation besteht. 