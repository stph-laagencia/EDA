# Data visualization
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

## Posibles tipos de texto:
## st.title() # corresponds to H1 heading
## st.header() # corresponds to H2 heading
## st.subheader() # corresponds to H3 heading
## st.st.subheader()text() v corresponds to text


##### --------- AQUÍ COMIENZA NUESTRA APLICACIÓN DE STREAMLIT---------##########
# 1. Leemos los datos de AirBnB
## Utilizar el path completo de la ubicación del dataset
data = pd.read_csv("C:/Users/laage/techW/EDA/madrid_airbnb_data_2023.csv")

# 2. Título General para la aplicación
st.title("Precios promedios de AirBnB en barrios de Madrid durante el año 2023")

# 3. Barplot de Precios promedios por barrio por tipo de habitación.
### Agrupamos el dataset por 'room_type','neighbourhood'
### Agrpuacion con el metodo groupby
df_neigborhood = data.groupby(['neighbourhood', 'room_type']).price.mean().reset_index() #dataset agrupado

#Barplot Precios medios por barrio por tipo de habitación.
st.subheader("Precios promedios de AirBnB en barrios de Madrid durante el año 2023")
fig_bar = px.bar(df_neigborhood, x='neighbourhood', y='price', color='room_type', hover_name='room_type')
st.plotly_chart(fig_bar)

# 4. Countplot: Conteo inmuebles por barrio por tipo de habitación.
st.subheader("Conteo inmuebles por barrio por tipo de habitación en Madrid durante el año 2023")
fig_count_plot = px.histogram(data, x='neighbourhood', color='room_type', hover_name='room_type' )
st.plotly_chart(fig_count_plot)

