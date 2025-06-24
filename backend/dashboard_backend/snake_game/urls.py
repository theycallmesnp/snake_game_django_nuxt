from django.urls import path
from .views import SnakeGameScoreListCreateView

urlpatterns = [
    path('scores/', SnakeGameScoreListCreateView.as_view(), name='snakegame-scores'),
]