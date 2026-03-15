from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.support.views import ListTicketsView, DetailTicketView
from apps.support.viewsets import TicketViewSet

router = DefaultRouter()

router.register(r'ticket-state', TicketViewSet, basename='ticket-sate')
urlpatterns = [
    path('ticket/', ListTicketsView.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', DetailTicketView.as_view(), name='ticket_detail'),
    path('', include(router.urls)),
]
