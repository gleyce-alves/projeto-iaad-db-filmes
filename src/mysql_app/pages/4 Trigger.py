import streamlit as st

st.title("Trigger")
st.subheader('Apenas filmes que tivessem uma duração maior que 30 minutos e menor que 3h30 podem ser inseridos no nosso banco de dados.')

sql_code = """
CREATE TRIGGER verifica_duracao_filme
BEFORE INSERT ON filme
FOR EACH ROW
BEGIN
    IF NEW.duracao < 30 OR NEW.duracao > 210 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A duração do filme deve ser maior que 30 minutos e menor que 3 horas e 30 minutos.';
    END IF;
END$$

-- Trigger para impedir atualizações de filmes com duração inválida
CREATE TRIGGER verifica_duracao_filme_update
BEFORE UPDATE ON filme
FOR EACH ROW
BEGIN
    IF NEW.duracao < 30 OR NEW.duracao > 210 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A duração do filme deve ser maior que 30 minutos e menor que 3 horas e 30 minutos.';
    END IF;
END$$
"""

st.code(sql_code, language='sql')