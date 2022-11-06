from datetime import datetime

from aluraflix_api.core.models import Video


def test_create(video):
    assert Video.objects.exists()
    assert video.id


def test_str(video):
    assert video.titulo == str(video)


def test_calibration_create_and_modified_at(video):
    assert isinstance(video.created_at, datetime)
    assert isinstance(video.modified_at, datetime)
