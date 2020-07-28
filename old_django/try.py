from mapa.models import CharacterPosition
from mapa.views.movement import get_map_squares_availables
from mapa.views.movement import decide_available_square
from mapa.views.throw_dice.throw_dice import throw_dice
from mapa.views.throw_dice.start_turn import  start_turn


c = CharacterPosition.objects.all()[1]
ms = c.map_square

start_turn()
dado = throw_dice()
lista = get_map_squares_availables(ms, dado, None, [])
decided = decide_available_square(lista)
