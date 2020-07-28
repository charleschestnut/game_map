from mapa.models import *
from django.db.models import Q

MAP_NAME = "Second map"
ROW_NUMBER = 5
COL_NUMBER = 4
CH_PS_X = 0
CH_PS_Y = 2


def get_axis_position(x, y):
    filter = Q(x_axis=x) & Q(y_axis=y)
    return AxisPosition.objects.get(filter)


def populate_map_2(walls):

    def create_map_2():
        map = MapGame.objects.create(
            name=MAP_NAME,
            row=ROW_NUMBER,
            col=COL_NUMBER)
        map.save()

    def create_map_squares_2():
        mapgame_id = MapGame.objects.get(name=MAP_NAME).id
        print(mapgame_id)
        wall_list = [
            walls[5],
            walls[9],
            walls[1],
            walls[8],
            walls[12],
            walls[0],
            walls[4],
            walls[9],
            walls[5],
            walls[2],
            walls[1],
            walls[8],
            walls[13],
            walls[6],
            walls[8]]
        map_square_list = []
        counter = 0
        # Creation of NO-GAME squares
        for position in range(ROW_NUMBER*COL_NUMBER):
            if position in [0, 3, 4, 7, 19]:
                map_square = MapSquare.objects.create(
                    base_square=BaseSquare.objects.get(type__exact='NO-GAME'),
                    axis_position=get_axis_position(int(position % ROW_NUMBER), int(position / COL_NUMBER)),
                    map_id=mapgame_id)
                map_square.save()
                map_square_list.append(map_square)

            else:
                filter = Q(walls=wall_list[counter]) & Q(type='NORMAL')
                map_square = MapSquare.objects.create(
                    base_square=BaseSquare.objects.get(filter),
                    axis_position=get_axis_position(int(position % COL_NUMBER), int(position / COL_NUMBER)),
                    map_id=mapgame_id)
                counter += 1
                print(map_square.base_square.walls, map_square.axis_position.x_axis, map_square.axis_position.y_axis)
                map_square.save()
                map_square_list.append(map_square)

    def create_character_position_2():
        axis_filter = Q(map__name__exact=MAP_NAME) & Q(axis_position__x_axis=CH_PS_X) & Q(axis_position__y_axis=CH_PS_Y)
        map_square = MapSquare.objects.get(axis_filter)
        character_position = CharacterPosition.objects.create(
            map_square_id=map_square.id
        )
        character_position.save()

    create_map_2()
    create_map_squares_2()
    create_character_position_2()
