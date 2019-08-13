from .models import Account
from Accounts.serializer import AccountsSerializer, OwnerSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from Accounts.permissions import IsOwnerOrReadOnly

"""
list all accounts or creates a new account
"""


class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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