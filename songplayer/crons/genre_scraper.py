from django_cron import CronJobBase,Schedule
from songplayer.models import Artist
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


class GenreScraper(CronJobBase):
    RUN_EVERY_MINS=1
    schedule=Schedule(run_every_mins=RUN_EVERY_MINS)
    code='songplayer.genre'
    def do(self):
        artists=Artist.objects.all()
        for i in artists:
            search_item="_".join(i.artist_name.split())
            print(search_item)
            try:
                url="https://en.wikipedia.org/wiki/{name}_(band)".format(name=search_item)
                print(url)
                html = urlopen(url)
            except:
                url="https://en.wikipedia.org/wiki/{name}".format(name=search_item)
                print(url)
                html = urlopen(url)
            soup = bs(html, 'lxml')
            table=soup.find_all('table')[0]
            try:
                ul=table.find_all("ul")[0]
                li=ul.find_all("li")
                genres=[]
                for i in li:
                    genres.append(i.text.title())
                print(genres)
            except:
                print ()
