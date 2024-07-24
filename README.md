# Umsatzprognose für eine Bäckereifiliale in Kiel

## Repository Link

https://github.com/FabsenMc/bakery_prediction/tree/main

## Beschreibung des Projekts

This project focuses on sales forecasting for a bakery branch, utilizing historical sales data spanning from July 1, 2013, to July 30, 2018, to inform inventory and staffing decisions. We aim to predict future sales for six specific product categories: Bread, Rolls, Croissants, Confectionery, Cakes, and Seasonal Bread. Our methodology integrates statistical and machine learning techniques, beginning with a baseline linear regression model to identify fundamental trends, and progressing to a sophisticated neural network designed to discern more nuanced patterns and enhance forecast precision. The initiative encompasses data preparation, crafting bar charts with confidence intervals for visualization, and fine-tuning models to assess their performance on test data from August 1, 2018, to July 30, 2019, using the Mean Absolute Percentage Error (MAPE) metric for each product category.

In diesem Projekt streben wir an, mit Hilfe eines machine learning models eine Umsatzprognose für eine Bäckerei Filiale in Kiel zu erstellen. Dafür nutzen wir die aufgezeichneten Umsätze vom 1. Juli 2013 bis zum 30. Juli 2018, um die zukünftigen Umsätze für 6 Kategorien von Backwaren vorauszusagen: Brot, Brötchen, Croissants, Süßwaren, Kuchen und saisonales Brot. Weiterhin Analysieren wir den Einfluss von äußeren Faktoren wie  Temperatur, Wetter, Feier- oder Ferientage etc., um ein genaueres Ergebnis zu erzielen.
In unserem Ansatz werden wir zunächst die bestehenden Daten statistisch analysieren und gegebenfalls zusätzliche Informationen acquirieren, die für die Analyse von Vorteil sein könnten. Im Anschluss erstellen wir ein linerares Regressionsmodell, um erste Tendenzen zu finden und die Zusammenhänge und den Einfluss der einzelnen Faktoren zu ermittlen. Unter Zuhilfenahme der Information aus den ersten Schritten erstellen wir ein neuronales Netzwerk, welches im weiteren Verlauf immer  weiter  feinabgestimmt wird. Zuletzt wird es uns möglich sein, anhand von Testdaten vom 1. August 2018 bis zum 30. Juli 2019 eine Umsatzprognose zu erstellen. Um die enstehenden Ergebnisse zu bewerten, nutzen wir die MAPE-Metrik (Mean Absolute Percentage Error) für jede einzelne Backwarenkategorie.

### Zusammenfassung der best möglichen Resultate

-   **Beste Model:** [Name of the best-performing model]
-   **Evaluations Metric:** MAPE
-   **Resultate nach Kategorien**:
    -   **Brot** (1): [XX]%
    -   **Brötchen** (2): [XX]%
    -   **Croissants** (3): [XX]%
    -   **Süßwaren** (4): [XX]%
    -   **Kuchen** (5): [XX]%
    -   **Saisonales Brot** (6): [XX]%

## Dokumentation

1.  [**Data Import and Preparation**](0_DataPreparation/)
3.  [**Dataset Characteristics (Barcharts)**](1_DatasetCharacteristics/)
4.  [**Baseline Model**](2_BaselineModel/)
5.  [**Model Definition and Evaluation**](3_Model/)
6.  [**Presentation**](4_Presentation/README.md)

## Cover Image

![](CoverImage/Cover_Image.jpg)
