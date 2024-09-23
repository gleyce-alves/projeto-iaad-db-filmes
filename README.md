# Sistema de Programação de Filmes - MySQL & NoSQL 

### Integrantes:
- Anna Carolina Bejan
- Edney Santos
- Gleyce Alves
- Matheus Costa
- Mylena Araújo
- Ygor Macêdo

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema computacional web utilizando o banco de dados relacional MySQL e o framework Streamlit em Python. O sistema implementa as operações básicas de CRUD (Create, Read, Update, Delete) para a gestão de programações de filmes, além de incluir um trigger customizado. Também será abordado o uso de um banco de dados NoSQL, com exemplos práticos das operações CRUD nesse tipo de banco.

## Estrutura do Projeto

- **/src**: Contém os códigos-fonte do projeto.
  - **/mysql_app**: Contém os arquivos relacionados à implementação da aplicação MySQL com Streamlit.
    - **App.py**: Arquivo principal da aplicação.
    - **db.py**: Script de conexão e operações com o banco de dados MySQL.
    - **/pages**: Contém as páginas que implementam as operações CRUD e trigger:
      - **0 Create.py**: Implementa a funcionalidade de criação (Create) no sistema.
      - **1 Read.py**: Implementa a funcionalidade de leitura (Read) no sistema.
      - **2 Update.py**: Implementa a funcionalidade de atualização (Update) no sistema.
      - **3 Delete.py**: Implementa a funcionalidade de exclusão (Delete) no sistema.
      - **4 Trigger.py**: Implementa o trigger customizado no sistema.
  - **/nosql_app**: Diretório reservado para a futura implementação da aplicação NoSQL.

- **/data**: Contém scripts SQL para a configuração do banco de dados.
  - **database_setup.sql**: Script para criar as tabelas e inserir dados no banco MySQL.

- **/docs**: Contém a documentação do projeto.
  - **der.png**: Diagrama Entidade-Relacionamento do banco de dados.

## Pré-requisitos

- **Python 3.8+**
- **MySQL 8.0+**
- **Bibliotecas Python**:
  - streamlit
  - mysql-connector-python
  - redis

Instale as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Como Rodar a aplicação

1. Certifique-se de que você está na raiz do projeto.
2. Navegue até o diretório onde está o arquivo **App.py** da aplicação MySQL:

```bash
   cd src/mysql_app
```

Execute o aplicativo usando o Streamlit:

```bash
  streamlit run App.py
```

O aplicativo será aberto no navegador padrão, e você poderá acessar a interface do sistema de programação de filmes.