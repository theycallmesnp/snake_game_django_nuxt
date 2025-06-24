from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import SnakeGameScore
from .serializers import SnakeGameScoreSerializer

class SnakeGameScoreListCreateView(generics.ListCreateAPIView):
    serializer_class = SnakeGameScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return SnakeGameScore.objects.filter(user=user).order_by('-score')
        else:
            return SnakeGameScore.objects.all().order_by('-score')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)