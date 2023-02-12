import streamlit as st
import pandas as pd
import numpy as np
from utils import list_of_states, list_of_dist, temp_humid, get_rain, get_composition

rainy_npk = pd.read_csv("data/rain_merge_npk.csv")

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    'Nov', 'Dec'
]


def pred_no_kit(best_model):
    # Form inputs
    state = st.selectbox("Choose the state", list_of_states(rainy_npk))
    dist = st.selectbox("Choose the district", list_of_dist(rainy_npk, state))
    month = st.selectbox("Choose the month", months)
    ph = st.number_input("pH value of soil",
                         step=0.01,
                         max_value=14.0,
                         min_value=0.0)

    N, P, K = get_composition(rainy_npk, dist, state)              
    

    # Output window
    if st.button("Submit"):
        temp, humid = temp_humid(dist, state)
        rain = get_rain(rainy_npk, dist, state, month)
        data = np.array([[N, P, K, temp, humid, ph, rain]])

        param = pd.DataFrame({"Parameters": ["N value", "P value", "K value", "temperature", "humidity", "pH", "rain"], "Values": [N, P, K, temp, humid, ph, rain]})

        st.table(param)

        prediction = best_model.predict(data)
        result = f"Best crop for you: {prediction[0]}"
        st.success(result)