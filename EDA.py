import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/Users/sanro/Project/processed_songs.csv" 
df = pd.read_csv(file_path)

# General statistics
print(df.describe())

# Ensure only numerical columns for correlation
df_numeric = df.select_dtypes(include=['number'])

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Histogram of key features
df_numeric.hist(figsize=(12,12), bins=30)
plt.suptitle("Feature Distributions", fontsize=16)
plt.show()

# Scatter plot for danceability vs. energy
plt.figure(figsize=(8,6))
sns.scatterplot(x=df["danceability"], y=df["energy"], alpha=0.6)
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.title("Danceability vs. Energy")
plt.show()