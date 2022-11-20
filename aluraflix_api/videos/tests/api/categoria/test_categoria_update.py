import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from aluraflix_api.conftest import fake

pytestmark = pytest.mark.django_db


END_POINT = 'videos:categoria-read-delete-update'


def test_full_update(client_auth, categoria):

    url = resolve_url(END_POINT, categoria.id)

    data = {'titulo': fake.name(), 'cor': 'red'}

    resp = client_auth.put(url, data=data)

    assert status.HTTP_204_NO_CONTENT == resp.status_code

    categoria.refresh_from_db()

    assert categoria.id
    assert categoria.titulo == data['titulo']
    assert categoria.cor == data['cor']


@pytest.mark.parametrize(
    'field, value',
    [
        ('titulo', 'Titulo novo'),
        ('cor', 'Red'),
    ],
)
def test_partial_update(field, value, client_auth, categoria):

    url = resolve_url(END_POINT, categoria.id)

    resp = client_auth.patch(url, data={field: value})

    assert status.HTTP_204_NO_CONTENT == resp.status_code

    categoria.refresh_from_db()

    assert value == getattr(categoria, field)


@pytest.mark.parametrize(
    'field, error',
    [
        ('titulo', {'titulo': ['Este campo é obrigatório.']}),
        ('cor', {'cor': ['Este campo é obrigatório.']}),
    ],
)
def test_missing_field_in_full_update(field, error, client_auth, categoria_info, categoria):

    categoria_info.pop(field)

    url = resolve_url(END_POINT, categoria.id)

    resp = client_auth.put(url, data=categoria_info)

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


def test_not_found(client_auth):

    url = resolve_url(END_POINT, 404)

    resp = client_auth.put(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code

    resp = client_auth.patch(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
