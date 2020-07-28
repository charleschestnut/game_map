from mapa.models import WALLS_VALUES
from mapa.views.movement.next_axis_position import next_axis_position


def get_oposite_direction(dir):
    if dir == 'L':
        return 'R'
    elif dir == 'R':
        return 'L'
    elif dir == 'T':
        return 'B'
    elif dir == 'B':
        return 'T'
    else:
        return None


def calc_directions(map_square, direction):
    walls = map_square.base_square.walls
    oposite_direction = get_oposite_direction(direction)
    directions = list(set(WALLS_VALUES.values()) - set(walls))
    if len(directions) > 1:
        directions.remove(oposite_direction)
    return directions


def get_map_squares_availables(map_square, dice_number, direction, positions=[]):
    if direction is not None:
        map_square = next_axis_position(direction, map_square)

        if dice_number == 0:
            positions.append(map_square)

        else:
            dice_number -= 1
            directions = calc_directions(map_square, direction)
            for direction_value in directions:
                get_map_squares_availables(map_square, dice_number, direction_value, positions)
    else:
        dice_number -= 1
        directions = calc_directions(map_square, direction)
        for direction_value in directions:
            get_map_squares_availables(map_square, dice_number,
                                      direction_value, positions)
    return list(set(positions))
