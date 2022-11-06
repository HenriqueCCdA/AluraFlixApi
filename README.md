# Django Rest Framework API

Desafio backend 5 da alura.

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | `AluraFlixApi`
| :label: Tecnologias | `Django Rest Framework`, `Python`, `Sqlite`, `Pytest`
| :rocket: URL         | 
| :fire: Desafio     | https://www.alura.com.br/challenges/back-end

![Captura de tela de 2022-11-06 20-12-44](https://user-images.githubusercontent.com/37959973/200200609-7969a2f8-279f-4c37-93ab-c3656e828837.png?text=imagem_do_peojeto#vitrinedev)

## Documentação da API:

[Postman](https://documenter.getpostman.com/view/18852890/2s8YYJq3D9)

## Preparando o ambiente de desenvolvimento

```console
python -m venv .venv --upgrade-deps
source .venv/bin/activate
pip install pip-tools
pip-sync requirements.txt requirements-dev.txt
```

## Rodando o servidor pela primeira vez

Para roda o servido para primeira vez precisamos aplicar as migrações ao `db` atravás do comando:

```console
python manage.py migrate
```

Após isto basta fazer

```console
python manage.py runserver
```
