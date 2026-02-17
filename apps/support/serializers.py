from rest_framework import serializers

from apps.core.serializers import CustomerSerializer, TechnicianSerializer
from apps.support.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['customer'] = CustomerSerializer(instance.customer).data

        # Solo lo que necesitas (Más ligero y rápido)
        # response['customer'] = {
        #     "id": instance.customer.id,
        #     "name": f"{instance.customer.first_name} {instance.customer.last_name}",
        #     "email": instance.customer.email
        # }

        if instance.technical:
            response['technical'] = TechnicianSerializer(instance.technical).data

        return response
