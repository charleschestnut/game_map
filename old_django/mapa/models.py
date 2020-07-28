from django.db import models
from colorfield.fields import ColorField
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

WALLS_VALUES = {'L': 'L',
                'R': 'R',
                'T': 'T',
                'B': 'B'}

SQUARE_CHOICES = {
    'NORMAL': 'NORMAL',
    'NO-GAME': 'NO-GAME',
    'START': 'START',
    'FINISH': 'FINISH',
    'MONSTER': 'MONSTER',
    'TREASURE': 'TREASURE',
    'TELEPORTAL': 'TELEPORT', }


class AxisPosition(models.Model):
    x_axis = models.PositiveIntegerField(null=False,
                                         blank=False,
                                         default=0)
    y_axis = models.PositiveIntegerField(null=False,
                                         blank=False,
                                         default=0)

    def __str__(self):
        return '['+str(self.x_axis)+','+str(self.y_axis)+']'


class BaseSquare(models.Model):
    walls = ArrayField(
        models.CharField(max_length=1,
                         blank=True),
        size=4, )
    type = models.CharField(max_length=20,
                            null=False,
                            blank=False)
    noGameColor = ColorField(default='#FF0000')

    def __str__(self):
        if self.type == SQUARE_CHOICES['NORMAL']:
            return str(self.walls)
        else:
            return self.type


class MapGame(models.Model):
    name = models.CharField(max_length=50,
                            unique=True)
    col = models.PositiveIntegerField(
        default=2,
        validators=[MinValueValidator(0),
                    MaxValueValidator(20)])
    row = models.PositiveIntegerField(
        default=2,
        validators=[MinValueValidator(0),
                    MaxValueValidator(20)])

    def __str__(self):
        return self.name+' '+str(self.row)+'x'+str(self.col)


class MapSquare(models.Model):
    base_square = models.ForeignKey(BaseSquare, on_delete=models.CASCADE)
    axis_position = models.ForeignKey(AxisPosition, on_delete=models.CASCADE)
    map = models.ForeignKey(MapGame, on_delete=models.CASCADE, related_name='squares')

    def __str__(self):
        return self.map.name+' - '+str(self.axis_position)


class CharacterPosition(models.Model):
    map_square = models.ForeignKey(MapSquare, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.map_square)
# class MatrixMap(models.Model):
#    map = models.ForeignKey(MapGame, on_delete=models.CASCADE)

# class RowMap(models.Model):
#    matrix = models.ForeignKey(MatrixMap, on_delete=models.CASCADE)


class Teleportal(models.Model):
    portal_connection = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
