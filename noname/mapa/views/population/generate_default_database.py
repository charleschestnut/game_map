from mapa.models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from .map_1 import populate_map_1
from .map_2 import populate_map_2


walls = [
    [],
    ['L'],
    ['R'],
    ['T'],
    ['B'],  # 4
    ['L', 'B'],
    ['L', 'T'],  # 6
    ['L', 'R'],
    ['R', 'T'],  # 8
    ['R', 'B'],
    ['T', 'B'],  # 10
    ['L', 'B', 'R'],
    ['L', 'B', 'T'],  # 12
    ['L', 'T', 'R'],
    ['B', 'T', 'R']  # 14
]


def populate(request):

    def create_axis_positions():
        for x in range(5):
            for y in range(5):
                axis = AxisPosition.objects.create(
                    x_axis=x,
                    y_axis=y
                )
                axis.save()

    def create_squares():
        for wall in walls:
            square = BaseSquare.objects.create(
                walls=wall,
                type=SQUARE_CHOICES['NORMAL']
            )
            square.save()
        square_no_game = BaseSquare.objects.create(
            walls=[],
            type=SQUARE_CHOICES['NO-GAME']
        )
        square_no_game.save()

    def create_superuser(username, password):
        User.objects.all().delete()
        superuser = User.objects.create_superuser(
            username=username,
            password=password)
        superuser.save()

    BaseSquare.objects.all().delete()
    MapSquare.objects.all().delete()
    MapGame.objects.all().delete()
    CharacterPosition.objects.all().delete()
    AxisPosition.objects.all().delete()


    create_squares()
    create_superuser('carlos', 'carlos')
    create_axis_positions()

    populate_map_1(walls)
    populate_map_2(walls)
    return render(request, 'populate.html')
