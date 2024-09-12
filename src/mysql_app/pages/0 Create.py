import streamlit as st
from datetime import datetime

cursor = st.session_state.get("cursor")
database = st.session_state.get("database")

st.title("Create")
st.write("Utilize as tabs de navegação para inserir itens nas tabelas de filme, canal e exibição.")

tab1, tab2, tab3 = st.tabs(["Filme", "Canal", "Exibição"])

with tab1:

    categorias = ["Ação", "Comédia", "Drama", "Ficção científica", "Terror", "Romance", "Animação", "Aventura", "Suspense", "Fantasia"]

    sql = "INSERT INTO filme (num_filme, titulo_original, titulo_brasil, ano_lancamento, pais_origem, categoria, duracao) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    col1, col2 = st.columns(2)

    with col1:
        id = st.number_input(label="Identificador", step=1, key="id", value=None)
        titulo = st.text_input("Título original")
        duracao = st.number_input(label="Duração (em minutos)", step=1, min_value=1)

    pais_origem = st.text_input("Pais de origem")

    with col2:
        ano_lancamento = st.number_input("Ano lançamento", step=1, value=None, min_value=1900, max_value=2025)
        titulo_brasil = st.text_input("Título Brasil")
        categoria = st.selectbox("Categoria", categorias)

    submitted = st.button("Adicionar filme", key="filme")

    with st.expander("Ver SQL utilizado"):
        st.write(sql)

    if submitted:

        values = (id, titulo, titulo_brasil, ano_lancamento, pais_origem, categoria, duracao)

        if any(item is None or item == '' or item == 0 for item in values):
            st.warning('Preencha todos os campos.', icon="⚠️")
        else :
            st.spinner("Enviando dados...")

            cursor.execute(sql, values)

            database.commit()

            st.success('Filme inserido com sucesso!', icon="✅")



with tab2:

    sql = "INSERT INTO canal (num_canal, nome, sigla) VALUES (%s, %s, %s)"

    col1, col2 = st.columns(2)

    with col1:
        num_canal = st.number_input(label="Número do canal", step=1, value=None)

    nome_canal = st.text_input("Nome do canal")

    with col2:
        sigla = st.text_input("Sigla do canal") 

    submitted = st.button("Adicionar canal", key="canal")

    with st.expander("Ver SQL utilizado"):
        st.write(sql)

    if submitted:

        values = (num_canal, nome_canal, sigla)

        if any(item is None or item == '' or item == 0 for item in values):
            st.warning('Preencha todos os campos.', icon="⚠️")
        else :
            st.spinner("Enviando dados...")

            cursor.execute(sql, values)

            database.commit()

            st.success('Canal inserido com sucesso!', icon="✅")



with tab3:

    sql = "INSERT INTO exibicao (num_filme, num_canal, data) VALUES (%s, %s, %s)"

    left, middle1, middle2, right = st.columns(4, vertical_alignment="bottom")

    num_filme = left.number_input(label="Número do filme", step=1, value=None, key="num_filme")
    num_canal = middle1.number_input(label="Número do canal", step=1, value=None, key="num_canal")
    data = middle2.date_input("Data", format="DD/MM/YYYY")
    hora = right.time_input("hora")

    submitted = st.button("Adicionar exibicao", key="exibicao")

    with st.expander("Ver SQL utilizado"):
        st.write(sql)

    if submitted:

        data_hora = datetime.combine(data, hora)

        values = (num_filme, num_canal, data_hora)

        if any(item is None or item == '' or item == 0 for item in values):
            st.warning('Preencha todos os campos.', icon="⚠️")
        else :
            st.spinner("Enviando dados...")

            cursor.execute(sql, values)

            database.commit()

            st.success('Exibição inserida com sucesso!', icon="✅")