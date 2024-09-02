import streamlit as st
from db import connect_db

connect_db()

st.title("IAAD - operações CRUD com MySQL e Streamlit")

# para resgatar a conexão com o bacno de dados em outras páginas, utilizar:
cursor = st.session_state.get("cursor")
database = st.session_state.get("database")
