from django_cron import CronJobBase, Schedule
from config import Secrets
from songplayer.models import Song,Artist,Album
import os
from mutagen.easyid3 import EasyID3

class SongInfo(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'songplayer.songinfo'

    def do(self):
        path=os.path.abspath(Secrets.SONG_DIRECTORY)
        files=os.listdir(path)
        for file in files:
            try:
                song = EasyID3(path+"/"+file)
                response=song
                artist_obj,exist=Artist.objects.get_or_create(artist_name=response['artist'][0],genre=response['genre'][0])
                album_obj,exist=Album.objects.get_or_create(album_name=response['album'][0],date=response["date"][0][0:4],artist_id=artist_obj)
                obj,exist=Song.objects.get_or_create(name=response['title'][0],target=path+"/"+file,album_id=album_obj)

            except Exception as e:
                print(e)
