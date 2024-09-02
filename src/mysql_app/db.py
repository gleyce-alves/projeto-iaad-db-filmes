import mysql.connector
import streamlit as st

def connect_db():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="programacao_filmes"
    )

    cursor = database.cursor()

    st.session_state.setdefault("cursor", cursor);
    st.session_state.setdefault("database", database);

    print("Conexão estabelecida")