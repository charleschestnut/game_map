from mapa.models import *
from django.db.models import Q

MAP_NAME = "First map"
ROW_NUMBER = 5
COL_NUMBER = 5
CH_PS_X = 1
CH_PS_Y = 1

def get_axis_position(x, y):
    filter = Q(x_axis=x) & Q(y_axis=y)
    return AxisPosition.objects.get(filter)


def populate_map_1(walls):

    def create_map_1():

        map = MapGame.objects.create(
            name=MAP_NAME,
            row=ROW_NUMBER,
            col=COL_NUMBER)
        map.save()

    def create_map_squares_1():

        mapgame_id = MapGame.objects.get(name=MAP_NAME).id
        print(mapgame_id)
        wall_list = [
            walls[12],
            walls[10],
            walls[9],
            walls[5],
            walls[14],
            walls[7],
            walls[6],
            walls[10],
            walls[8]]
        map_square_list = []
        counter = 0
        for position in range(ROW_NUMBER*COL_NUMBER):
            if position in [0, 1, 2, 3, 4, 5, 9, 10, 14, 15, 19, 20, 21, 22, 23, 24]:
                print('nogame', int(position % ROW_NUMBER), int(position / COL_NUMBER))
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

                map_square.save()
                map_square_list.append(map_square)

    def create_character_position_1():
        axis_filter = Q(map__name__exact=MAP_NAME) & Q(axis_position__x_axis=CH_PS_X) & Q(axis_position__y_axis=CH_PS_Y)
        map_square = MapSquare.objects.get(axis_filter)
        character_position = CharacterPosition.objects.create(
            map_square_id=map_square.id
        )
        character_position.save()

    create_map_1()
    create_map_squares_1()
    create_character_position_1()
