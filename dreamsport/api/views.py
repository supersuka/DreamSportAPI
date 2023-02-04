from rest_framework import generics

from api.models import Trains
from api.serializers import TrainSerializer


# Create your views here.
class TrainsView(generics.ListAPIView):
    queryset = Trains.objects.all()
    serializer_class = TrainSerializer