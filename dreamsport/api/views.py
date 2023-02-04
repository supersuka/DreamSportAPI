from rest_framework import generics

from api.models import Workouts
from api.serializers import TrainSerializer


# Create your views here.
class WorkoutsView(generics.ListAPIView):
    queryset = Workouts.objects.all()
    serializer_class = TrainSerializer