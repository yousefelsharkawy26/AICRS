import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Smart Crop Recommendation 🌾", layout="centered")

st.title("🌾 Smart crop recommendation using Machine Learning")
st.write("Enter the environment characteristics and the model will suggest the best crop to grow: ")

# The input from the user
N = st.number_input("Nitrogen percentage (N)", 0, 200, 50)
P = st.number_input("Phosphorus ratio (P)", 0, 200, 50)
K = st.number_input("Potassium percentage (K)", 0, 200, 50)
temperature = st.number_input("temperature (°C)", 0.0, 60.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
ph = st.number_input("soil pH (pH)", 0.0, 14.0, 6.5)
rainfall = st.number_input("amount of rain (mm)", 0.0, 500.0, 100.0)

if st.button("🔍 Predict the right crop"):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"🌱 Current conditions are suitable for rice **{prediction}** cultivation. ✅")

st.markdown("---")
st.caption("Developed using Python + Streamlit + Machine Learning")
