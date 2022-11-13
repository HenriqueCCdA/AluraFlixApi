from datetime import datetime

import pytest

from aluraflix_api.core.models import Categoria

pytestmark = pytest.mark.django_db


def test_create(categoria):
    assert Categoria.objects.exists()
    assert categoria.id


def test_str(categoria):
    assert categoria.titulo == str(categoria)


def test_create_and_modified_at(categoria):
    assert isinstance(categoria.created_at, datetime)
    assert isinstance(categoria.modified_at, datetime)


def test_one_to_many(video, categoria):
    assert categoria.videos.exists()


def test_get_absolute_url(categoria):

    assert f'/categorias/{categoria.id}' == categoria.get_absolute_url()
