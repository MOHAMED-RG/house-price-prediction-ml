# 🏠 California House Price Prediction

## 📌 Project Overview

This project predicts median house values in California using machine learning. It covers the complete machine learning workflow, from data cleaning and exploratory data analysis (EDA) to feature engineering, model training, hyperparameter tuning, and deployment using Streamlit.

The goal is to build a model that estimates house values based on housing characteristics and location-related features.

## 🎯 Project Objectives

- Explore and understand the California Housing dataset.
- Clean and preprocess the data.
- Perform exploratory data analysis (EDA).
- Create new features to improve model performance.
- Train and evaluate machine learning models.
- Optimize a Random Forest model using GridSearchCV.
- Deploy the trained model using Streamlit.

## 📊 Dataset

The dataset contains **20,640 records** and housing-related features.

**Dataset:** [California Housing Prices Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

### Features

- `longitude`: Geographic longitude.
- `latitude`: Geographic latitude.
- `housing_median_age`: Median age of houses in the area.
- `total_rooms`: Total number of rooms.
- `total_bedrooms`: Total number of bedrooms.
- `population`: Population of the area.
- `households`: Number of households.
- `median_income`: Median income in the area.
- `ocean_proximity`: Proximity to the ocean.

**Target variable:** `median_house_value`

## 🧹 Data Cleaning and Preprocessing

The data preparation process included:

- Checking for missing values.
- Handling missing values in `total_bedrooms`.
- Inspecting data types and duplicate records.
- Preparing numerical and categorical features for modeling.
- Encoding categorical data where required.

## 🔍 Exploratory Data Analysis (EDA)

EDA was used to understand the distribution of house prices and the relationships between numerical features.

### 1. House Price Distribution

![House Price Distribution](house-price-distribution.png)

The distribution shows that house values are not perfectly symmetrical. The visible concentration near the upper price limit reflects the dataset's capped house values.

### 2. Correlation Heatmap

![Correlation Heatmap](correlation-heatmap.png)

Key observations:

- `median_income` has a positive correlation of approximately **0.69** with `median_house_value`.
- `longitude` and `latitude` have a strong negative correlation of approximately **-0.92** with each other.
- `total_rooms`, `total_bedrooms`, `population`, and `households` have strong positive correlations with one another.

Correlation indicates association, not causation.

## ⚙️ Feature Engineering

Three additional features were created to represent housing characteristics more meaningfully:

- `room_per_household`: Average number of rooms per household.
- `bedrooms_per_room`: Proportion of bedrooms relative to total rooms.
- `population_per_house`: Average population per household.

These features were introduced to help the model capture additional patterns in the data.

## 🤖 Model Training and Evaluation

Two regression models were trained and evaluated.

### Models

**1. Linear Regression**

Used as a baseline model to establish an initial performance benchmark.

**2. Random Forest Regressor**

Used to capture more complex relationships between housing features and house values.

GridSearchCV was used to tune the Random Forest hyperparameters.

### Model Performance

| Model | MAE | R² Score |
|---|---:|---:|
| Linear Regression | 50,670 | 0.63 |
| Tuned Random Forest | 32,471 | 0.8073 |

The tuned Random Forest model achieved a lower Mean Absolute Error (MAE) and a higher R² score than Linear Regression.

### Best Hyperparameters

The best parameters found through GridSearchCV were:

- `n_estimators`: 100
- `max_depth`: 20
- `min_samples_split`: 2

### Final Model Metrics

| Metric | Value |
|---|---:|
| Mean Absolute Error (MAE) | 32,471 |
| Mean Squared Error (MSE) | 2,524,509,266 |
| Root Mean Squared Error (RMSE) | Approximately 50,244 |
| R² Score | 0.8073 |

The final model explains approximately **80.73% of the variance** in the target variable on the evaluated dataset.

## 🚀 Streamlit Deployment

The trained model is deployed as an interactive web application where users can enter housing characteristics and receive a predicted house value.

**[Open the Live Application](https://house-price-prediction-ml-rcfsthuqqhowawk87jlhma.streamlit.app/)**

## 🛠️ Technologies Used

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Hyperparameter Tuning:** GridSearchCV
- **Model Serialization:** Joblib
- **Web Application:** Streamlit
- **Development:** Jupyter Notebook, Git, GitHub

## 📁 Project Structure

```text
house-price-prediction-ml/
│
├── images/
│   ├── house-price-distribution.png
│   └── correlation-heatmap.png
│
├── house_price_prediction.ipynb
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

- `images/`: Contains the visualizations displayed in this README.
- `house_price_prediction.ipynb`: Contains data cleaning, EDA, feature engineering, model training, and evaluation.
- `app.py`: Contains the Streamlit application.
- `model.pkl`: Stores the trained model.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Documents the project and its results.

*Note: Make sure the filenames above match the actual files in your repository.*

## 💡 Key Takeaways

- Data exploration helps identify patterns and relationships in housing data.
- Feature engineering can provide more informative inputs for machine learning models.
- Hyperparameter tuning can improve model performance.
- Comparing a baseline model with a more advanced model helps evaluate the value of additional complexity.
- Streamlit makes it possible to turn a trained model into an interactive application.

## 🔮 Future Improvements

- Experiment with additional regression algorithms.
- Apply cross-validation for more robust model evaluation.
- Improve feature selection and engineering.
- Compare model performance using additional evaluation metrics.
- Explore alternative deployment options.

---


