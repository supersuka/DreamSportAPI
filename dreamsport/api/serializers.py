from rest_framework import serializers

from api.models import Trains


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trains
        fields = "__all__"