from django.urls import path

from . import views

urlpatterns = [
    # minesweeper game
    path('', views.welcome, name='welcome'),

    # minesweeper game
    path('game/', views.game, name='game'),

    # score board
    path('leaderboard/', views.leader_board, name='score_board'),
]
