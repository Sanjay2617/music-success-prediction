import pandas as pd
import lyricsgenius
import time
import re

# Load dataset
file_path = "/Users/sanro/Project/songs_normalize 2.csv"  
df = pd.read_csv(file_path)

# Initialize Genius API 
GENIUS_ACCESS_TOKEN = "WFXSQuatTKQql5FmgfZWzLSCf63vn4BxlnRkkYqMDR57TL-mJdAlaQhU8jcMth0d"
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN, timeout=10)
genius.verbose = False  
genius.remove_section_headers = True  
genius.skip_non_songs = True  

# Limit to first 100 songs
df = df.head(100)

# Function to clean lyrics
def clean_lyrics(lyrics):
    """Cleans lyrics by removing metadata, contributors, and translations."""
    if not lyrics:
        return "Lyrics Not Found"
    
    lyrics = lyrics.replace("\n", " ")  
    lyrics = re.sub(r'\[.*?\]', '', lyrics)  # Remove text inside brackets
    lyrics = re.sub(r'^\s*(.*?Lyrics)', '', lyrics, flags=re.IGNORECASE)  
    lyrics = re.sub(r'Contributors.*?Translations', '', lyrics, flags=re.IGNORECASE)  
    return lyrics.strip()  

# Function to fetch lyrics
def fetch_lyrics(song_name, artist_name, retries=3):
    """Fetch and clean lyrics from Genius API."""
    for attempt in range(retries):
        try:
            print(f"🎵 Fetching lyrics for: {song_name} by {artist_name}... (Attempt {attempt + 1})")
            song = genius.search_song(song_name, artist_name)
            if song:
                return clean_lyrics(song.lyrics)
            else:
                return "Lyrics Not Found"
        except Exception as e:
            print(f"⚠ Error fetching lyrics for {song_name}: {e}")
            time.sleep(2)  # Wait before retrying

    return "Error"

df["lyrics"] = None

for index, row in df.iterrows():
    song_name = row["song"]  
    artist_name = row["artist"]  

    df.at[index, "lyrics"] = fetch_lyrics(song_name, artist_name)
    
    
    time.sleep(2)

# Save the results
output_file = "songs_with_cleaned_lyrics.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print(f" Lyrics saved to `{output_file}`!")