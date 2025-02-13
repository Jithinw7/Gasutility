from rest_framework import serializers
from .models import ServiceRequest, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','email', 'phone_number']

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['id','customer','request_type','details','attachment','status', 'submitted_date','resolved_date']