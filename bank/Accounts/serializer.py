from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User

<<<<<<< HEAD
class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    """

=======

<<<<<<< HEAD

class AccountsSerializer(serializers.ModelSerializer):
=======
<<<<<<< HEAD

class AccountsSerializer(serializers.ModelSerializer):
=======
class AccountsSerializer(serializers.HyperlinkedModelSerializer):
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
    """
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
    defines fields to be serialized
    """
    class Meta:
        model = Account
<<<<<<< HEAD
        fields = ['id','first_name', 'second_name', 'account_name', 'account_number', 'account_type', 'branch_name', 'phonenumber']
=======
<<<<<<< HEAD
        fields = ['id','first_name', 'second_name', 'account_name', 'account_number', 'account_type', 'branch_name', 'phonenumber','owner']
=======
        fields = ['id','first_name', 'second_name', 'account_name', 'account_number', 'account_type', 'branch_name', 'phonenumber']
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b

 
    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        
<<<<<<< HEAD
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Account instance, given the validated data.
=======
<<<<<<< HEAD
        return Account.objects.create(**validated_data)
=======
<<<<<<< HEAD
        return Accounts.objects.create(**validated_data)
=======
        return Account.objects.create(**validated_data)
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.account_name = validated_data.get('account_name', instance.account_name)
        instance.account_number = validated_data.get('account_number', instance.account_number)
        instance.account_type= validated_data.get('account_type', instance.account_type)
        instance.branch_name= validated_data.get('branch_name', instance.branch_name)
        instance.phonenumber= validated_data.get('phonenumber', instance.phonenumber)
<<<<<<< HEAD
=======
<<<<<<< HEAD
        instance.save()
        return instance

    from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Account = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())

    class Meta:
        model = User
        # import pdb; pdb.set_trace()
        fields = ['id', 'username']
=======
<<<<<<< HEAD
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'users']
=======
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
        owner = serializers.ReadOnlyField(source='owner.username')
        instance.save()
        return instance


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
<<<<<<< HEAD
    owner = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
=======
<<<<<<< HEAD
    owner = serializers.HyperlinkedRelatedField(many=True, view_name='Owner-detail', read_only=True)
>>>>>>> fc52c12f4c0514a995a6a66629f42e40204c774f

    class Meta:
        model = User
        fields = ['id', 'username', 'owner']
=======
    owner = serializers.HyperlinkedRelatedField(many=True,view_name= 'Owner-list', queryset= User.objects.all())
   
    class Meta:
        model = User
        fields = ['id', 'username', 'owner']
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
