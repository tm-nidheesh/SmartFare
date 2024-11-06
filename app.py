import streamlit as st
import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("SmartFare - Ride Fare Prediction")

# Create input fields
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=10)

weekday = st.selectbox('Weekday', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

monthly_quarter = st.selectbox('Monthly Quarter', ['Q1', 'Q2', 'Q3', 'Q4'])

hourly_segments = st.selectbox('Hourly Segments', ['H1', 'H2', 'H3', 'H4', 'H5', 'H6'])

distance = st.number_input('Distance (in km)', min_value=0.0)

# Predict button
if st.button('Predict Fare'):
    prediction = model.predict([[passenger_count, weekday, monthly_quarter, hourly_segments, distance]])
    st.write(f"Predicted Fare: ${prediction[0]:.2f}")
