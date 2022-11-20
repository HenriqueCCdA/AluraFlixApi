import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from aluraflix_api.core.models import Video

pytestmark = pytest.mark.django_db


END_POINT = 'core:videos-list-create'


def test_create(client_auth, video_info):

    url = resolve_url(END_POINT)

    resp = client_auth.post(url, data=video_info, format='json')

    assert status.HTTP_201_CREATED == resp.status_code

    body = resp.json()

    from_db = Video.objects.get(titulo=video_info['titulo'])

    assert from_db.id == body['id']
    assert from_db.titulo == body['titulo']
    assert from_db.descricao == body['descricao']
    assert from_db.categoria.id == body['categoria']
    assert from_db.url == body['url']


def test_create_without_caregoria(client_auth, video_info):

    url = resolve_url(END_POINT)
    video_info.pop('categoria_id')
    resp = client_auth.post(url, data=video_info, format='json')

    assert status.HTTP_201_CREATED == resp.status_code

    body = resp.json()

    from_db = Video.objects.get(titulo=video_info['titulo'])

    # assert 1 == from_db.categoria.id
    assert 'LIVRE' == from_db.categoria.titulo

    assert from_db.id == body['id']
    assert from_db.titulo == body['titulo']
    assert from_db.descricao == body['descricao']
    assert from_db.categoria.id == body['categoria']
    assert from_db.url == body['url']


@pytest.mark.parametrize(
    'field, error',
    [
        ('titulo', {'titulo': ['Este campo é obrigatório.']}),
        ('descricao', {'descricao': ['Este campo é obrigatório.']}),
        ('url', {'url': ['Este campo é obrigatório.']}),
    ],
)
def test_missing_field(field, error, client_auth, video_info):

    video_info.pop(field)

    url = resolve_url(END_POINT)

    resp = client_auth.post(url, data=video_info, format='json')

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


@pytest.mark.parametrize(
    'field, value, error',
    [
        ('url', '45684', {'url': ['Entrar um URL válido.']}),
    ],
)
def test_invalid_field(field, value, error, client_auth, video_info):

    video_info[field] = value

    url = resolve_url(END_POINT)

    resp = client_auth.post(url, data=video_info, format='json')

    assert status.HTTP_400_BAD_REQUEST == resp.status_code

    body = resp.json()

    assert error == body


def test_create_wrong_caregoria(client_auth, video_info):

    url = resolve_url(END_POINT)
    video_info['categoria_id'] = 404
    resp = client_auth.post(url, data=video_info, format='json')

    assert status.HTTP_409_CONFLICT == resp.status_code

    body = resp.json()

    assert 'Categoria inválida.' == body['error']
