# Sistema de Programação de Filmes - MySQL & NoSQL

### Integrantes:
- Ygor Macêdo
- Matheus Costa
- Anna Carolina Bejan
- Gleyce Alves
- Edney Santos

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema computacional web utilizando o banco de dados relacional MySQL e o framework Streamlit em Python. O sistema implementa as operações básicas de CRUD (Create, Read, Update, Delete) para a gestão de programações de filmes, além de incluir um trigger customizado. Também será abordado o uso de um banco de dados NoSQL, com exemplos práticos das operações CRUD nesse tipo de banco.

## Estrutura do Projeto

- **/src**: Contém os códigos-fonte do projeto.
  - **/mysql_app**: Contém os arquivos relacionados à implementação da aplicação MySQL com Streamlit.
    - `app.py`: Arquivo principal da aplicação.
    - `db.py`: Script de conexão e operações com o banco de dados MySQL.
    - `crud_operations.py`: Funções para realizar as operações CRUD no banco de dados MySQL.
    - `trigger.sql`: Script de criação do trigger no MySQL.
    - **/templates**: Contém os arquivos HTML e outros templates utilizados na interface.
  - **/nosql_app**: Contém os arquivos relacionados à implementação da aplicação NoSQL.
    - `nosql_example.py`: Arquivo contendo exemplos das operações CRUD no banco de dados NoSQL.
    - `nosql_comparison.py`: Script para comparação entre MySQL e o banco de dados NoSQL escolhido.
  
- **/data**: Contém o script SQL para criação das tabelas e inserção de dados iniciais.
  - `database_setup.sql`: Script para criar as tabelas e inserir dados no banco MySQL.
  
- **/docs**: Contém a documentação do projeto.
  - `relatorio.pdf`: Documento com explicações detalhadas sobre o desenvolvimento do sistema, ambiente de desenvolvimento e a explicação do trigger.
  - `der.png`: Diagrama Entidade-Relacionamento do banco de dados.

## Pré-requisitos

- **Python 3.8+**
- **MySQL 8.0+**
- **Bibliotecas Python**:
  - streamlit
  - mysql-connector-python
  - pymongo (caso MongoDB seja utilizado para a parte NoSQL)
  
Instale as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
