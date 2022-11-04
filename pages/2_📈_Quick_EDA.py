pip install streamlit-pandas-profiling


import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report


df = pd.read_csv("https://github.com/osmandolu/Streamlit/blob/main/final_scout_not_dummy.csv")

pr = df.profile_report()

st_profile_report(pr)
