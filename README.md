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
```bash
git clone https://github.com/elvisdasilva/processo-seletivo-youshop.git
```

**Acesse o diretório**
```bash
cd processo-seletivo-youshop
```

**Crie um ambiente virtual e ative**
```bash
python -m venv venv
```
**Windows**
```bash
.\venv\Scripts\activate
```
**Linux**
```bash
source venv/bin/activate
```
**Instale as dependências do projeto**
```bash
pip install -r requirements.txt
```

## Conexão com o banco de dados e execução de migrations
**Execute as migrations**
```bash
python manage.py migrate
```

## Criando usuário Admin
```bash
python manage.py createsuperuser
```

> ℹ️ **Observação:**  
> Ao tentar fazer login no template de login com o usuário `admin` (usuário criado via `createsuperuser`), ocorrerá o seguinte erro:  
> 
> `User has no extension.`  
> 
> Isso acontece porque o usuário `admin` não possui uma instância de `UserExtension` associada.  
> Para evitar o erro, crie manualmente a extensão para esse usuário com o comando:
>
> ```bash
> python manage.py shell
> ```
> ```python
> from django.contrib.auth.models import User
> from apps.user.models import UserExtension
>
> admin = User.objects.get(username="admin")
> UserExtension.objects.create(user=admin)
> ```


## Executando o projeto
Após obter sucesso em toda a instalação, é hora de rodar o projeto.
```bash
python manage.py runserver
```

## Acessar o sistema

- Admin: http://localhost:8000/admin
- Login: http://localhost:8000/login
- API: http://localhost:8000/api/planted-tree/


## 📬 Utilizando a API com Postman

A API da aplicação utiliza autenticação JWT para proteger os endpoints. Abaixo estão os passos para autenticar e fazer requisições via Postman:

## 🔐 1. Obter o Token de Acesso

Faça uma requisição `POST` para o endpoint de autenticação:

**Endpoint:**  
```
api/v1/authentication/token/
```

**Corpo da requisição (JSON):**
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

**Resposta esperada**
```json
{
  "access": "seu_token_de_acesso",
  "refresh": "seu_token_de_refresh"
}
```

## 🚪 2. Acessar Endpoints Autenticados
Com o token access, você pode acessar os endpoints protegidos. Basta adicionar o seguinte cabeçalho nas suas requisições:
```Headers
Authorization: Bearer seu_token_de_acesso
```

## 🌱 3. Exemplo: Listar Árvores Plantadas pelo Usuário Logado

Faça uma requisição `GET` para o endpoint de listagem:

**Endpoint:**
```
api/planted-tree/
```

**Resposta esperada**
```json
[
    {
        "id": 3,
        "age": 224,
        "planted_at": "2025-07-27T11:45:39.186635-03:00",
        "location_latitude": "-00.000000",
        "location_longitude": "-00.000000",
        "user": 3,
        "tree": 1,
        "account": 2
    },
    {
        "id": 2,
        "age": 223,
        "planted_at": "2025-07-27T11:41:38.422222-03:00",
        "location_latitude": "-00.000000",
        "location_longitude": "-00.000000",
        "user": 3,
        "tree": 1,
        "account": 1
    }
]
```

## 🔁 4. Refresh do Token (Opcional)

Quando o token access expirar, use o token refresh para obter um novo. Faça uma requisição `GET` para o endpoint de refresh:

**Endpoint:**
```
api/v1/authentication/token/refresh/
```
**Corpo da requisição (JSON):**
```json
{
  "refresh": "seu_token_de_refresh"
}
```

**Resposta esperada**
```json
{
  "access": "novo_token_de_acesso"
}
```

## 🧪 5. Testes

Criar um cenário de teste com duas contas, três usuários distribuídos pelas duas contas e
algumas árvores plantadas por cada um. Este cenário será utilizado nos testes abaixo:

- ✅ Criar um teste de template que mostre que a listagem de árvores plantadas por um usuário
  específico está sendo renderizada corretamente.

- 🚫 Criar um teste de template que mostre que ao tentar acessar as árvores plantadas por outro
  usuário é retornado um erro 403 (Forbidden).

- 🔁 Criar um teste de template que mostre que a listagem de árvores plantadas pelos usuários das
  contas das quais o usuário é membro está sendo renderizada corretamente.

- 🌱 Criar testes unitários para os métodos `User.plant_tree()` e `User.plant_trees` que
  demonstrem que, ao serem chamados, os respectivos objetos `PlantedTree` são criados e
  associados ao usuário.


Para executar os testes, acesse a pasta apps e utilize o seguinte comando:

```bash
python manage.py test
```

## Obrigado!
Se encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para enviar pull requests. Agradeço pela sua contribuição!

