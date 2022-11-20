import pytest
from django.shortcuts import resolve_url
from rest_framework import status

END_POINT = 'core:videos-list-create'

pytestmark = pytest.mark.django_db


def test_list(client_auth, list_videos):

    url = resolve_url(END_POINT)

    resp = client_auth.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert len(list_videos) == len(body)

    for from_db, from_api in zip(list_videos, body):
        assert from_db.id == from_api['id']
        assert from_db.titulo == from_api['titulo']
        assert from_db.descricao == from_api['descricao']
        assert from_db.url == from_api['url']


def test_list_empty(client_auth):

    url = resolve_url(END_POINT)

    resp = client_auth.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert 0 == len(body)

    assert [] == body


def test_search_match(client_auth, list_videos_fixed_title):

    url = resolve_url(END_POINT)

    resp = client_auth.get(url, {'search': 'jogo'})

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert 2 == len(body)


def test_search_dont_match(client_auth, list_videos_fixed_title):

    url = resolve_url(END_POINT)

    resp = client_auth.get(url, {'search': 'Banana'})

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert 0 == len(body)

    assert [] == body
