from django.contrib.auth.models import User
from django.db.models import Max
from django.shortcuts import render

from .models import Game
from .utils import get_level, create_game


def game(request):
    """
    Initialize Game
    """
    # get user
    user = None
    username = request.POST.get('username', None)
    if username:
        user = User.objects.get_or_create(username=username)

    # get game level
    level = request.POST.get('level')
    level = get_level(level)

    # create game arrays
    bombs, solution = create_game(level[0], level[1], level[2])

    # create Game instance
    game = Game.objects.create(user=user, level=level)

    return render(request, 'minesweeper.html', {'game': game.id, 'user': user, 'bombs': bombs, 'solution': solution})


def leader_board(request):
    """
    Leader board
    """
    # score for a specific level
    level = request.POST.get('level', '1')

    # get the best game score per user
    leaderboard_data = Game.objects.\
        filter(level=level). \
        values('user'). \
        annotate(best_score=Max('score')). \
        order_by('-best_score')

    return render(request, 'leader_board.html', {'leaderboard_data': leaderboard_data})
