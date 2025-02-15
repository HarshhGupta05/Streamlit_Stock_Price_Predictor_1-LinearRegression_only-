import numpy as np
import pickle
import streamlit as st

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("📈 Stock Price Predictor")
st.markdown("Enter stock details to predict the **Closing Price**.")

# User input fields
open_price = st.number_input("Enter Open Price", min_value=0.0, format="%.2f")
high_price = st.number_input("Enter High Price", min_value=0.0, format="%.2f")
low_price = st.number_input("Enter Low Price", min_value=0.0, format="%.2f")
volume = st.number_input("Enter Volume", min_value=0, format="%.0f")

# Predict button
if st.button("Predict Closing Price"):
    input_data = np.array([[open_price, high_price, low_price, volume]])
    prediction = model.predict(input_data)[0]
    st.success(f"📉 Predicted Closing Price: **${round(prediction, 2)}**")
