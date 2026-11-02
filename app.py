
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("used_car_resale_price", "rb") as file:
    model = pickle.load(file)

# Application title
st.title("Car Resale Price Prediction")
st.write("Enter the car details to predict its resale price.")

# Input fields
make = st.selectbox(
    "Car Manufacturer",
    ["Ford", "BMW", "Audi", "Toyota", "Hyundai", "Volkswagen", "Other"]
)

car_model = st.text_input("Car Model")

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2026,
    value=2018
)

mileage = st.number_input("Mileage", min_value=0, value=30000)

tax = st.number_input("Tax", min_value=0, value=150)

mpg = st.number_input("Miles Per Gallon (MPG)", min_value=0.0, value=45.0)

engine_size = st.number_input("Engine Size", min_value=0.0, value=1.5)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto", "Other"]
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

# Predict button
if st.button("Predict Resale Price"):

    # Prepare input data
    input_data = pd.DataFrame([{
        "Make": make,
        "model": car_model,
        "year": year,
        "mileage": mileage,
        "tax": tax,
        "mpg": mpg,
        "engineSize": engine_size,
        "transmission": transmission,
        "fuelType": fuel_type
    }])

    # Predict price
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted Car Resale Price: {prediction[0]:,.2f}")
