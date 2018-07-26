from django.shortcuts import render
from django.http import HttpResponse
from songplayer.models import Song
from songplayer.serializers import SongSerializer
import json


def songs(request):
    if request.method=="GET":
        songs=Song.objects.order_by('album_id').all()
        result=SongSerializer(songs,many=True)
        print(result.data)
        return HttpResponse(json.dumps(result.data))
