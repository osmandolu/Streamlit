import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# Web App Title
st.markdown('''
# 🚀 Data Uploader

Here you will upload your data to the program and use the sidebar on the lefthand side to navigate.

**Connect with me:** [Osman Dolu, Ph.D.](linkedin.com/in/odolu) 

---
''')

# Upload CSV data
#importing required libraries

import streamlit as st

from io import StringIO 



#adding a file uploader

file = st.file_uploader("Please choose a file")

if file is not None:

    #To read file as bytes:

    bytes_data = file.getvalue()

    st.write(bytes_data)



    #To convert to a string based IO:

    stringio = StringIO(file.getvalue().decode("utf-8"))

    st.write(stringio)



    #To read file as string:

    string_data = stringio.read()

    st.write(string_data)



    #Can be used wherever a "file-like" object is accepted:

    df= pd.read_csv(file)

    st.write(df)



#adding a file uploader to accept multiple CSV files

uploaded_files = st.file_uploader("Please choose a CSV file", accept_multiple_files=True)

for file in uploaded_files:

    bytes_data = file.read()

    st.write("File uploaded:", file.name)

    st.write(bytes_data)
