from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.support.models import Ticket
from apps.support.permissions import IsTechnical
from apps.support.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    permission_classes = [IsAuthenticated]

    # detail=True meaning than the URL need ID (ej: /tickets/5/resolver/)
    # If was detail=False, be as (ej: /tickets/resueltos/)
    @action(detail=True, methods=['post'], url_path='ticket-solved', permission_classes=[IsAdminUser | IsTechnical])
    def ticket_solved(self, request, pk=None):
        # 1. Get specific ticket
        ticket = self.get_object()

        # 2. Update the status of ticket
        ticket.status = 'RESOLVED'
        ticket.save()

        # 3. Return the answer
        return Response({
            'message': f'The ticket {ticket.code} has been solved.',
            'ticket_code': ticket.code,
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='ticket-unsolved', permission_classes=[IsAdminUser | IsTechnical])
    def ticket_unsolved(self, request, pk=None):
        # 1. Get specific ticket
        ticket = self.get_object()

        # 2. Update the status of ticket
        ticket.status = 'UNSOLVED'
        ticket.save()

        # 3. Return the answer
        return Response({
            'message': f'The ticket {ticket.code} is unsolved.',
            'ticket_code': ticket.code,
        }, status=status.HTTP_200_OK)
