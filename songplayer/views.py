from django.shortcuts import render
from django.http import JsonResponse
from songplayer.models import Song,Artist,Genre
from songplayer.serializers import SongSerializer,GenreSerializer
import json


def songs(request):
    if request.method=="GET":
        songs=Song.objects.order_by('album_id').all()
        result=SongSerializer(songs,many=True)
        return JsonResponse(result.data,safe=False)

def artists(request):
    if request.method=="GET":
        artists=Artist.objects.first()
        genre1=Genre.objects.filter(artist__id=artists.id).all()
        result=GenreSerializer(genre1,many=True)
        return JsonResponse(result.data,safe=False)
