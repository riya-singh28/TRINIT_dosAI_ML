import streamlit as st
import pandas as pd
import numpy as np
from utils import list_of_states

price = pd.read_csv("data/price.csv")
# price = price.astype({'modal_price':'float32'}).dtypes

def stats_price():
    crops = pd.DataFrame({"Crops we support": ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']})
    
    st.table(crops)
    # Form inputs
    state = st.selectbox("Choose the state", list_of_states(price))

    # Output window
    if st.button("Submit"):
        
        price['modal_price'] = price['modal_price'].apply(np.ceil)
        p = price.groupby(['state'])['label','modal_price']
        pf = p.get_group(state)
        vis = pf.sort_values(by='modal_price', ascending=False)
        
        st.bar_chart(vis, x="label", y="modal_price")
        st.success("Ranking of crops by sales price")