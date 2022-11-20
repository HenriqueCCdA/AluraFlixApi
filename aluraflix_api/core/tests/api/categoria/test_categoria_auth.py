import pytest
from django.shortcuts import resolve_url
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_list_create_no_token(client, categoria_info):

    url = resolve_url('core:categoria-list-create')

    resp = client.post(url, data=categoria_info, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    assert {'detail': 'As credenciais de autenticação não foram fornecidas.'} == body


def test_list_create_invalid_token(client, categoria_info):

    client.credentials(HTTP_AUTHORIZATION='Bearer ss')

    url = resolve_url('core:categoria-list-create')

    resp = client.post(url, data=categoria_info, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    expected = {
        'detail': 'O token informado não é válido para qualquer tipo de token',
        'code': 'token_not_valid',
        'messages': [
            {'message': 'O token é inválido ou expirado', 'token_class': 'AccessToken', 'token_type': 'access'}
        ],
    }

    assert expected == body


def test_read_delete_update_no_token(client, categoria, categoria_info):

    url = resolve_url('core:categoria-read-delete-update', categoria.id)

    resp = client.post(url, data=categoria_info, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    assert {'detail': 'As credenciais de autenticação não foram fornecidas.'} == body


def test_read_delete_update_invalid_token(client, categoria, categoria_info):

    client.credentials(HTTP_AUTHORIZATION='Bearer ss')

    url = resolve_url('core:categoria-read-delete-update', categoria.id)

    resp = client.post(url, data=categoria_info, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    expected = {
        'detail': 'O token informado não é válido para qualquer tipo de token',
        'code': 'token_not_valid',
        'messages': [
            {'message': 'O token é inválido ou expirado', 'token_class': 'AccessToken', 'token_type': 'access'}
        ],
    }

    assert expected == body


def test_videos_by_categoria_no_token(client, categoria, categoria_info):

    url = resolve_url('core:videos-by-categoria', categoria.id)

    resp = client.post(url, data=categoria_info, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    assert {'detail': 'As credenciais de autenticação não foram fornecidas.'} == body


def test_videos_by_categoria_invalid_token(client, categoria, categoria_info):

    client.credentials(HTTP_AUTHORIZATION='Bearer ss')

    url = resolve_url('core:videos-by-categoria', categoria.id)

    resp = client.post(url, data=categoria_info, format='json')

    assert status.HTTP_401_UNAUTHORIZED == resp.status_code

    body = resp.json()

    expected = {
        'detail': 'O token informado não é válido para qualquer tipo de token',
        'code': 'token_not_valid',
        'messages': [
            {'message': 'O token é inválido ou expirado', 'token_class': 'AccessToken', 'token_type': 'access'}
        ],
    }

    assert expected == body
