from django.urls import path

from api.views import WorkoutsView

api_v1 = [
    path('v1/workouts/all', WorkoutsView.as_view())
]
