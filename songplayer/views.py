from django.shortcuts import render
from songplayer.models import Song
from django.http import HttpResponse
from songplayer.serializers import SongSerializer
import json


def songs(request):
    if request.method=="GET":
        songs=Song.objects.all()
        result=SongSerializer(songs,many=True)
        print(result.data)
        return HttpResponse(json.dumps(result.data))
