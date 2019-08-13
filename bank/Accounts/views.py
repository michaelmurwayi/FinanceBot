from Accounts.models import Account
from Accounts.serializer import AccountsSerializer
from rest_framework import generics


class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

from Accounts.models import Account
from Accounts.serializer import AccountsSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from Accounts.serializer import UserSerializer


class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer