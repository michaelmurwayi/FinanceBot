from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User


<<<<<<< HEAD

class AccountsSerializer(serializers.ModelSerializer):
=======
class AccountsSerializer(serializers.HyperlinkedModelSerializer):
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
    """
    defines fields to be serialized
    """
    class Meta:
        model = Account
        fields = ['id','first_name', 'second_name', 'account_name', 'account_number', 'account_type', 'branch_name', 'phonenumber']

 
    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        
<<<<<<< HEAD
        return Accounts.objects.create(**validated_data)
=======
        return Account.objects.create(**validated_data)
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.account_name = validated_data.get('account_name', instance.account_name)
        instance.account_number = validated_data.get('account_number', instance.account_number)
        instance.account_type= validated_data.get('account_type', instance.account_type)
        instance.branch_name= validated_data.get('branch_name', instance.branch_name)
        instance.phonenumber= validated_data.get('phonenumber', instance.phonenumber)
<<<<<<< HEAD
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'users']
=======
        owner = serializers.ReadOnlyField(source='owner.username')
        instance.save()
        return instance


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=True,view_name= 'Owner-list', queryset= User.objects.all())
   
    class Meta:
        model = User
        fields = ['id', 'username', 'owner']
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
