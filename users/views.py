from django.shortcuts import render
from users.models import User
from django.http import HttpResponse
from django.core import serializers
import json


def user(request):
    if request.method=="GET":
        users=User.object.all()
        result=serializers.serialize('json',users)
        return HttpResponse(result)
