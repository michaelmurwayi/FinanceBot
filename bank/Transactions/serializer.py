from rest_framework import serializers
from .models import Records

class RecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Records
		fields= [ "account_name","account_type","branch_name", "phonenumber", "transaction_type", "account_number", "transaction_amount"]
