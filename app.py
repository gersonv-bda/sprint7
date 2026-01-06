import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Visualizador de Diagramas de Vehículos')

# crear una casilla de verificación
hist_check = st.checkbox('Mostrar histograma')
# crear otra casilla de verificación
scatter_check = st.checkbox('Mostrar diagrama de dispersión')

if hist_check:  # al marcar la casilla de verificación
    # escribir un mensaje
    st.write(
        'Creando histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_check:  # al marcar la otra casilla de verificación
    # escribir un mensaje
    st.write('Creando diagrama de dispersión (odometer vs price)')
    # crear un diagrama de dispersión
    fig2 = px.scatter(car_data, x='odometer', y='price')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
