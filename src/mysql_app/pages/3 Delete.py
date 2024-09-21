import streamlit as st
from datetime import datetime

cursor = st.session_state.get("cursor")
database = st.session_state.get("database")

st.title("Delete")
st.write("Utilize as tabs de navegação para deletar itens das tabelas de filme, canal e exibição.")

tab1, tab2, tab3 = st.tabs(["Filme", "Canal", "Exibição"])

# Deletar Filme
with tab1:

    sql = "DELETE FROM filme WHERE num_filme = %s"

    num_filme = st.number_input("Número do filme para deletar", step=1, value=None)

    submitted = st.button("Deletar filme", key="delete_filme")

    with st.expander("Ver SQL utilizado"):
        st.write(sql)

    if submitted:
        if num_filme is None or num_filme == 0:
            st.warning('Insira um número de filme válido.', icon="⚠️")
        else:
            st.spinner("Deletando dados...")

            cursor.execute(sql, (num_filme,))
            database.commit()

            st.success(f'Filme com número {num_filme} deletado com sucesso!', icon="✅")

# Deletar Canal
with tab2:

    sql = "DELETE FROM canal WHERE num_canal = %s"

    num_canal = st.number_input("Número do canal para deletar", step=1, value=None)

    submitted = st.button("Deletar canal", key="delete_canal")

    with st.expander("Ver SQL utilizado"):
        st.write(sql)

    if submitted:
        if num_canal is None or num_canal == 0:
            st.warning('Insira um número de canal válido.', icon="⚠️")
        else:
            st.spinner("Deletando dados...")

            cursor.execute(sql, (num_canal,))
            database.commit()

            st.success(f'Canal com número {num_canal} deletado com sucesso!', icon="✅")

# Deletar Exibição
with tab3:

    sql = "DELETE FROM exibicao WHERE num_filme = %s AND num_canal = %s AND data = %s"

    left, middle1, middle2, right = st.columns(4)

    num_filme = left.number_input("Número do filme", step=1, value=None, key="delete_num_filme")
    num_canal = middle1.number_input("Número do canal", step=1, value=None, key="delete_num_canal")
    data = middle2.date_input("Data", format="DD/MM/YYYY")
    hora = right.time_input("Hora")

    submitted = st.button("Deletar exibição", key="delete_exibicao")

    with st.expander("Ver SQL utilizado"):
        st.write(sql)

    if submitted:
        data_hora = datetime.combine(data, hora)
        values = (num_filme, num_canal, data_hora)

        if any(item is None or item == '' or item == 0 for item in values):
            st.warning('Preencha todos os campos.', icon="⚠️")
        else:
            st.spinner("Deletando dados...")

            cursor.execute(sql, values)
            database.commit()

            st.success(f'Exibição com filme {num_filme}, canal {num_canal} e data {data_hora} deletada com sucesso!', icon="✅")
