import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load dataset
file_path = "songs_normalize.csv"
df = pd.read_csv(file_path)

# Drop unnecessary columns (modify based on your dataset structure)
df = df[['song_name', 'danceability', 'energy', 'loudness', 'tempo', 'valence', 'popularity']]

# Handle missing values (Fill with mean or drop)
df.fillna(df.mean(), inplace=True)

# Normalize numerical features
scaler = MinMaxScaler()
df[['danceability', 'energy', 'loudness', 'tempo', 'valence']] = scaler.fit_transform(
    df[['danceability', 'energy', 'loudness', 'tempo', 'valence']]
)

# Save cleaned dataset
df.to_csv("processed_songs.csv", index=False)
print("Data preprocessing complete. Saved as 'processed_songs.csv'")
