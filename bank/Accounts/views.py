from .models import Account
from Accounts.serializer import AccountsSerializer, OwnerSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from Accounts.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework import viewsets

class AccountsViewSet(viewsets.ModelViewSet):

    # This viewset automatically provides list, create, retrieve,update and destroy actions for accounts.
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

class OwnersViewSet(viewsets.ReadOnlyModelViewSet):
    #  This viewset automatically provides owners list and owners detail actions.

    queryset = User.objects.all()
    serializer_class = OwnerSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Accounts': reverse('Accounts-list', request=request, format=format),
        'Owners': reverse('Owners-list', request=request, format=format)
    })
