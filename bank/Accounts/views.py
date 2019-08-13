from .models import Account
from Accounts.serializer import AccountsSerializer, OwnerSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from Accounts.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

"""
list all accounts or creates a new account
"""


class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


""" 
Retrieve , update or delete account
"""


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


"""
retrieve list of users in the db
"""


class OwnersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


"""
retrieve individual user account
"""


class OwnerDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer  

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Accounts': reverse('Accounts-list', request=request, format=format),
        'Owners': reverse('Owners-list', request=request, format=format)
    })