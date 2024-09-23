import mysql.connector
import streamlit as st

def connect_db():
    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="140178",
            database="programacao_filmes"
        )

        if database.is_connected():
            cursor = database.cursor()
            st.session_state["cursor"] = cursor
            st.session_state["database"] = database
            print("Conexão estabelecida")
        else:
            st.error("Conexão ao banco de dados falhou.")
    except mysql.connector.Error as err:
        st.error(f"Erro ao conectar ao banco de dados: {err}")
