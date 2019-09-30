from .models import Records
from .serializer import RecordSerializer, AdminSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions


class RecordViewSet(viewsets.ReadOnlyModelViewSet):

    """ This viewset automatically provides list and details actions"""

    queryset = Records.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdminViewSet(viewsets.ReadOnlyModelViewSet):
    """ This viewset provides list , create , retrieve, update and destroy actions """

    queryset = User.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            'Records': reverse("record-list", request=request, format=format),
            'Admins': reverse("Admin-list", request=request, format=format),
        }
    )