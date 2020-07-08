from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Dynasty
from .serializers import DynastySerializer
from .filters.in_ import InFilterSet


class DynastyView(ModelViewSet):
    queryset = Dynasty.objects.all()
    serializer_class = DynastySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InFilterSet
