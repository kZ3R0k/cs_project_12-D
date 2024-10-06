import streamlit as st
import plotly.express as px

df = st.session_state['df']
x_values = st.selectbox('X-Axis', options=df.columns)
y_values = st.selectbox("Y-Axis", options=df.columns)
col = st.color_picker('Pick Your Colour')
line_plot = px.line(df, x=x_values, y=y_values, line_shape='linear')
average_y = df[y_values].mean()
line_plot.add_hline(y=average_y, line_dash="dash", line_color="red", annotation_text="Average", annotation_position="top right")
line_plot.update_traces(line=dict(color=col))
st.plotly_chart(line_plot)