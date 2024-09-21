import streamlit as st
from datetime import datetime
import psycopg2

cursor = st.session_state.get("cursor")
database = st.session_state.get("database")

st.title("Update")
st.write("Utilize as tabs de navegação para atualizar os itens nas tabelas de filme, canal e exibição.")

tab1, tab2, tab3 = st.tabs(["Filme", "Canal", "Exibição"])

# Função para capturar erros de integridade
def handle_integrity_error(error):
    if "foreign key" in str(error).lower():
        st.error("Erro de integridade referencial: O ID informado não existe na tabela relacionada.", icon="⚠️")
    elif "not null" in str(error).lower():
        st.error("Erro de integridade: Um ou mais campos obrigatórios não foram preenchidos.", icon="⚠️")
    elif "unique" in str(error).lower():
        st.error("Erro de integridade: Valor duplicado detectado para um campo único.", icon="⚠️")
    elif "primary key" in str(error).lower():
        st.error("Erro de integridade: O valor da chave primária já existe ou é inválido.", icon="⚠️")
    else:
        st.error(f"Ocorreu um erro: {str(error)}", icon="⚠️")

# Aba 1 - Atualizar Filme
with tab1:
    st.header("Atualizar Filme")

    filme_id = st.number_input("Digite o ID do filme para atualizar", step=1)

    titulo_original = st.text_input("Título original")
    titulo_brasil = st.text_input("Título Brasil")
    ano_lancamento = st.number_input("Ano lançamento", min_value=1900, max_value=2025)
    pais_origem = st.text_input("País de origem")
    categoria = st.selectbox("Categoria", ["Ação", "Comédia", "Drama", "Ficção científica", "Terror", "Romance", "Animação", "Aventura", "Suspense", "Fantasia"])
    duracao = st.number_input("Duração (em minutos)", step=1, min_value=1)

    sql_filme_update = """
    UPDATE filme 
    SET titulo_original=%s, titulo_brasil=%s, ano_lancamento=%s, pais_origem=%s, categoria=%s, duracao=%s 
    WHERE num_filme=%s
    """

    submitted_filme = st.button("Atualizar filme")

    if submitted_filme:
        values = (titulo_original, titulo_brasil, ano_lancamento, pais_origem, categoria, duracao, filme_id)

        if any(item is None or item == '' for item in values[:-1]): 
            st.warning("Preencha todos os campos.", icon="⚠️")
        else:
            try:
                with st.spinner("Atualizando dados..."):
                    cursor.execute(sql_filme_update, values)
                    database.commit()
                    st.success("Filme atualizado com sucesso!", icon="✅")
            except psycopg2.IntegrityError as e:
                database.rollback()  # Desfaz a transação
                handle_integrity_error(e)

# Aba 2 - Atualizar Canal
with tab2:
    st.header("Atualizar Canal")

    canal_id = st.number_input("Digite o ID do canal para atualizar", step=1)

    nome_canal = st.text_input("Nome do canal")
    sigla_canal = st.text_input("Sigla do canal")

    sql_canal_update = """
    UPDATE canal 
    SET nome=%s, sigla=%s 
    WHERE num_canal=%s
    """

    submitted_canal = st.button("Atualizar canal")

    if submitted_canal:
        values = (nome_canal, sigla_canal, canal_id)

        if any(item is None or item == '' for item in values[:-1]):
            st.warning("Preencha todos os campos.", icon="⚠️")
        else:
            try:
                with st.spinner("Atualizando dados..."):
                    cursor.execute(sql_canal_update, values)
                    database.commit()
                    st.success("Canal atualizado com sucesso!", icon="✅")
            except psycopg2.IntegrityError as e:
                database.rollback()
                handle_integrity_error(e)

# Aba 3 - Atualizar Exibição
with tab3:
    st.header("Atualizar Exibição")

    filme_id = st.number_input("Digite o ID do filme", step=1)
    canal_id = st.number_input("Digite o ID do canal", step=1)

    data_exibicao = st.date_input("Data de exibição", format="DD/MM/YYYY")
    hora_exibicao = st.time_input("Hora de exibição")

    sql_exibicao_update = """
    UPDATE exibicao 
    SET data=%s 
    WHERE num_filme=%s AND num_canal=%s
    """

    submitted_exibicao = st.button("Atualizar exibição")

    if submitted_exibicao:
        data_hora = datetime.combine(data_exibicao, hora_exibicao)
        values = (data_hora, filme_id, canal_id)

        if any(item is None or item == '' for item in values[:-2]): 
            st.warning("Preencha todos os campos.", icon="⚠️")
        else:
            try:
                with st.spinner("Atualizando dados..."):
                    cursor.execute(sql_exibicao_update, values)
                    database.commit()
                    st.success("Exibição atualizada com sucesso!", icon="✅")
            except psycopg2.IntegrityError as e:
                database.rollback()
                handle_integrity_error(e)
