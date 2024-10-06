import streamlit as st
import pandas as pd

upload_file = st.file_uploader("Please Upload Your File Here!")
if upload_file:
    df = pd.read_csv(upload_file)
    st.session_state['df'] = df
