
## Preparando o ambiente de desenvolvimento

```console
python -m venv .venv --upgrade-deps
source .venv/bin/activate
pip install pip-tools
pip-sync requirements.txt requirements-dev.txt
```
