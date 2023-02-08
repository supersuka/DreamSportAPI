from django.urls import path

from api.views import WorkoutsView, ExerciseView

api_v1 = [
    path('v1/workouts/all', WorkoutsView.as_view()),
    path('v1/exercise/all', ExerciseView.as_view())
]
