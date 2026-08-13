# Rainfall Prediction using Machine Learning

A machine learning project that predicts whether rainfall will occur based on various weather conditions. The project uses a **Random Forest Classifier** and provides an interactive **Streamlit web application** for real-time predictions.

## Project Overview

Rainfall prediction is a binary classification problem where the model predicts one of two outcomes:

- **1 → Rainfall**
- **0 → No Rainfall**

The project includes data preprocessing, exploratory data analysis, missing-value handling, class balancing, feature selection, model training, hyperparameter tuning, and evaluation.

## Features

- Data preprocessing and cleaning
- Missing-value handling
- Exploratory Data Analysis (EDA)
- Correlation analysis
- Outlier analysis using boxplots
- Class balancing using resampling
- Feature selection
- Random Forest classification
- Hyperparameter tuning using GridSearchCV
- Cross-validation
- Model evaluation using accuracy, classification report, and confusion matrix
- Interactive Streamlit web application

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Pickle**

## Dataset

The project uses a rainfall dataset containing weather-related features such as:

- Pressure
- Dewpoint
- Humidity
- Cloud
- Sunshine
- Wind Direction
- Wind Speed
- Rainfall

The target variable is:

```text
Rainfall
0 → No Rainfall
1 → Rainfall
