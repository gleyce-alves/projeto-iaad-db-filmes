import streamlit as st

cursor = st.session_state.get("cursor")
database = st.session_state.get("database")

st.title("Read")
st.write("Utilize as tabs para visualizar os registros nas tabelas de Filme, Canal e Exibição.")

# Criar varias opções de tabelas
tab1, tab2, tab3 = st.tabs(["Filme", "Canal", "Exibição"])

# Tabela Filme
with tab1:
    st.subheader("Filmes cadastrados")
    
    sql = "SELECT num_filme, titulo_original, titulo_brasil, ano_lancamento, pais_origem, categoria, duracao FROM filme"
    cursor.execute(sql)
    filmes = cursor.fetchall()

    if filmes:
        for filme in filmes:
            st.write(f"ID: {filme[0]}")
            st.write(f"Título Original: {filme[1]}")
            st.write(f"Título Brasil: {filme[2]}")
            st.write(f"Ano Lançamento: {filme[3]}")
            st.write(f"País de Origem: {filme[4]}")
            st.write(f"Categoria: {filme[5]}")
            st.write(f"Duração: {filme[6]} minutos")
            st.write("---")
    else:
        st.write("Nenhum filme cadastrado.")

# Tabela Canal
with tab2:
    st.subheader("Canais cadastrados")
    
    sql = "SELECT num_canal, nome, sigla FROM canal"
    cursor.execute(sql)
    canais = cursor.fetchall()

    if canais:
        for canal in canais:
            st.write(f"Número do Canal: {canal[0]}")
            st.write(f"Nome: {canal[1]}")
            st.write(f"Sigla: {canal[2]}")
            st.write("---")
    else:
        st.write("Nenhum canal cadastrado.")

# Tabela Exibição
with tab3:
    st.subheader("Exibições cadastradas")
    
    sql = "SELECT num_filme, num_canal, data FROM exibicao"
    cursor.execute(sql)
    exibicoes = cursor.fetchall()

    if exibicoes:
        for exibicao in exibicoes:
            st.write(f"Número do Filme: {exibicao[0]}")
            st.write(f"Número do Canal: {exibicao[1]}")
            st.write(f"Data: {exibicao[2]}")
            st.write("---")
    else:
        st.write("Nenhuma exibição cadastrada.")
