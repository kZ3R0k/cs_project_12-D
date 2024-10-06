import streamlit as st

df = st.session_state['df']
st.write(df.describe())