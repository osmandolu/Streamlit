import streamlit as st
from PIL import Image
import plotly.express as px
import plotly as pl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (10,6)
pd.set_option('display.max_columns', 100)


st.title("Exploratory Data Analysis")


"**Descriptive Statistics**"

df = pd.read_csv("./final_scout_not_dummy.csv")
df = df[["make_model", "hp_kW", "km","age", "price", "Gearing_Type", "Gears"]]

st.table(df.describe())


"**Mean Scores of Car Features by Age**"
st.table(df.groupby("age").mean())



fig = px.scatter(df,
                x="hp_kW",
                y='price',
                hover_name='make_model',
                title=f'Car Price by {"hp_kW"}')

st.plotly_chart(fig)
