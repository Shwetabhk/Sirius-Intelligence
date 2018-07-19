from django.shortcuts import render
from songplayer.models import Song
from django.http import HttpResponse
from django.core import serializers
import json


def songs(request):
    if request.method=="GET":
        songs=Song.objects.all()
        result=serializers.serialize('json',songs)
        print(result)
        return HttpResponse(result.encode("utf-8"))
