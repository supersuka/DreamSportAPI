from rest_framework import serializers

from api.models import Workouts


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workouts
        fields = "name", "description", "monday", "thuesday", "wednsday", "thursday", "friday", "saturday", "sunday", "approach"