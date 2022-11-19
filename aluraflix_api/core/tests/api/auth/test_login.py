import pytest
from django.shortcuts import resolve_url
from rest_framework import status

pytestmark = pytest.mark.django_db

ENDPOINT = 'core:login'


def test_ok(client, user):

    url = resolve_url(ENDPOINT)

    data = {'username': 'user1', 'password': '123456!!'}

    resp = client.post(url, data=data, format='json')

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert 'access' in body
    assert 'refresh' in body


def test_missing_fields(client, user):

    url = resolve_url(ENDPOINT)

    resp = client.post(url, data={}, format='json')

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    expected = {'password': ['Este campo é obrigatório.'], 'username': ['Este campo é obrigatório.']}

    assert expected == body


def test_wrong_credentials(client, user):

    url = resolve_url(ENDPOINT)

    data = {'username': 'user', 'password': '123456!!'}

    resp = client.post(url, data=data, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    assert {'detail': 'Usuário e/ou senha incorreto(s)'} == body
