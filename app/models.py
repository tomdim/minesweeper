from django.db import models
from django.contrib.auth.models import User

from .lists import *


class Game(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    level = models.CharField(max_length=10, choices=GAME_LEVELS, blank=True, null=True)
    status = models.CharField(max_length=10, choices=GAME_STATUSES, blank=True, null=True, default=None)

    bombs_flagged = models.IntegerField(blank=True, null=True, default=0)
    time_elapsed = models.IntegerField(blank=True, null=True, default=0)
    score = models.IntegerField(blank=True, null=True, default=0)

    started = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now=True)

