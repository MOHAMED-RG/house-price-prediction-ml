# House Price Prediction Project

## Project Overview

This project predicts California house prices using Machine Learning techniques.

### Workflow
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Building
- Hyperparameter Tuning
- Streamlit Deployment

---

# Dataset

The project uses the California Housing Dataset.

### Features
- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

### Target Variable
- Median House Value

---

# Data Cleaning

- Handled missing values using the median
- Checked duplicate rows
- Applied One-Hot Encoding for categorical variables

---

# Exploratory Data Analysis (EDA)

- Analyzed target variable distribution
- Performed correlation analysis
- Used heatmaps to explore feature relationships
- Analyzed ocean proximity distribution

---

# Feature Engineering

New features were created to improve model performance:

- room_per_household
- bedrooms_per_room
- population_per_house

These features helped capture hidden relationships in the data.

---

# Models Used

## 1. Linear Regression (Baseline)

### Results
- MAE: 50670  
- R² Score: 0.63  

---

## 2. Random Forest Regressor

### Results
- R² Score: 0.81  

---

## 3. Hyperparameter Tuning (GridSearchCV)

GridSearchCV was used to optimize the Random Forest model.

### Best Parameters
- n_estimators: 100  
- max_depth: 20  
- min_samples_split: 2  

### Results
- MAE: 32471  
- MSE: 2524509266  
- RMSE: 50244  
- R² Score: 0.8073  

---

# Model Comparison

| Model | R² Score |
|------|---------|
| Linear Regression | 0.63 |
| Random Forest (Baseline) | 0.81 |
| GridSearchCV (Final Model) | 0.81 |

Both models achieved similar performance (~0.81 R²).

---

# Final Model (Selected)

The final model used for deployment is **GridSearchCV Optimized Random Forest**.

GridSearchCV was selected because it provides a more structured and systematic approach to hyperparameter tuning, ensuring better reproducibility and model stability.

### Final Performance
- MAE: 32471  
- RMSE: 50154  
- R² Score: 0.81  

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# Streamlit Application

A Streamlit web app was developed for real-time house price prediction.

### Inputs
- Median Income
- Location Information
- Number of Rooms
- Population
- Ocean Proximity

### Output
- Predicted house price instantly

🔗 Live Demo:  
https://house-price-prediction-ml-rcfsthuqqhowawk87jlhma.streamlit.app/

---

# Project Structure

```
text
House-Price-Prediction/
│
├── app.py
├── housing.csv
├── house_price_model.pkl
├── requirements.txt
├── README.md
├── house-price-project.ipynb


