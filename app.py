import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('employee_attrition_model.pkl')

# Function to make predictions
def predict_attrition(input_data):
    prediction = model.predict(input_data)
    return prediction

# Streamlit app
st.title("Employee Attrition Prediction")

# Input form
st.sidebar.header("Employee Features")
features = {}
for feature in X.columns:
    features[feature] = st.sidebar.number_input(feature, value=0.0)

# Convert input features to DataFrame
input_data = pd.DataFrame([features])

# Predict and display the result
if st.button("Predict"):
    prediction = predict_attrition(input_data)
    if prediction[0] == 1:
        st.write("The employee is likely to leave the company.")
    else:
        st.write("The employee is likely to stay with the company.")
