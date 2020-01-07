from django.urls import path

from . import views

urlpatterns = [
    # entry page
    path('', views.welcome, name='welcome'),

    # minesweeper game
    path('game/', views.game, name='game'),

    # score board
    path('scoreboard/', views.score_board, name='score_board'),
]
