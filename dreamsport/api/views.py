from rest_framework import generics
from rest_framework.views import APIView

from api.models import Workouts, Exercise
from api.serializers import WorkoutsSerializer, ExerciseSerializer


class WorkoutsView(generics.ListAPIView):
    queryset = Workouts.objects.all()
    serializer_class = WorkoutsSerializer


class ExerciseView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer