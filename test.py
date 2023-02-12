import streamlit as st
import pandas as pd

st.title("Simple Form with Dropdown Menu and Data Visualization")

options = ['option 1', 'option 2', 'option 3']
selected_option = st.selectbox("Choose an option", options)

# Create a sample dataframe
data = {'Option': options, 'Value': [10, 20, 30]}
df = pd.DataFrame(data)

# Plot the bar chart
st.bar_chart(df)

# Form inputs
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")

# Output window
if st.button("Submit"):
    result = f"Name: {name}, Age: {age}"
    st.success(result)