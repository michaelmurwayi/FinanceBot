from .models import Records
from .serializer import RecordSerializer
from rest_framework import mixins
from rest_framework import generics

class ListRecords(generics.ListCreateAPIView):
    
    """ list all transaction records adn post new records """

    queryset= Records.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer
