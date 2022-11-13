import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from aluraflix_api.core.models import Categoria

pytestmark = pytest.mark.django_db


END_POINT = 'core:categoria-list-create'


def test_create(client, categoria_info):

    url = resolve_url(END_POINT)

    resp = client.post(url, data=categoria_info)

    assert status.HTTP_201_CREATED == resp.status_code

    body = resp.json()

    from_db = Categoria.objects.get(titulo=categoria_info['titulo'])

    expected = f'/categorias/{from_db.pk}'

    assert expected == resp.headers['Location']

    assert from_db.id == body['id']
    assert from_db.titulo == body['titulo']
    assert from_db.cor == body['cor']


@pytest.mark.parametrize(
    'field, error',
    [
        ('titulo', {'titulo': ['Este campo é obrigatório.']}),
        ('cor', {'cor': ['Este campo é obrigatório.']}),
    ],
)
def test_missing_field(field, error, client, categoria_info):

    categoria_info.pop(field)

    url = resolve_url(END_POINT)

    resp = client.post(url, data=categoria_info)

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body
