from mapa.models import MapSquare, WALLS_VALUES, MapGame
from django.db.models import Q


def next_axis_position(direction, map_square):
    axis_position = map_square.axis_position
    if direction == WALLS_VALUES['L'] or direction == WALLS_VALUES['R'] or \
            direction == WALLS_VALUES['T'] or direction == WALLS_VALUES['B']:

        if direction == WALLS_VALUES['L']:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis - 1) & \
                            Q(axis_position__y_axis=axis_position.y_axis)

        elif direction == WALLS_VALUES['R']:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis + 1) & \
                            Q(axis_position__y_axis=axis_position.y_axis)

        elif direction == WALLS_VALUES['T']:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis) & \
                            Q(axis_position__y_axis=axis_position.y_axis + 1)

        else:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis) & \
                            Q(axis_position__y_axis=axis_position.y_axis - 1)

        map_game = MapGame.objects.get(id=map_square.map_id)
        map_square_2 = MapSquare.objects.all().filter(map__name__exact=map_game.name).filter(filter_square)[0]

        return map_square_2
    else:
        print('Wrong direction movement. Only can be: L, R, T, B')
