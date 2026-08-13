import streamlit as st
import pickle
import pandas as pd

# Load the trained model and feature names
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]


# Streamlit app
st.title("🌧️ Rainfall Prediction")

st.write("Enter the weather details below to predict whether rainfall is expected.")


# Input fields
pressure = st.number_input(
    "Pressure",
    min_value=900.0,
    max_value=1100.0,
    value=1015.9
)

dewpoint = st.number_input(
    "Dewpoint",
    min_value=-10.0,
    max_value=50.0,
    value=19.9
)

humidity = st.number_input(
    "Humidity",
    min_value=0.0,
    max_value=100.0,
    value=95.0
)

cloud = st.number_input(
    "Cloud",
    min_value=0.0,
    max_value=100.0,
    value=81.0
)

sunshine = st.number_input(
    "Sunshine",
    min_value=0.0,
    max_value=24.0,
    value=0.0
)

winddirection = st.number_input(
    "Wind Direction",
    min_value=0.0,
    max_value=360.0,
    value=40.0
)

windspeed = st.number_input(
    "Wind Speed",
    min_value=0.0,
    max_value=150.0,
    value=13.7
)


# Prediction
if st.button("Predict Rainfall"):

    input_data = (
        pressure,
        dewpoint,
        humidity,
        cloud,
        sunshine,
        winddirection,
        windspeed
    )

    input_df = pd.DataFrame(
        [input_data],
        columns=feature_names
    )

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("🌧️ Rainfall is predicted.")
    else:
        st.info("☀️ No Rainfall is predicted.")