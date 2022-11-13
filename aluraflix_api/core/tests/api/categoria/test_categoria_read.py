import pytest
from django.shortcuts import resolve_url
from rest_framework import status

END_POINT = 'core:categoria-read-delete-update'

pytestmark = pytest.mark.django_db


def test_read(client, categoria):

    url = resolve_url(END_POINT, categoria.id)

    resp = client.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert categoria.id == body['id']
    assert categoria.titulo == body['titulo']
    assert categoria.cor == body['cor']


def test_not_found(client):

    url = resolve_url(END_POINT, 404)

    resp = client.get(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
