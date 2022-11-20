import pytest
from django.shortcuts import resolve_url
from rest_framework import status

END_POINT = 'core:categoria-list-create'

pytestmark = pytest.mark.django_db


def test_list(client_auth, list_categorias):

    url = resolve_url(END_POINT)

    resp = client_auth.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert len(list_categorias) == len(body)

    for from_db, from_api in zip(list_categorias, body):
        assert from_db.id == from_api['id']
        assert from_db.titulo == from_api['titulo']
        assert from_db.cor == from_api['cor']


def test_list_empty(client_auth):

    url = resolve_url(END_POINT)

    resp = client_auth.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert 0 == len(body)

    assert [] == body
