import pytest
from django.shortcuts import resolve_url
from rest_framework import status

END_POINT = 'core:videos-by-categoria'

pytestmark = pytest.mark.django_db


def test_list(client_auth, list_videos, categoria):

    url = resolve_url(END_POINT, categoria.pk)

    resp = client_auth.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert len(list_videos) == len(body)

    for db, response in zip(list_videos, body):
        assert db.titulo == response['titulo']
        assert db.categoria.id == response['categoria']
        assert db.url == response['url']
        assert db.descricao == response['descricao']


def test_list_empty(client_auth, categoria):

    url = resolve_url(END_POINT, categoria.pk)

    resp = client_auth.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert 0 == len(body)

    assert [] == body


def test_not_found(client_auth):

    url = resolve_url(END_POINT, 404)

    resp = client_auth.get(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
