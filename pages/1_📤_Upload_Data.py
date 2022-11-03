import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# Web App Title
st.markdown('''
# 🚀 Data Uploader

Here you will upload your data to the program and use the sidebar on the lefthand side to navigate. This app is created in Streamlit using various libraries such as **pandas-profiling** for quick EDA and **PyCarret** for ML automation.

**Connect with me:** [Osman Dolu, Ph.D.](linkedin.com/in/odolu) 

---
''')

# Upload CSV data
with st.header('1. Upload your CSV data'):
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
#     st.sidebar.markdown("""
# [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
# """)

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    st.session_state['df'] = df
    pr = ProfileReport(df, explorative=True)
    if "df" not in st.session_state: # we are transferring dataframe to other pages with this.
        st.session_state['df'] = df   # we are transferring dataframe to other pages with this.

    # st.subheader('Dataframe:')
    n, m = df.shape
    st.write(f'<p style="font-size:100%">DataFrame contains {n} rows and {m} columns.</p>', unsafe_allow_html=True)   

    if 'number_of_rows' not in st.session_state:
        st.session_state["number_of_rows"] = 5
        st.session_state['type'] = 'Categorical'

    data_container = st.container()

    with data_container:
        a,b = st.columns(2)
        with a:
            increment = st.button("Show more columns ⬆️")
            if increment:
                st.session_state.number_of_rows +=1
        with b:
            decrement = st.button("Show fewer columns ⬇️")
            if decrement:
                st.session_state.number_of_rows -=1

    st.table(df.head(st.session_state["number_of_rows"]))

    st.write(f'<p style="font-size:100%">You have successully uploaded your data. Now, you can continue with data cleaning stage.</p>', unsafe_allow_html=True)

    # st.write('**DataFrame Head**')
    # st.write(df)
    # st.write('---')
    # st.header('**Pandas Profiling Report**')
    # st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_csv():
            csv = pd.read_csv("final_scout_not_dummy.csv")
            return csv
        df = load_csv()
        st.session_state['df'] = df
        pr = ProfileReport(df, explorative=True)

        if "df" not in st.session_state: # we are transferring dataframe to other pages with this.
            st.session_state['df'] = df   # we are transferring dataframe to other pages with this.

            # st.subheader('Dataframe:')
            n, m = df.shape
            st.write(f'<p style="font-size:130%">DataFrame contains {n} rows and {m} columns.</p>', unsafe_allow_html=True)   

        st.header('**DataFrame Head**')
        st.write(df)
        # st.write('---')
        # st.header('**Pandas Profiling Report**')
        # st_profile_report(pr)

