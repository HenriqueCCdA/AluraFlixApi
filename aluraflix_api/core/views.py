from dataclasses import asdict, dataclass, field

from rest_framework.decorators import api_view
from rest_framework.response import Response


@dataclass
class Videos:
    id: int = field()
    titulo: str = field()
    descricao: str = field()
    url: str = field()


videos_lista = [
    Videos(1, "Titulo 1", "Descricao 1", "https://qualquer1"),
    Videos(2, "Titulo 2", "Descricao 2", "https://qualquer2"),
]


@api_view(["GET"])
def videos_list_create(request):

    if request.method == "GET":

        data = [asdict(l) for l in videos_lista]

        return Response(data=data)
