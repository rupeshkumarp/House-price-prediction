import streamlit as st
import pickle
import numpy as np
import pandas as pd
import logging
from datetime import datetime
import os

# Set up logging
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, f"predictions_{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# CSV file for storing predictions
predictions_csv = "predictions_data.csv"

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    logging.info("Model loaded successfully")

# Set page config
st.set_page_config(page_title="House Price Prediction", layout="wide")

# Title
st.title("🏠 House Price Prediction")
st.write("Predict house prices based on property features")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Property Features")
    
    bedrooms = st.slider("Bedrooms", min_value=0, max_value=8, value=3, step=1)
    bathrooms = st.slider("Bathrooms", min_value=0, max_value=8, value=2, step=1)
    floors = st.slider("Floors", min_value=1, max_value=3, value=2, step=1)
    waterfront = st.selectbox("Waterfront", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    st.subheader("Additional Details")
    
    yr_built = st.slider("Year Built", min_value=1900, max_value=2024, value=2000, step=1)
    
    # Renovation status
    has_renovation = st.checkbox("Has been renovated?", value=False)
    if has_renovation:
        yr_renovated = st.slider("Year Renovated", min_value=1912, max_value=2014, value=2010, step=1)
    else:
        yr_renovated = 0
        st.info("Property has not been renovated (yr_renovated = 0)")
    
    city_e = st.slider("City Code", min_value=0, max_value=43, value=25, step=1)

# Prediction button
if st.button("Predict Price", use_container_width=True):
    # Prepare input data
    input_data = np.array([[bedrooms, bathrooms, floors, waterfront, yr_built, yr_renovated, city_e]])
    
    # Make prediction
    predicted_price = model.predict(input_data)[0]
    
    # Log the prediction
    logging.info(f"Prediction made - Bedrooms: {bedrooms}, Bathrooms: {bathrooms}, Floors: {floors}, Waterfront: {waterfront}, Year Built: {yr_built}, Year Renovated: {yr_renovated}, City Code: {city_e}, Predicted Price: ${predicted_price:,.2f}")
    
    # Save to CSV
    prediction_record = {
        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'Floors': floors,
        'Waterfront': waterfront,
        'Year_Built': yr_built,
        'Year_Renovated': yr_renovated,
        'City_Code': city_e,
        'Predicted_Price': predicted_price
    }
    
    # Check if CSV exists, if not create it with headers
    if os.path.exists(predictions_csv):
        df_existing = pd.read_csv(predictions_csv)
        df_new = pd.DataFrame([prediction_record])
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(predictions_csv, index=False)
    else:
        df_new = pd.DataFrame([prediction_record])
        df_new.to_csv(predictions_csv, index=False)
    
    logging.info(f"Prediction data saved to {predictions_csv}")
    
    # Display result
    st.success("✅ Prediction Complete!")
    st.metric("Predicted Price", f"${predicted_price:,.2f}")
    
    # Display input summary
    with st.expander("Input Summary"):
        summary_df = pd.DataFrame({
            'Feature': ['Bedrooms', 'Bathrooms', 'Floors', 'Waterfront', 'Year Built', 'Year Renovated', 'City Code'],
            'Value': [bedrooms, bathrooms, floors, waterfront, yr_built, yr_renovated, city_e]
        })
        st.table(summary_df)

# Footer with log info
st.divider()
st.caption(f"Logs are saved to: `{log_file}`")
st.caption(f"Predictions data saved to: `{predictions_csv}`")
