from .models import CovidSymptoms
from rest_framework import serializers

class CovidSymptomsSerializer(serializers.Serializer):
    cough = serializers.FloatField()
    fever = serializers.FloatField()
    breath = serializers.FloatField()
    age = serializers.IntegerField()
    environment = serializers.IntegerField()
    hypertension = serializers.IntegerField()
    diabetes = serializers.IntegerField()
    cardiovascular = serializers.IntegerField()
    respiratory = serializers.IntegerField()
    immune = serializers.IntegerField()

    def create(self, validated_data):
        return CovidSymptoms.objects.create(**validated_data)
