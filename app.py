import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 SF Housing Price Trends")

# Load data
df = pd.read_csv("data/sf_housing_sample.csv")

# Show data table
st.subheader("Raw Data")
st.write(df)

# Add dropdown and chart
st.subheader("Price Trend by Neighborhood")

neighborhood = st.selectbox("Select a neighborhood:", df['Neighborhood'].unique())

filtered = df[df['Neighborhood'] == neighborhood]

fig = px.line(filtered, x='Year', y='Price', title=f"{neighborhood} Housing Prices Over Time")
st.plotly_chart(fig)


