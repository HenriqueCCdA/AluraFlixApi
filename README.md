# Django Rest Framework API

Desafio backend 5 da alura.

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | `AluraFlixApi`
| :label: Tecnologias | `Django Rest Framework`, `Python`, `Sqlite`, `Pytest`
| :rocket: URL         |
| :fire: Desafio     | https://www.alura.com.br/challenges/back-end

![Captura de tela de 2022-11-06 20-12-44](https://user-images.githubusercontent.com/37959973/200200609-7969a2f8-279f-4c37-93ab-c3656e828837.png?text=imagem_do_peojeto#vitrinedev)

Index
    - [Documentação da  API](#documentação-da-api)
    - [Preparando o ambiente de desenvolvimento](#preparando-o-ambiente-de-desenvolvimento)
    - [Rodando o servidor pela primeira vez](#rodando-o-servidor-pela-primeira-vez)
    - [Variaveis de Ambiente](#variaveis-de-ambiente)
    - [Subindo o banco de dados](#subindo-postgresql-com-o-docker)
    - [Usando o sqlite](#usando-o-sqlite)
    - [Rodando os testes](#rodando-os-testes)


## Documentação da API:

[Postman](https://documenter.getpostman.com/view/18852890/2s8YYJq3D9)

## Preparando o ambiente de desenvolvimento

```console
python -m venv .venv --upgrade-deps
source .venv/bin/activate
cp contrib/env-samples .env
pip install pip-tools
pip-sync requirements.txt requirements-dev.txt
```

## Rodando o servidor pela primeira vez

Para roda o servido na primeira vez precisamos aplicar as migrações ao `db` atravás do comando:

```console
python manage.py migrate
```

Após isto basta fazer

```console
python manage.py runserver
```

## Variaveis de ambiente

As variaveis de ambiente podem estão no arquivo `.env`

```console
DEBUG=True
SECRET_KEY=Sua chave secreta aqui!
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://aluratube:aluratube@localhost:5435/aluratube
```

## Subindo postgresql com o Docker

Para subir o o `db` basta executar o `docker-compose` abaixo. O banco irá ficar disponivel na porta `5435`. Note que as configurações do banco estão na variavel `DATABASE_URL`

```console
docker-compose -f docker-compose-db.yml up -d
```

## Usando o sqlite

Para usar o `sqlite` basta excluir a varaivel `DATABASE_URL` do arquivo `.env`.

## Rodando os testes

```console
pytest
```