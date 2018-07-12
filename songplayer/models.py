from django.db import models


class Artist(models.Model):
    artist_name=models.CharField(null=False,max_length=100)
    genre=models.CharField(null=False,max_length=100)


class Album(models.Model):
    album_name=models.CharField(null=False,default='',max_length=100)
    artist_id=models.ForeignKey(Artist, on_delete=models.CASCADE)
    date=models.CharField(null=True,max_length=10)

class Youtube(models.Model):
    link=models.CharField(null=False,max_length=500)
    artist_id=models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    name=models.CharField(null=False,max_length=200)
    target=models.FileField(null=False,max_length=500)
    album_id=models.ForeignKey(Album,null=True,on_delete=models.CASCADE)
