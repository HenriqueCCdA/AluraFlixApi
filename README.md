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
