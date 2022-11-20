import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from aluraflix_api.videos.models import Categoria

END_POINT = 'videos:categoria-read-delete-update'

pytestmark = pytest.mark.django_db


def test_read(client_auth, categoria):

    url = resolve_url(END_POINT, categoria.id)

    resp = client_auth.delete(url)

    assert status.HTTP_204_NO_CONTENT == resp.status_code

    assert not Categoria.objects.filter(id=categoria.id).exists()


def test_not_found(client_auth):

    url = resolve_url(END_POINT, 404)

    resp = client_auth.delete(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
