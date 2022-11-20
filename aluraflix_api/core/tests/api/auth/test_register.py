import pytest
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from rest_framework import status

User = get_user_model()

pytestmark = pytest.mark.django_db

ENDPOINT = 'core:register'


def test_ok(client, user_register):

    url = resolve_url(ENDPOINT)

    resp = client.post(url, data=user_register, format='json')

    assert status.HTTP_201_CREATED == resp.status_code

    body = resp.json()

    user_db = User.objects.first()

    assert user_db.username == body['username']
    assert user_db.email == body['email']
    assert user_db.id == body['id']


@pytest.mark.parametrize(
    'field, error',
    [
        ('username', {'username': ['Este campo é obrigatório.']}),
        ('password', {'password': ['Este campo é obrigatório.']}),
        ('password2', {'password2': ['Este campo é obrigatório.']}),
    ],
)
def test_missing_fields(client, field, error, user_register):

    user_register.pop(field)

    url = resolve_url(ENDPOINT)

    resp = client.post(url, data=user_register, format='json')

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


def test_fail_username_already_exists(client, user, user_register):

    url = resolve_url(ENDPOINT)
    resp = client.post(url, data=user_register)

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert {'username': ['Um usuário com este nome de usuário já existe.']} == body


@pytest.mark.parametrize(
    'password, error',
    [
        ('15684568', {'non_field_errors': ['Esta senha é inteiramente numérica.']}),
        ('ads2', {'non_field_errors': ['Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres.']}),
    ],
)
def test_fail_password(password, error, client, user_register):

    user_register['password'] = password
    user_register['password2'] = password

    url = resolve_url(ENDPOINT)

    resp = client.post(url, data=user_register, format='json')

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


def test_invalid_email(client, user_register):

    user_register['email'] = 'useremail.com'

    url = resolve_url(ENDPOINT)

    resp = client.post(url, data=user_register, format='json')

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert {'email': ['Insira um endereço de email válido.']} == body
