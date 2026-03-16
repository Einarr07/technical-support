from rest_framework import serializers

from apps.core.models import Customer, Technician


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    # def validate_email(self, value):
    #     if not value.endswith('@example.com'):
    #         raise serializers.ValidationError('Email address is not valid. The email must end with "@example.com".')
    #
    #     return value


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
