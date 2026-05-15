import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

st.write(
    "Enter house information to predict the price."
)

income = st.number_input("Median Income")

longitude = st.number_input("Longitude")

latitude = st.number_input("Latitude")

housing_median_age = st.number_input("Housing Median Age")

total_rooms = st.number_input("Total Rooms")

total_bedrooms = st.number_input("Total Bedrooms")

population = st.number_input("Population")

households = st.number_input("Households")

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "NEAR BAY", "NEAR OCEAN", "<1H OCEAN", "ISLAND"]
)
input_data = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [income]
})

input_data["room_per_household"] = (
    input_data["total_rooms"] / input_data["households"]
)

input_data["bedrooms_per_room"] = (
    input_data["total_bedrooms"] / input_data["total_rooms"]
)

input_data["population_per_house"] = (
    input_data["population"] / input_data["households"]
)

input_data["ocean_proximity_INLAND"] = (
    1 if ocean_proximity == "INLAND" else 0
)

input_data["ocean_proximity_ISLAND"] = (
    1 if ocean_proximity == "ISLAND" else 0
)

input_data["ocean_proximity_NEAR BAY"] = (
    1 if ocean_proximity == "NEAR BAY" else 0
)

input_data["ocean_proximity_NEAR OCEAN"] = (
    1 if ocean_proximity == "NEAR OCEAN" else 0
)
input_data = input_data[
    [
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
        "ocean_proximity_INLAND",
        "ocean_proximity_ISLAND",
        "ocean_proximity_NEAR BAY",
        "ocean_proximity_NEAR OCEAN",
        "room_per_household",
        "bedrooms_per_room",
        "population_per_house"
    ]
]
if st.button("Predict Price"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )

