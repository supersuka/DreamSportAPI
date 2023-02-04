from django.urls import path

from api.views import TrainsView

api_v1 = [
    path('v1/trains/all', TrainsView.as_view())
]
