from django.contrib import admin

from .models import Workouts, Exercise, ExercisePhotos, Approach

admin.site.register(Workouts)
admin.site.register(Exercise)
admin.site.register(ExercisePhotos)
admin.site.register(Approach)