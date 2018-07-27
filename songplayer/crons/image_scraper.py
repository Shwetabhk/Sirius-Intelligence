from django_cron import CronJobBase,Schedule
from songplayer.models import Artist,Album
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
from songplayer.util.images_download import googleimagesdownload  #importing the library

class ImageScraper(CronJobBase):
    RUN_EVERY_MINS=1
    schedule=Schedule(run_every_mins=RUN_EVERY_MINS)
    code="songplayer.wiki"
    def do(self):
        album=Album.objects.all()
        for i in album:
            flag=0
            artist=Artist.objects.filter(id=i.artist_id.id).first()
            artist_name=artist.artist_name
            album_name=i.album_name
            # artist_name="_".join(artist_name.split())
            # album_name="_".join(album_name.split())
            # url="https://www.google.co.in/search?q={name}&source=lnms&tbm=isch&tbs=isz:m".format(name=album_name+"+"+artist_name)
            # print(url)
            # soup = bs(requests.get(url).text, 'lxml')
            # images=soup.find_all('img')
            # for j in images:
            #     html=urlopen(j["src"])
            #     soup2=bs(html,"lxml")
            #     image=soup.find_all("img")
            #     for k in image:
            #         print(k["src"])
            #         i.image=k["src"]
            response = googleimagesdownload()   #class instantiation
            arguments = {"keywords":album_name+" "+artist_name,"limit":1,"print_urls":True}   #creating list of arguments
            paths,url = response.download(arguments)   #passing the arguments to the function
            i.image=url
            i.save(update_fields=["image"])
