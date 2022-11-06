import pytest
from django.shortcuts import resolve_url
from rest_framework import status

END_POINT = "core:videos-read-delete-update"

pytestmark = pytest.mark.django_db


def test_read(client, video):

    url = resolve_url(END_POINT, video.id)

    resp = client.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert video.id == body["id"]
    assert video.titulo == body["titulo"]
    assert video.descricao == body["descricao"]
    assert video.url == body["url"]


def test_not_found(client):

    url = resolve_url(END_POINT, 404)

    resp = client.get(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
