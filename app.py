import streamlit as st
import pandas as pd
import numpy as np
import joblib
from templates import pred_direct, pred_real_time, pred_no_kit

st.title("Crop Prediction")

best_model = joblib.load("./model/best_model.joblib")


options = ['Crop Prediction - Direct', 'Crop Prediction - Real-time', 'Crop Prediction - Real-time (no kit required)']
selected_option = st.selectbox("Choose an option", options)

if selected_option == 'Crop Prediction - Direct':
    pred_direct(best_model)

elif selected_option == 'Crop Prediction - Real-time':
    pred_real_time(best_model)

elif selected_option == 'Crop Prediction - Real-time (no kit required)':
    pred_no_kit(best_model)