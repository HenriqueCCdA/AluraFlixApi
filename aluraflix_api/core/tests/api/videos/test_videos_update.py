import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from aluraflix_api.core.tests.conftest import fake

pytestmark = pytest.mark.django_db


END_POINT = 'core:videos-read-delete-update'


def test_full_update(client_auth, video):

    url = resolve_url(END_POINT, video.id)

    data = {
        'titulo': fake.name(),
        'descricao': fake.sentence(nb_words=20),
        'url': fake.url(),
    }

    resp = client_auth.put(url, data=data)

    assert status.HTTP_204_NO_CONTENT == resp.status_code

    video.refresh_from_db()

    assert video.id
    assert video.titulo == data['titulo']
    assert video.descricao == data['descricao']
    assert video.url == data['url']


@pytest.mark.parametrize(
    'field, value',
    [
        ('titulo', 'Titulo novo'),
        ('descricao', 'Descricação nova'),
        ('url', 'https://www.new.com'),
    ],
)
def test_partial_update(field, value, client_auth, video):

    url = resolve_url(END_POINT, video.id)

    resp = client_auth.patch(url, data={field: value})

    assert status.HTTP_204_NO_CONTENT == resp.status_code

    video.refresh_from_db()

    assert value == getattr(video, field)


@pytest.mark.parametrize(
    'field, error',
    [
        ('titulo', {'titulo': ['Este campo é obrigatório.']}),
        ('descricao', {'descricao': ['Este campo é obrigatório.']}),
        ('url', {'url': ['Este campo é obrigatório.']}),
    ],
)
def test_missing_field_in_full_update(field, error, client_auth, video_info, video):

    video_info.pop(field)

    url = resolve_url(END_POINT, video.id)

    resp = client_auth.put(url, data=video_info)

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


@pytest.mark.parametrize(
    'field, value, error',
    [
        ('url', '45684', {'url': ['Entrar um URL válido.']}),
    ],
)
def test_invalid_field(field, value, error, client_auth, video_info, video):

    video_info[field] = value

    url = resolve_url(END_POINT, video.id)

    # full update

    resp = client_auth.put(url, data=video_info)

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body

    # partial update

    resp = client_auth.patch(url, data=video_info)

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


def test_not_found(client_auth):

    url = resolve_url(END_POINT, 404)

    resp = client_auth.put(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code

    resp = client_auth.patch(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
