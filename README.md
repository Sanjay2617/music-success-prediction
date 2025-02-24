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
 Markup : 
 * Song Data – This includes attributes such as energy, danceability, loudness, and popularity. It was sourced from Kaggle: Top Hits Spotify (2000–2019).https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019
 * Lyrics Data – Lyrics were collected by web scraping using the Genius API.

# Data Preprocessing 
The dataset undergoes multiple preprocessing steps to ensure data quality and consistency. First, missing values are handled by dropping rows with any missing values to maintain data integrity. Next, MinMax Scaling is applied to numerical features, such as danceability, energy, loudness, tempo, and valence, to normalize them within the range of 0 to 1. This helps in ensuring that all numerical attributes are on a comparable scale without distorting their relative differences. The cleaned and scaled dataset is then stored in Snowflake for further analysis.

# Exploratory Data Analysis
EDA is performed to gain insights into the dataset’s structure and relationships between different musical and lyrical attributes. The describe() function provides summary statistics, including count, mean, standard deviation, and range for each numerical feature. A correlation heatmap is generated to visualize relationships between different variables, revealing how strongly certain features (e.g., energy and danceability) are associated with each other. Additionally, histograms illustrate the distribution of key features, showing how values are spread across different ranges. A scatter plot of danceability vs. energy further highlights patterns and trends in song characteristics. These visualizations help in understanding the dataset better before further modeling or analysis. 
