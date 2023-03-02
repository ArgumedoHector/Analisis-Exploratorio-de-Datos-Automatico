# %%
import streamlit as st
import plotly.express as px
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.image("https://abdatum.com/media/images/analisis-exploratorio-datos-cover.png")
    st.title("EDA-APP")
    choice = st.radio("Panel",["Subir","EDA"])
    st.info("Esta app te ayuda realizando un Analisis Exploratorio de Datos")

if choice == "Subir":
    st.title("Sube tu Dataset")
    file = st.file_uploader("")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "EDA": 
    st.title("Analisis Exploratorio de Datos")
    profile_df = df.profile_report()
    st_profile_report(profile_df)



