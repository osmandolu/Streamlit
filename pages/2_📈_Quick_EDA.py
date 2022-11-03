import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


df = st.session_state['df']
pr = ProfileReport(df, explorative=True)
# st.header('DataFrame Header')
# st.write(df)
# st.write('---')
# st.header('Pandas Profiling Report')
st_profile_report(pr)