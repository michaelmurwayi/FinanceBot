from Accounts.models import Account
from Accounts.serializer import AccountsSerializer
from rest_framework import generics


class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

