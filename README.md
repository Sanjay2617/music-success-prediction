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
     
