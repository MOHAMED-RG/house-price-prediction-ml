# House Price Prediction Project

## Project Overview

This project predicts California house prices using Machine Learning techniques.

The project workflow includes:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Data Preprocessing
* Model Building
* Hyperparameter Tuning
* Streamlit Deployment

---

# Dataset

The project uses the California Housing Dataset.

## Features Include

* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity

## Target Variable

* Median House Value

---

# Data Cleaning

The following preprocessing steps were applied:

* Handled missing values using the median
* Checked duplicate rows
* Converted categorical variables using One Hot Encoding

---

# Exploratory Data Analysis (EDA)

During EDA:

* Analyzed the target variable distribution
* Performed correlation analysis
* Used heatmaps to explore feature relationships
* Analyzed ocean proximity distribution

---

# Feature Engineering

New features were created to improve model performance:

* room_per_household
* bedrooms_per_room
* population_per_house

These engineered features improved the model’s ability to capture hidden relationships in the dataset.

---

#Models Used
1. Linear Regression

Linear Regression was used as the baseline model.

Results
MAE: 50670
R² Score: 0.63

2. Random Forest Regressor

Random Forest significantly improved prediction performance.

Results
R² Score: 0.81

3. Hyperparameter Tuning using GridSearchCV

GridSearchCV was used to optimize the Random Forest model.

Best Parameters
n_estimators = 100
max_depth = 20
min_samples_split = 2

Final Optimized Model Results

Metric	Score

MAE	32471
MSE	2524509266
RMSE	50244
R² Score	0.8073

# Model Comparison

| Model | R² Score |
|------|---------|
| Linear Regression | 0.63 |
| Random Forest (Baseline) | 0.81 |
| GridSearchCV (Final Model) | 0.81 |

Both models achieved similar performance (~0.81 R²).


# Final Model (Selected)

The final model used for deployment is GridSearchCV Optimized Random Forest.

GridSearchCV was selected because it provides a more structured and systematic approach to hyperparameter tuning, ensuring better reproducibility and model stability.


### Performance

* MAE: 32471
* RMSE: 50154
* R² Score: 0.81


---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib

---

# Streamlit Application

A Streamlit web application was developed for real-time house price prediction.

Users can input:

* Median Income
* Location Information
* Number of Rooms
* Population Information
* Ocean Proximity

The application predicts the estimated house price instantly.

## Live Demo

https://house-price-prediction-ml-rcfsthuqqhowawk87jlhma.streamlit.app/

---

# Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── housing.csv
├── house_price_model.pkl
├── requirements.txt
├── README.md
├── house-price-project.ipynb
```

---

# Run The Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

---
# Key Insights

* Median income was the most important feature affecting house prices.
* Houses located near the ocean generally had higher prices.
* Feature engineering improved model performance compared to the baseline model.
* Random Forest performed significantly better than Linear Regression.
* Hyperparameter tuning using GridSearchCV provided a structured optimization process and was selected as the final model despite similar performance to the baseline Random Forest.
---

# Future Improvements

* Improve model performance using more advanced models such as XGBoost or LightGBM.
* Perform deeper feature engineering and feature selection.
* Add more interactive visualizations to the Streamlit application.
* Deploy the application using cloud services for better scalability.
* Experiment with ensemble learning techniques to reduce prediction error.

---

# Author

Mohamed Atia

Aspiring Data Scientist
