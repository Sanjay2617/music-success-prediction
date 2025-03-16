# 🎵 Music Streaming Success Prediction 🎵  
📊 **Machine Learning for Song Popularity Analysis**  

## 📌 Overview  
This project aims to predict the success of songs on streaming platforms using **machine learning models**. We analyze **audio features**, **lyrics sentiment**, and **song metadata** to classify songs into different popularity levels. The insights from this project help the music industry make **data-driven** decisions regarding song production and marketing.  

## 📂 Dataset  
The dataset is compiled from multiple sources:  
- **Spotify Audio Features (2018, 2019)** - Includes **danceability, energy, tempo, loudness**, etc.  
- **Lyrics Data (Genius & Kaggle Millsong Dataset)** - Contains song lyrics for sentiment analysis.  
- **Merged Dataset** - Combined features with **sentiment scores** and **popularity labels**.  

## 🛠 Preprocessing Steps  
✔ Merged audio features and lyrics data  
✔ Handled missing values & outliers  
✔ Applied **SMOTE** for class imbalance correction  
✔ Normalized features using **StandardScaler**  
✔ Assigned popularity labels (Low, Medium, High)  

## 🚀 Models Used  
We implemented and compared the performance of **XGBoost** and **Random Forest** classifiers using **10-Fold Cross-Validation** to ensure robust evaluation.  

### **XGBoost Model**  
✔ Tuned hyperparameters for better precision and recall  
✔ Applied **multi-class classification** (Low, Medium, High)  
✔ Used **feature selection** for improved model interpretability  

### **Random Forest Model**  
✔ Balanced class weights for better predictions  
✔ Applied feature selection for reducing overfitting  

## 📊 Evaluation Metrics  
The models were evaluated using:  
- **Accuracy, Precision, Recall, F1-Score** (for classification performance)  
- **ROC-AUC Score** (to measure class separation)  
- **Confusion Matrix** (to analyze misclassifications)  

## 🔥 Results Comparison  
| Model           | Training Accuracy | Validation Accuracy | Test Accuracy | F1-Score | ROC-AUC |
|----------------|------------------|------------------|--------------|----------|---------|
| **XGBoost**    | 99.56%           | 92.88%           | 89.07%       | 88.93%   | 94%     |
| **Random Forest** | 97.32%        | 89.05%           | 85.34%       | 84.92%   | 91%     |

## 📈 Visualizations  
- **Feature Correlation Heatmap**  
- **Confusion Matrix Comparison (XGBoost vs. RF)**  
- **ROC Curve for Multi-Class Classification**  

## 🔍 Challenges Faced  
- Handling **class imbalance** (Class 2 had fewer instances)  
- Avoiding **overfitting** with hyperparameter tuning  
- Finding the **best trade-off** between precision and recall  

## 🔮 Future Work  
- Implementing **Deep Learning models (LSTMs)** for lyrics sentiment analysis  
- Enhancing dataset with **real-time streaming data**  
- Fine-tuning models for better interpretability  
