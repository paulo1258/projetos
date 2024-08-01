#%%
import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)
caminho = r"C:\Users\paulo\OneDrive\Área de Trabalho\Python\Projetos\Streamlit\01_Spotify.csv"

@st.cache_data  # Usando o Cache
def load_data():
    df = pd.read_csv(caminho)
    time.sleep(5)  # Simula tempo de carregamento
    return df

# Carregamento dos dados
df = load_data()

df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists) # SIDEBAR
df_filtered = df[df["Artist"] == artist]

albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

df_filtered2 = df[df["Album"] == album]

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

st.write(artist)
st.sidebar.button("test")

