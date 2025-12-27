import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

conn = sqlite3.connect('iot.db')
data = pd.read_sql_query("SELECT * FROM sensor_data", conn)
conn.close()

st.title("IoT Sensor Dashboard")

fig_temp = px.line(data, x='timestamp', y='temperature', title='Temperature Over Time')
st.plotly_chart(fig_temp)

fig_hum = px.line(data, x='timestamp', y='humidity', title='Humidity Over Time')
st.plotly_chart(fig_hum)

st.subheader("Raw Data")
st.dataframe(data)