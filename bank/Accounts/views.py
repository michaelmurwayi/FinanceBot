<<<<<<< HEAD
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
=======
from .models import Account
from Accounts.serializer import AccountsSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


# list all accounts or creates a new account


class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer



# Retrieve , update or delete account

>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
<<<<<<< HEAD
=======
   


# retrieve list of users in the db

>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


<<<<<<< HEAD
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
=======

# retrieve individual user account



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
