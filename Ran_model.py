import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('ctr_model.sav', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Ad Click Prediction App')

# Input fields
daily_time_spent = st.number_input('Daily Time Spent on Site (in minutes)', min_value=0, max_value=100, step=1)
age = st.number_input('Age', min_value=18, max_value=70, step=1)
area_income = st.number_input('Area Income', min_value=0, max_value=100000, step=500)
daily_internet_usage = st.number_input('Daily Internet Usage (in minutes)', min_value=0, max_value=300, step=1)
gender = st.selectbox('Gender', ['Male', 'Female'])

# Convert gender input to numerical format
gender = 1 if gender == 'Male' else 0

# Optional inputs for extra features
hour = st.slider('Hour of Visit', 0, 23, 12)
day = st.slider('Day of the Month', 1, 31, 15)
month = st.slider('Month', 1, 12, 6)

# When the user clicks the 'Predict' button
if st.button('Predict'):
    # Prepare the input features as a 2D array
    input_features = np.array([[daily_time_spent, age, area_income, daily_internet_usage, gender, hour, day, month]])

    # Make a prediction
    prediction = model.predict(input_features)

    # Display the result
    if prediction[0] == 1:
        st.write('The user is likely to click the ad.')
    else:
        st.write('The user is unlikely to click the ad.')