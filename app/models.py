from django.db import models
from django.contrib.auth.models import User

from .lists import GAME_STATUSES


class Game(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    status = models.CharField(max_length=10, choices=GAME_STATUSES, blank=True, null=True)
    bombs_revealed = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True, db_index=True)

    time_elapsed = models.IntegerField(blank=True, null=True)
    started = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now=True)

