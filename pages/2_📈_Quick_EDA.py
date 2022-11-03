import numpy as np
import pandas as pd
import streamlit as st

from streamlit_pandas_profiling import st_profile_report


df = pd.read_csv("https://github.com/osmandolu/Streamlit/blob/main/final_scout_not_dummy.csv")
pr = ProfileReport(df, explorative=True)
st_profile_report(pr)
