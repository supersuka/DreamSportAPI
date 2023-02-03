from django.contrib import admin

from .models import Trains, Exercise, ExercisePhotos, Approach

admin.site.register(Trains)
admin.site.register(Exercise)
admin.site.register(ExercisePhotos)
admin.site.register(Approach)