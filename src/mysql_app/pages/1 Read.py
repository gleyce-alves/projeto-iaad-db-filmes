import streamlit as st

cursor = st.session_state.get("cursor")
database = st.session_state.get("database")

st.title("Read")
st.write("Utilize as tabs de navegação para visualizar os itens nas tabelas de filme, canal e exibição.")

tab1, tab2, tab3 = st.tabs(["Filme", "Canal", "Exibição"])

with tab1:
    st.header("Visualizar Filmes")

    sql_filmes = "SELECT num_filme, titulo_original FROM filme"
    
    cursor.execute(sql_filmes)
    filmes = cursor.fetchall()

    if filmes:
        filme_selecionado = st.selectbox("Selecione um filme:", [f[1] for f in filmes])

        num_filme = next(f[0] for f in filmes if f[1] == filme_selecionado)

        sql_detalhes = f"""
        SELECT titulo_original, titulo_brasil, ano_lancamento, pais_origem, categoria, duracao 
        FROM filme WHERE num_filme = {num_filme}
        """

        cursor.execute(sql_detalhes)
        detalhes = cursor.fetchone()

        if detalhes:
            st.write("### Detalhes do Filme")
            st.write(f"Título Original: {detalhes[0]}")
            st.write(f"Título Brasil: {detalhes[1]}")
            st.write(f"Ano de Lançamento: {detalhes[2]}")
            st.write(f"País de Origem: {detalhes[3]}")
            st.write(f"Categoria: {detalhes[4]}")
            st.write(f"Duração: {detalhes[5]} minutos")
            st.success("Detalhes do filme carregados com sucesso!", icon="✅")
    else:
        st.warning("Nenhum filme encontrado.", icon="⚠️")

with tab2:
    st.header("Visualizar Canais")

    sql_canais = "SELECT num_canal, nome FROM canal"

    cursor.execute(sql_canais)
    canais = cursor.fetchall()

    if canais:
        canal_selecionado = st.selectbox("Selecione um canal:", [c[1] for c in canais])

        num_canal = next(c[0] for c in canais if c[1] == canal_selecionado)

        sql_detalhes_canal = f"""
        SELECT nome, sigla FROM canal WHERE num_canal = {num_canal}
        """

        cursor.execute(sql_detalhes_canal)
        detalhes_canal = cursor.fetchone()

        if detalhes_canal:
            st.write("### Detalhes do Canal")
            st.write(f"Nome: {detalhes_canal[0]}")
            st.write(f"Sigla: {detalhes_canal[1]}")
            st.success("Detalhes do canal carregados com sucesso!", icon="✅")
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
        exibição_selecionada = st.selectbox("Selecione uma exibição:", [f"{e[1]} - {e[3]} - {e[4]}" for e in exibicoes])

        num_filme, num_canal = next((e[0], e[2]) for e in exibicoes if f"{e[1]} - {e[3]} - {e[4]}" == exibição_selecionada)

        sql_detalhes_exibicao = f"""
        SELECT e.data, f.titulo_brasil, c.nome 
        FROM exibicao e
        JOIN filme f ON e.num_filme = f.num_filme
        JOIN canal c ON e.num_canal = c.num_canal
        WHERE e.num_filme = {num_filme} AND e.num_canal = {num_canal}
        """

        cursor.execute(sql_detalhes_exibicao)
        detalhes_exibicao = cursor.fetchone()

        if detalhes_exibicao:
            st.write("### Detalhes da Exibição")
            st.write(f"Título: {detalhes_exibicao[1]}")
            st.write(f"Canal: {detalhes_exibicao[2]}")
            st.write(f"Data: {detalhes_exibicao[0]}")
            st.success("Detalhes da exibição carregados com sucesso!", icon="✅")
    else:
        st.warning("Nenhuma exibição encontrada.", icon="⚠️")
