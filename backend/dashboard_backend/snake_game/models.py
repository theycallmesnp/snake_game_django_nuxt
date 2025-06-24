from django.db import models
from authentication.models import User

class SnakeGameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snake_scores')
    score = models.PositiveIntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.score} ({self.date_played.strftime('%Y-%m-%d %H:%M')})"
# Create your models here.
