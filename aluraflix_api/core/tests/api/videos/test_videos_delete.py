import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from aluraflix_api.core.models import Video

END_POINT = 'core:videos-read-delete-update'

pytestmark = pytest.mark.django_db


def test_read(client_auth, video):

    url = resolve_url(END_POINT, video.id)

    resp = client_auth.delete(url)

    assert status.HTTP_204_NO_CONTENT == resp.status_code

    assert not Video.objects.filter(id=video.id).exists()


def test_not_found(client_auth):

    url = resolve_url(END_POINT, 404)

    resp = client_auth.delete(url)

    assert status.HTTP_404_NOT_FOUND == resp.status_code
