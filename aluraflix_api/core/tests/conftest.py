import pytest
from faker import Faker

from aluraflix_api.core.models import Video

fake = Faker()


@pytest.fixture
def video_info():
    return dict(
        titulo=fake.name(), descricao=fake.sentence(nb_words=20), url="https://qualquer"
    )


@pytest.fixture
def video(video_info, db):
    return Video.objects.create(**video_info)
