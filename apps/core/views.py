from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.models import Customer, Technician
from apps.core.serializers import CustomerSerializer, TechnicianSerializer


# ---------------------------------------------------------
# URL: /api/customers/
# Maneja la lista completa y la creación
# ---------------------------------------------------------
@api_view(['GET', 'POST'])
def customer_list_view(request):
    # Listar todos
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    # Crear uno nuevo
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ---------------------------------------------------------
# URL: /api/customers/<int:pk>/
# Maneja un solo cliente (Ver, Editar, Borrar)
# ---------------------------------------------------------
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail_view(request, pk):
    # Esto busca el cliente. Si no existe, corta aquí y devuelve 404 automáticamente.
    customer = get_object_or_404(Customer, pk=pk)

    # Ver un cliente
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    # Actualizar un cliente
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Borrar un cliente
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def technician_list_view(request):
    if request.method == 'GET':
        technician = Technician.objects.all()
        serializer = TechnicianSerializer(technician, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TechnicianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
