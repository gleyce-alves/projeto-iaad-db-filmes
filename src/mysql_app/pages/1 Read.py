import streamlit as st
from datetime import datetime

cursor = st.session_state.get("cursor")
database = st.session_state.get("database")

st.title("Read")
st.write("Utilize as tabs de navegação para visualizar os itens nas tabelas de filme, canal e exibição.")

tab1, tab2, tab3 = st.tabs(["Filme", "Canal", "Exibição"])

with tab1:
    st.header("Visualizar Filmes")

    sql_filmes = "SELECT num_filme, titulo_original, titulo_brasil, ano_lancamento, pais_origem, categoria, duracao FROM filme"
    
    cursor.execute(sql_filmes)
    filmes = cursor.fetchall()

    if filmes:
        st.table(filmes)
        st.success("Filmes carregados com sucesso!", icon="✅")
    else:
        st.warning("Nenhum filme encontrado.", icon="⚠️")

with tab2:
    st.header("Visualizar Canais")

    sql_canais = "SELECT num_canal, nome, sigla FROM canal"

    cursor.execute(sql_canais)
    canais = cursor.fetchall()

    if canais:
        st.table(canais)
        st.success("Canais carregados com sucesso!", icon="✅")
    else:
        st.warning("Nenhum canal encontrado.", icon="⚠️")

with tab3:
    st.header("Visualizar Exibições")

    sql_exibicoes = """
    SELECT e.num_filme, f.titulo_brasil, e.num_canal, c.nome, e.data
    FROM exibicao e
    JOIN filme f ON e.num_filme = f.num_filme
    JOIN canal c ON e.num_canal = c.num_canal
    """

    cursor.execute(sql_exibicoes)
    exibicoes = cursor.fetchall()

    if exibicoes:
        st.table(exibicoes)
        st.success("Exibições carregadas com sucesso!", icon="✅")
    else:
        st.warning("Nenhuma exibição encontrada.", icon="⚠️")
