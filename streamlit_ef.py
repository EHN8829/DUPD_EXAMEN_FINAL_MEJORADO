
import streamlit as st
from googleapiclient.discovery import build
import pandas as pd

# Título de la aplicación
st.title('Análisis de Sentimientos en YouTube')

# Entrada para la clave de API de YouTube
api_key = st.text_input('Introduce tu clave de API de YouTube')

if api_key:
    # Construyendo el cliente de la API de YouTube
    youtube = build("youtube", "v3", developerKey=api_key)

    # Solicitar ID de lista de reproducción
    playlist_id = 'PLeySRPnY35dFSDPi_4Q5R1VCGL_pab26A'

    # Solicitar los videos de la lista de reproducción
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=30
    )

    response = request.execute()

    # Mostrar los títulos y los ID de los videos
    for item in response.get('items', []):
        st.write(f'Título: {item["snippet"]["title"]}, Video ID: {item["snippet"]["resourceId"]["videoId"]}')
