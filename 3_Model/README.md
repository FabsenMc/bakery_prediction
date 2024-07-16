# Model Definition and Evaluation

- **Model Selection**
Wir haben als Basis das Model aus dem Beispiel (Tensorflow-Framework) genutzt und es für unsere Zwecke angepasst, diverse Parameter iterativ verändert und jeweils die Ergebnisse verglichen. Schritt für Schritt haben wir uns so dem Ergebnis angenähert, das wir abgegeben haben. Wir sind dabei eher „konservativ“ vorgegangen, um ein Overfitting auf jeden Fall zu verhindern.
Aus Zeitmangel am Ende haben wir darauf verzichtet, das Model mittels ChatGPT noch zu optimieren. Unser Ziel war es, mit einer für uns guten Lösung durchs Ziel zu kommen.
- **Feature Engineering**
Anders als beim Baseline-Model haben wir die Variablen 
-	Regen
-	Wochenende und 
-	Windgeschwindigkeit
nacheinander aus dem Modell genommen, da diese bei den Durchläufen mit Tensorflow keine Verbesserungen gebracht haben. Das war nicht zu erwarten gewesen.
Die Variablen 
-	Windgeschwindigkeit und 
-	Verbraucherpreisindex
haben wir normalisiert, in der Hoffnung, dass dies die Qualität des Models erhöht.
Als neues Feature wurde an dieser Stelle die „Saison_Warengruppe“ eingeführt, um dem neuronalen Netz die Möglichkeit zu geben, die Werte für die Produktkategorie 6 eigens zu analysieren usw. 
Die Feature-Engineering-Arbeitsschritte fanden im Notebook „model_1_data_preparation_FINAL“ statt.
Die Daten für den Export in Richtung Kaggle wurden um Notebook „model_2_kaggle_export_preparation_FINAL“ vorbereitet.
- **Hyperparameter Tuning**
Das Tuning konzentrierte sich hauptsächlich auf die Parameter Lernrate und Epochen-Anzahl. Hierfür wurden diverse schrittweise Versuche unternommen, um die Ergebnisse zu verbessern. Am Ende sind wir bei 
learning_rate=0.001
epochs=12
gelandet. Bei den verwendeten Layern gab es bei unseren Versuchen keine weiteren Verbesserungen.
Bei den Dropout-Rates sind wir zunächst mit jeweils 0.3 vor beiden Schichten gestartet. Das Einführen der beiden Dropout-Layer verbesserte die Qualität der Ergebnisse. Ein Absenken auf 0.2 und 0.1 erhöhte die Qualität weiter. Löschten wir die Dropout-Layer, wurde die Qualität hingegen wieder schlechter.
Die Batch-Size haben wir nicht verändert.
- **Implementation**
Mittels Tensorflow – siehe Code "model_3_estimation_FINAL"
- **Evaluation Metrics**
Für die Bewertung des Tensorflow-Models wurde der MSE genutzt (Mean Squared Error) – nach dem Durchlauf jeder Epoche für die Gesamtdaten.
Für die Bewertung der Ergebnisse auf Basis der sechs Produkte wurde hingegen der MAPE (Mean absolute percentage error) genutzt. Er zeigte die großen Ergebnisunterschiede bei den einzelnen Warengruppen: Sehr gute Vorhersagen bei Kategorie 5, schlechte bei Kategorie 6.
