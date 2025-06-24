from rest_framework import serializers
from .models import SnakeGameScore

class SnakeGameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeGameScore
        fields = ['id', 'user', 'score', 'date_played']
        read_only_fields = ['id', 'user', 'date_played']