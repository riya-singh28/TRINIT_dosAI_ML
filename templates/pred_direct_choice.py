from pytest import param
import streamlit as st
import numpy as np
import pandas as pd

def pred_direct(best_model):
    # Form inputs
    temp = st.number_input("Temperature", step=0.01)
    rain = st.number_input("Rainfall", step=0.01)
    humid = st.number_input("Humidity", step=0.01)
    ph = st.number_input("pH value of soil", step=0.01, max_value=14.0, min_value=0.0)
    N = st.number_input("Nitrogen ratio in soil", step=0.01)
    P = st.number_input("Phosphorus ratio in soil", step=0.01)
    K = st.number_input("Potassium ratio in soil", step=0.01)

    # Output window
    if st.button("Submit"):
        data = np.array([[N, P, K, temp, humid, ph, rain]])

        param = pd.DataFrame({"Parameters": ["N value", "P value", "K value", "temperature", "humidity", "pH", "rain"], "Values": [N, P, K, temp, humid, ph, rain]})

        st.table(param)
        prediction = best_model.predict(data)
        result = f"Best crop for you: {prediction[0]}"
        st.success(result)