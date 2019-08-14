<<<<<<< HEAD
from .models import Account
from Accounts.serializer import AccountsSerializer, OwnerSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from Accounts.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework import viewsets

<<<<<<< HEAD
class AccountsViewSet(viewsets.ModelViewSet):
=======
"""
list all accounts or creates a new account
"""
=======
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
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
>>>>>>> fc52c12f4c0514a995a6a66629f42e40204c774f

# This viewset automatically provides list, create, retrieve,update and destroy actions for accounts.

<<<<<<< HEAD
=======
class AccountsList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


""" 
Retrieve , update or delete account
"""
=======



# Retrieve , update or delete account

>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
>>>>>>> fc52c12f4c0514a995a6a66629f42e40204c774f
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
=======
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
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
