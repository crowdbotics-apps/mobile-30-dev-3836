from rest_framework import authentication
from rfdg.models import SFff
from .serializers import SFffSerializer
from rest_framework import viewsets


class SFffViewSet(viewsets.ModelViewSet):
    serializer_class = SFffSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SFff.objects.all()
