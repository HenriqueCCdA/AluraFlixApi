from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient

END_POINT = "core:videos-list-create"


def test_list(client):

    url = resolve_url(END_POINT)

    resp = client.get(url)

    assert status.HTTP_200_OK == resp.status_code

    body = resp.json()

    assert len(body) == 2

    list_db = [
        {
            "descricao": "Descricao 1",
            "id": 1,
            "titulo": "Titulo 1",
            "url": "https://qualquer1",
        },
        {
            "descricao": "Descricao 2",
            "id": 2,
            "titulo": "Titulo 2",
            "url": "https://qualquer2",
        },
    ]

    assert list_db == body
