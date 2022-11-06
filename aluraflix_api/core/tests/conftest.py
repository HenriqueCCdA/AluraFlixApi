import pytest
from faker import Faker
from rest_framework.test import APIClient

from aluraflix_api.core.models import Video

fake = Faker()


pytestmark = pytest.mark.django_db


@pytest.fixture
def video_info():
    return dict(
        titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url()
    )


@pytest.fixture
def video(video_info):
    return Video.objects.create(**video_info)


@pytest.fixture
def list_videos():
    list_ = [
        Video(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url()),
        Video(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url()),
        Video(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url()),
    ]
    Video.objects.bulk_create(list_)

    return list(Video.objects.all())


@pytest.fixture
def client():
    return APIClient()
