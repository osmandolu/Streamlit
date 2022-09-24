import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://file.kelleybluebookimages.com/kbb/base/evox/CP/15180/2023-Chevrolet-Corvette-front_15180_032_1838x654_GA7_cropped.png");
background-size: 30%;
background-position: center right;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stSidebar"] > div:first-child {{
# background-image: url("https://i.pinimg.com/originals/04/a2/ea/04a2ea25b1868a0ac1fd61241fdd9946.jpg");
background-position: top left; 
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

html_temp = """
    <div style="background-color:#6b5b95;padding:12px">
    <h2 style="color:white;text-align:center;"> Car Price Prediction </h2>
    </div>
    """
# st.title("FREE CAR VALUATION")
st.markdown(html_temp,unsafe_allow_html=True)

st.text("")
st.text("")


df = pd.read_csv("./final_scout_not_dummy.csv")
df = df[["make_model", "hp_kW", "km","age", "price", "Gearing_Type", "Gears"]]



data_container = st.container()

with data_container:
    a,b = st.columns(2)
    with a:
        car_model=st.selectbox("Car Model", df["make_model"].unique())
        age=st.selectbox("Age", sorted(df["age"].astype(int).unique()))
    with b:
        gearing_type=st.selectbox("Gearing Type", df["Gearing_Type"].unique())
        gears=st.selectbox("Gears", sorted(df["Gears"].astype(int).unique()))






#slider
hp = st.slider("Horse Power", min_value=int(df["hp_kW"].min()), max_value=int(df["hp_kW"].max()), value=80, step=1)

km = st.slider("Mileage", min_value=int(df["km"].min()), max_value=int(df["km"].max()), value=20000, step=1)



import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

my_dict = {
    "make_model": car_model ,
    "hp_kW": hp,
    "km": km,
    "age" :age,
    "Gearing_Type":gearing_type,
    "Gears":gears
}

df=pd.DataFrame.from_dict([my_dict])
st.table(df)

if st.button("Click Here to Learn How Much Your Car is Worth!"): 
    pred = model.predict(df)
    st.write(str(int(pred[0]))+" $")


