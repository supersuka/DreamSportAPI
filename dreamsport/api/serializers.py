from rest_framework import serializers

from api.models import Workouts, Exercise, ExercisePhotos, Approach

class ExercisePhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePhotos
        fields = 'name', "image"

class ExerciseSerializer(serializers.ModelSerializer):
    photos = ExercisePhotosSerializer(many=True, read_only=True)
    class Meta:
        model = Exercise
        fields = "name", "valueType", "countType", "considerOwnWeight", "photos", "created_ad"

class ApproachSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    class Meta:
        model = Approach
        fields = "name", "exercise", "created_ad"

class WorkoutsSerializer(serializers.ModelSerializer):
    approach = ApproachSerializer(many=True, read_only=True)
    class Meta:
        model = Workouts
        fields = "name", "description", "monday", "thuesday", "wednsday", "thursday", "friday", "saturday", "sunday", "approach"

