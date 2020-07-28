from mapa.models import CharacterPosition, SQUARE_CHOICES
from mapa.views.movement.next_axis_position import next_axis_position


def movement_in_game(character_position_id, direction='NO-DIRECTION'):
    character_position = CharacterPosition.objects.get(id=int(character_position_id))
    print('Start Character position:' + str(character_position.map_square.axis_position))
    if direction == 'NO-DIRECTION':
        if character_position:
            print("The position of your character is: " + str(character_position.map_square.axis_position))
        else:
            print("Please, insert the character position ID")

    if direction in character_position.map_square.base_square.walls:
        print('Not possible to cross the square because there is a wall. Choose another direction')
        print('The walls are in: ' + str(character_position.map_square.base_square.walls))

    else:
        next_map_square = next_axis_position(direction, character_position.map_square)

        if next_map_square and (next_map_square.base_square.type != SQUARE_CHOICES['NO-GAME'] or
                                next_map_square.base_square.type != SQUARE_CHOICES['START']):
            character_position.map_square = next_map_square
            character_position.save()
            print('The new position is: [' + str(character_position.map_square.axis_position.x_axis) + ','
                  + str(character_position.map_square.axis_position.y_axis) + '].')
            print('The new walls are in: ' + str(character_position.map_square.base_square.walls))
        else:
            print("You can't cross, this is not a valid position.")
