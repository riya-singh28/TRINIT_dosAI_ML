import streamlit as st
import pandas as pd
import numpy as np
import joblib
from templates import pred_direct

st.title("Crop Prediction")

best_model = joblib.load("./model/best_model.joblib")


options = ['Crop Prediction (direct)', 'Crop Prediction (real-time)', 'option 3']
selected_option = st.selectbox("Choose an option", options)

if selected_option == 'Crop Prediction (direct)':
    pred_direct(best_model)