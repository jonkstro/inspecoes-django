from rest_framework.viewsets import ModelViewSet

from plataforma.api.serializers import PlanoManutSerializer
from plataforma.models import PlanoManut


class PlanoManutViewset(ModelViewSet):
    serializer_class = PlanoManutSerializer
    def get_queryset(self):
        return PlanoManut.objects.all()