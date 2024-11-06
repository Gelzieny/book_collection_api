<h1 align="center">Projeto de API para Gerenciamento de Livros</h1>

## 💻 Sobre o projeto

<p align="justify">
Este projeto é uma API RESTful desenvolvida com Django, que permite o gerenciamento de livros, incluindo a criação, avaliação, exclusão e sorteio de livros com base em filtros. O projeto utiliza Django Ninja para a criação da API e o Django ORM para a manipulação de dados no banco de dados.
</p>

<p align="center" style="display: flex; align-items: flex-start; justify-content: center;">
  <img alt="" title="#" src="https://github.com/Gelzieny/book_collection_api/blob/main/.github/img/endp.png?raw=true" width="400px">

  <img alt="" title="#" src="https://github.com/Gelzieny/book_collection_api/blob/main/.github/img/image.png?raw=true" width="400px">
</p>

## 🔨 Funcionalidades do projeto

- `Criar um Livro`: Cria um novo livro com base nos dados fornecidos (nome, streaming e categorias).
- `Avaliar um Livro`: Atualiza a avaliação de um livro, incluindo a nota e os comentários.
- `Deletar um Livro`: Deleta o livro com o ID fornecido.
- `Sortear um Livro Aleatoriamente`: Sorteia um livro aleatoriamente com base nos filtros fornecidos (nota mínima, categorias e se o livro já foi assistido).
- `Listar Todos os Livros`: Lista todos os livros cadastrados no banco de dados.
- `Listar Todos os Categorias`: Lista todas as categorias cadastradas no banco de dados.

## 🛠 Tecnologias

<p align="justify">Este projeto utiliza um conjunto de tecnologias modernas para garantir uma aplicação eficiente e escalável, incluindo:</p>

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Ninja](https://django-ninja.dev/)

## 🚀 Como executar o projeto

### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,python,vscode" />
</a>

### 🎲 Rodando aplicação

```bash
# Clone este repositório
$ git clone <https://github.com/Gelzieny/book_collection_api.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd book_collection_api

# Instale as dependências no Windows
$ python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# Instale as dependências no Linux ou MacOS
$ python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

## 🧑🏻‍💻 Autor

Feito com ❤️ por Gelzieny R. Martins 👋🏽 [Entre em contato!](https://www.linkedin.com/in/gelzieny/)

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Projeto de gerenciamento de senhas desenvolvido na imersão de Python do Pythonando. Ele inclui módulos para manipulação de banco de dados, geração de senhas e um script principal para execução do programa.
