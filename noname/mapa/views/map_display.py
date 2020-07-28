from django.shortcuts import render, redirect
from mapa.models import MapGame

def map_display(request, id):
    map = MapGame.objects.get(id=int(id))
