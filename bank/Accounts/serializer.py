from rest_framework import serializers
from Accounts.models import Accounts
from django.contrib.auth.models import User



class AccountsSerializer(serializers.ModelSerializer):
    """
    defines fields to be serialized
    """
    class Meta:
        model = Accounts
        fields = ['id','first_name', 'second_name', 'account_name', 'account_number', 'account_type', 'branch_name', 'phonenumber']

 
    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        import pdb; pdb.set_trace()
        return Accounts.objects.create(**validated_data)

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
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=Accounts.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'users']