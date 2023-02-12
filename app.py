import streamlit as st
import pandas as pd
import numpy as np
import joblib
from templates import home_page, geek_page, pred_direct, pred_real_time, pred_no_kit, stats_price

st.title("AgroFirst: Crop Prediction Portal")

best_model = joblib.load("./model/best_model.joblib")


options = ['What you wanna grow?', 'Crops Stats (statewise)', 'Crop Prediction - Direct', 'Crop Prediction - Real-time', 'Crop Prediction - Real-time (no kit required)', 'Technical Jargon']
selected_option = st.selectbox("Choose an option", options)

if selected_option == 'What you wanna grow?':
    home_page()

elif selected_option == 'Crops Stats (statewise)':
    stats_price()

elif selected_option == 'Crop Prediction - Direct':
    pred_direct(best_model)

elif selected_option == 'Crop Prediction - Real-time':
    pred_real_time(best_model)

elif selected_option == 'Crop Prediction - Real-time (no kit required)':
    pred_no_kit(best_model)

elif selected_option == 'Technical Jargon':
    geek_page()