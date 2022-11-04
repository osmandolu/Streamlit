import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="No-Code Machine Learning",
    page_icon=":car:",
)


st.title("Welcome to No-Code Machine Learning with Streamlit!")


"Hello visitor!" 
"Welcome to my No-Code Machine Learning page!" 
"My name is Osman Dolu. I am a data scientist with 10+ years of experience in this field."
"With this web app, you will see a brief presentation of car price prediction using AutoScout data scraped from the Europe's famous car sale website. Instead of writing so many lines of code, you can simply change the parameters and see how the price of the car changes. Beware that the data I have used might not be up-to-date when you visit this page."
"I have used Streamlit and Python's Numpy and Pandas libraries and major machine learning algorithms to realize this project. It's just a sample and in this respect, it should be noted as a showcase example for what can be done using Streamlit's powerful environment."
"I hope you will like it."

"Best regards,"

"Osman Dolu, Ph.D."




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



def navbar_component():
    with open("assets/images/settings.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    settings_items = ''
    for key, value in SETTINGS.items():
        settings_items += (
            f'<a href="/?nav={value}" class="settingsNav">{key}</a>')

    component = rf'''
            ....
    '''
    st.markdown(component, unsafe_allow_html=True)
    
    js = '''
    <script>
    ....
    </script>
    '''
    html(js)
