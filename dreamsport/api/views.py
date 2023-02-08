from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Workouts, Exercise
from api.serializers import WorkoutsSerializer


class WorkoutsView(generics.ListAPIView):
    queryset = Workouts.objects.all()
    serializer_class = WorkoutsSerializer


class ExerciseView(APIView):
    def get(self, request):
        exercise = Exercise.objects.all().values()
        return Response(list(exercise))