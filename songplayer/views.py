from django.shortcuts import render
from django.http import JsonResponse
from songplayer.models import Song,Artist,Genre,Album
from songplayer.serializers import SongSerializer,GenreSerializer,AlbumSerializer,ArtistSerializer
import json


def songs(request):
    if request.method=="GET":
        songs=Song.objects.order_by('name').all()
        result=SongSerializer(songs,many=True)
        return JsonResponse(result.data,safe=False)

def genres(request):
    if request.method=="GET":
        genres=Genre.objects.all()
        result=GenreSerializer(genres,many=True)
        return JsonResponse(result.data,safe=False)

def albums(request):
    if request.method=="GET":
        albums=Album.objects.order_by('album_name').all()
        result=AlbumSerializer(albums,many=True)
        return JsonResponse(result.data,safe=False)

def artists(request):
    if request.method=="GET":
        artists=Artist.objects.order_by('artist_name').all()
        result=ArtistSerializer(artists,many=True)
        return JsonResponse(result.data,safe=False)

def search(request):
    if request.method=="GET":
        songs=Song.objects.filter(name__icontains="oo").all()
        result=SongSerializer(songs,many=True)
        return  JsonResponse(result.data,safe=False)