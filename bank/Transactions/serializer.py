from rest_framework import serializers
from .models import Records
from django.contrib.auth.models import User


class RecordSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	
	class Meta:
		model = Records
		fields= [ "account_name","account_type","branch_name", "phonenumber", "transaction_type", "account_number", "transaction_amount", "owner"]

class AdminSerializer(serializers.HyperlinkedModelSerializer):
	Admin = serializers.PrimaryKeyRelatedField(many=True, queryset=Records.objects.all())

	class Meta :
		model = User
		fields = ['id', 'username', 'Admin']