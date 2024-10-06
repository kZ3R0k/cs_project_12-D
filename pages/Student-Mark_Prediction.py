import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.markdown("""
    <style>
    
    .rainbow-button {
        background-image: linear-gradient(to right, red, orange, yellow, green, cyan, blue, violet);
        color: white;
        font-size: 16px;
        padding: 10px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        display: inline-block;
        opacity: 0;
    }

    .rainbow-button:hover {
        filter: brightness(1.2);
    }
    </style>
    """, unsafe_allow_html=True)

upload_file = st.file_uploader("Please Upload Your File Here!", type='csv')

if upload_file:
    df = pd.read_csv(upload_file)

    if 'exam_no' in df.columns and 'marks' in df.columns:
        x = df[['exam_no']]
        y = df['marks']

        model = LinearRegression()
        model.fit(x, y)

        p = df['exam_no'].max()
        next_exam = np.array([[p + 1]])
        predicted = model.predict(next_exam)

        st.markdown('<div class="rainbow-button-container">', unsafe_allow_html=True)
        if st.button('Click to Predict', key="rainbow-button", use_container_width=True):
            st.write(f"Predicted Marks for Exam No {next_exam[0][0]} is {predicted[0]:.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("The uploaded file must contain 'exam_no' and 'marks' columns.")