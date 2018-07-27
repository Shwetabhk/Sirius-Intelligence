from rest_framework import serializers
from songplayer.models import Song,Album,Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('artist_name','genre')


class AlbumSerializer(serializers.ModelSerializer):
    artist_id=ArtistSerializer()
    class Meta:
        model=Album
        fields=('id','album_name','artist_id','image')

class SongSerializer(serializers.ModelSerializer):
    album_id=AlbumSerializer()
    class Meta:
        model=Song
        fields=('id','name','target','album_id')
