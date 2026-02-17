from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.support.models import Ticket
from apps.support.serializers import TicketSerializer


class ListTicketsView(ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    # def get(self, request):
    #     tickets = Ticket.objects.all()
    #     serializer = TicketSerializer(tickets, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = TicketSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# El codeigo comentado funciona eredando de APIView
class DetailTicketView(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    # def get(self, request, pk):
    #     ticket = Ticket.objects.get(pk=pk)
    #     serializer = TicketSerializer(ticket)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     ticket = Ticket.objects.get(pk=pk)
    #     serializer = TicketSerializer(ticket, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def delete(self, request, pk):
    #     ticket = Ticket.objects.get(pk=pk)
    #     ticket.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
