# Data visualization
import pandas as pd
import numpy as np
import streamlit as st

# Create a bar chart
st.title("Bar Chart")
#data = pd.DataFrame(np.random.rand(50, 2), columns=["x", "y"])

#Abrir csv
data= pd.read_csv("madrid_data_airbnb_2023.csv")
st.bar_chart(data)

# Line chart
st.title("Line Chart")
st.line_chart(data)

# Area chart
st.title("Area Chart")
st.area_chart(data)