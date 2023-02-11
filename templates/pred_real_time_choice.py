from math import dist
import streamlit as st
import pandas as pd
import numpy as np
from utils import list_of_states, list_of_dist, temp_humid, get_rain

rainy = pd.read_csv("data/monthly_rainfall.csv")

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    'Nov', 'Dec'
]


def pred_real_time(best_model):
    # Form inputs
    state = st.selectbox("Choose the state", list_of_states(rainy))
    dist = st.selectbox("Choose the district", list_of_dist(rainy, state))
    month = st.selectbox("Choose the month", months)
    ph = st.number_input("pH value of soil",
                         step=0.01,
                         max_value=14.0,
                         min_value=0.0)
    N = st.number_input("Nitrogen ratio in soil", step=0.01)
    P = st.number_input("Phosphorus ratio in soil", step=0.01)
    K = st.number_input("Potassium ratio in soil", step=0.01)

    # Output window
    if st.button("Submit"):
        temp, humid = temp_humid(dist, state)
        rain = get_rain(rainy, dist, state, month)
        data = np.array([[N, P, K, temp, humid, ph, rain]])
        prediction = best_model.predict(data)
        result = f"Best crop for you: {prediction[0]}"
        st.success(result)
