# Music-Success-Prediction
A project analyzing song features and lyrics to predict song success using Machine Learning
The objective of this project is to predict the success of songs based on their musical features and lyrics. Due to limitations with the Spotify API, we switched to a normal dataset containing features like danceability, energy, tempo, valence, and loudness. Additionally, we extracted lyrics from Genius API for text-based analysis. The goal is to train a machine learning model to predict a song’s success using audio characteristics and textual sentiment.

# Current Approach
	1.Data Collection
	    •Used a pre-existing dataset containing song features.
	    •Extracted lyrics for 100 songs using the Genius API.
	2.Data Preprocessing
	    •Cleaned missing values and duplicates.
	    •Normalized song features (danceability, energy, etc.).
	    •Processed textual data (lyrics) for sentiment analysis.
	3.Feature Engineering
	    •Extracted key numerical (danceability, energy, tempo, valence, loudness) and textual (sentiment score) features.
	    •Created a combined dataset with both audio features & lyrics.
	4.Machine Learning Models
	    •Regression-based models (Random Forest, XGBoost) to predict song popularity.
	    •Classification models (Logistic Regression, Neural Networks) to classify songs into hit or non-hit categories.
	5.Database Integration
	    •Database Selection: Snowflake
	    •Reason: Handles structured data, supports large-scale analytics, and integrates well with ML pipelines.
     
# Data Collection 
Two types of data were collected for this project:
 * Song Data – This includes attributes such as energy, danceability, loudness, and popularity. It was sourced from Kaggle: Top Hits Spotify (2000–2019).https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019
 * Lyrics Data – Lyrics were collected by web scraping using the Genius API.

# Data Preprocessing 
The dataset undergoes multiple preprocessing steps to ensure data quality and consistency. First, missing values are handled by dropping rows with any missing values to maintain data integrity. Next, MinMax Scaling is applied to numerical features, such as danceability, energy, loudness, tempo, and valence, to normalize them within the range of 0 to 1. This helps in ensuring that all numerical attributes are on a comparable scale without distorting their relative differences. The cleaned and scaled dataset is then stored in Snowflake for further analysis.

# Exploratory Data Analysis
EDA is performed to gain insights into the dataset’s structure and relationships between different musical and lyrical attributes. The describe() function provides summary statistics, including count, mean, standard deviation, and range for each numerical feature. A correlation heatmap is generated to visualize relationships between different variables, revealing how strongly certain features (e.g., energy and danceability) are associated with each other. Additionally, histograms illustrate the distribution of key features, showing how values are spread across different ranges. A scatter plot of danceability vs. energy further highlights patterns and trends in song characteristics. These visualizations help in understanding the dataset better before further modeling or analysis. 

# Project Workflow Overview

1.	Data Collection (Data_Collection.py)
The first step involves collecting and examining the raw data to understand its structure and characteristics. This script is used to load, inspect, and merge datasets to create a combined dataset containing various musical features. The objective is to assess the initial quality of the data before proceeding with preprocessing.
2.	Data Preprocessing (Data_Preprocessing.py)
Once the data is collected, we use the Songs.csv it is cleaned and prepared for further analysis. This script removes missing values, normalizes numerical features using MinMax Scaling, and ensures data consistency. After preprocessing, the cleaned dataset is saved as processed_songs.csv, which serves as the foundation for further analysis. The cleaned dataset is also stored in Snowflake for efficient data retrieval.
3.	Exploratory Data Analysis (EDA.py)
With the preprocessed dataset, exploratory data analysis (EDA) is conducted to understand trends, relationships, and distributions within the data. This includes summary statistics, correlation analysis, feature distributions through histograms, and scatter plots for key features like danceability vs. energy. These visualizations provide insights into the dataset before further feature engineering or modeling.
4.	Lyrics Data Collection (Genius.py)
After cleaning and analyzing the song features, the Genius API is used to fetch lyrics for each song present in the processed_songs.csv file. This script queries Genius based on song titles and artists, retrieves the lyrics, and processes them for sentiment analysis. The collected lyrics are then stored for integration with existing musical features, allowing for combined analysis of both audio characteristics and lyrical sentiment in the songs_with_cleaned_lyrics.csv file.
5.	The files Songs.csv contains the Audio features and the Lyrics_only.csv file has only the lyrics for the first 100 songs. 
