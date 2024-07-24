import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Set a random seed for reproducibility
np.random.seed(42)
n_samples = 100

# Generating a simple linear relationship (relevant feature)
X = np.random.rand(n_samples, 1) * 10  # Feature values between 0 and 10 -> Created 100 values durch das n_sample, ohne *10 ist es zwischen 0 und 1, mit 100 wäre es zwischen 0 und 100. die 1 Gibt die Dimension an. Values anscheinend positiv
y = 3 * X.squeeze() + 5 + np.random.randn(n_samples)  # squeeze entfernt dimensions. Linear relationship with Gaussian noise. Gibt anscheinend auch negative values aus, aber auch normalverteilt (zwischen + und -10 anscheindn) -> diese Werte haben ne Beziehung zu X

# Adding multiple irrelevant features (noise features)
X_noise = np.random.rand(n_samples, 10) # 100 values in 10 Spalten
X_overfit = np.hstack([X, X_noise]) # packt X und X_noise zusammen in eine Tabelle

# Creating a DataFrame to facilitate data operations
df = pd.DataFrame(X_overfit, columns=[f'feature_{i}' for i in range(11)]) # alles zusammen in Dataframe packen + Spalten benennen
df['target'] = y # target spalte hinzufügen mit y werten

df.head()

# Splitting the full dataset into a 80-20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X_overfit, y, test_size=0.2, random_state=42)

# Printing the shapes of the training and test sets including labels with titles
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")