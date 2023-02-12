import streamlit as st
from PIL import Image

def home_page():
    image = Image.open('data/crops.jpg')
    st.image(image)
    st.header("About Us")
    st.write("Welcome to our crop prediction portal! We are dedicated to helping farmers and agriculture business owners make informed decisions about what crops to grow in their specific locations. Our innovative approach takes into account crucial factors such as soil composition, rainfall patterns, temperature fluctuations, and return on investment to provide farmers with the optimal crop choices. Gone are the days of trial-and-error farming practices, where farmers spent large amounts of money on fertilizers and other resources only to have limited success. Our cutting-edge technology offers farmers a personalized and data-driven solution, allowing them to make informed decisions and achieve maximum profits. We understand the importance of sustainable farming practices, and that's why our predictions also take into account the impact on the soil and its natural resources. By avoiding the repetition of growing the same crops in the same areas, farmers can maintain healthy soil and preserve it for future generations. At our crop prediction company, we believe that the future of agriculture lies in the intersection of technology and sustainability. Join us as we revolutionize the farming industry and lead the way towards a brighter, more profitable, and sustainable future.")
    st.subheader("Authors")
    st.write("Riya Singh, EC Engg, National Institute of Technology Karnataka, India")
    st.write("Aryan Amit Barsainyan, Mechanical Engg, National Institute of Technology Karnataka, India")