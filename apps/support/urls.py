from django.urls import path

from apps.support.views import ListTicketsView, DetailTicketView

urlpatterns = [
    path('ticket/', ListTicketsView.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', DetailTicketView.as_view(), name='ticket_detail'),
]
