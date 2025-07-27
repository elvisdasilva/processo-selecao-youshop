# 🌲Trees Everywhere
[![Python Version](https://img.shields.io/badge/python-3.12.8-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-5.2.4-blue.svg)](https://www.djangoproject.com/)
[![pip Version](https://img.shields.io/badge/pip-24.3.1-blue.svg)](https://pypi.org/project/pip/)



## Descrição
Este repositório contém o código-fonte do Trees Everywhere, que foi desenvolvido para o processo seletivo da YouShop. O projeto tem por objetivo criar um banco de dados de árvores plantadas por voluntários espalhados pelo mundo.

## Funcionalidades Principais
- Admin
    * Cadastro de novos usuários e senha. Permite associar um usuário a uma conta.
    * Listagem e criação de contas (modelo Account).
        - Permite ativar e desativar contas a partir da tela de listagem de contas.
    * Cadastro e visualização de plantas (modelo Tree).
        - A página de visualização de uma planta mostra a lista de todas as plantas deste tipo que foram plantadas (modelo PlantedTree), incluindo o nome da pessoa que plantou.

- Template Views
    * Fazer login de um usuário que foi cadastrado pelo admin.
    * Visualizar as árvores plantadas por um usuário.
        - Um usuário não consegue visualizar as árvores plantadas por outro usuário a não ser que este faça parte da mesma conta.
        - Um usuário só consegue editar a sua própria plantação.
    * Exibir os dados de uma árvore plantada via tabela.
    * Plantar uma árvore.
    * O usuário possui uma página de perfil que pode conter um texto onde ele fala sobre si(bio) e a data em que ele entrou na plataforma.

- API
    * Autenticação via JWT.
    * Método de api REST que retorna em formato json uma lista de todas as árvores plantadas pelo usuário logado atualmente.

## Tecnologias Utilizadas
- Django 5: https://www.djangoproject.com/
- AdminLTE: https://adminlte.io/


## Instalação

**Clone o repositório**
```
git clone https://github.com/elvisdasilva/processo-selecao-youshop.git
```

**Acesse o diretório**
```
cd processo-selecao-youshop
```

**Crie um ambiente virtual e ative**
```
python -m venv venv
```
**Windows**
```
.\venv\Scripts\activate
```
**Linux**
```
source venv/bin/activate
```
**Instale as dependências do projeto**
```
pip install -r requirements.txt
```

## Conexão com o banco de dados e execução de migrations
**Execute as migrations**
```
python manage.py migrate
```

## Criando usuário Admin
```
python manage.py createsuperuser
```

## Executando o projeto
Após obter sucesso em toda a instalação, é hora de rodar o projeto.
```
python manage.py runserver
```

## Acessar o sistema

- Admin: http://localhost:8000/admin
- Login: http://localhost:8000/login
- API: http://localhost:8000/api/planted-tree/


## Obrigado!
Se encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para enviar pull requests. Agradeço pela sua contribuição!

