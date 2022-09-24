import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Car Price Prediction App",
    page_icon=":car:",
)


st.title("AutoScout Car Price Prediction Project")
st.sidebar.success("Please select a page to navigate")


"Hello visitor!" 

"My name is Osman and I am a data scientist. In this project, you willsee a brief presentation of exploratory data analysis and car price prediction using AutoScout data. I have used Streamlit and Python to realize this project."

"I hope you will like it. You can navigate the analysis pages using the sidebar on the left hand side."

"**Osman Dolu, Ph.D.**"



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://miro.medium.com/max/540/1*J_EXEmUkOcg-rgzJudUhZQ.png");
background-size: 30%;
background-position: bottom right;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

