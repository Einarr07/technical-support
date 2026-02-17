from django.urls import path

# Importa las dos vistas nuevas
from apps.core.views import customer_list_view, customer_detail_view, technician_list_view

urlpatterns = [
    # 1. URL General: Para listar (GET) y crear (POST)
    path('clientes/', customer_list_view, name='customer_list'),

    # 2. URL de Detalle: Para ver uno (GET), editar (PUT) y borrar (DELETE)
    path('clientes/<int:pk>/', customer_detail_view, name='customer_detail'),
    path('technician/', technician_list_view, name='technician_list'),
]
