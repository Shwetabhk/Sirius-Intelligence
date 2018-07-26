from django.db import models


class Artist(models.Model):
    artist_name=models.CharField(null=False,max_length=100)
    genre=models.CharField(null=False,max_length=100)
    image=models.ImageField(null=True)


class Album(models.Model):
    album_name=models.CharField(null=False,default='',max_length=100)
    artist_id=models.ForeignKey(Artist, on_delete=models.CASCADE)
    date=models.CharField(null=True,max_length=10)

class Youtube(models.Model):
    link=models.CharField(null=False,max_length=500)
    artist_id=models.ForeignKey(Artist, on_delete=models.CASCADE)

def get_file_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

#Renaming the image file to truck+(Random Integer)
def upload_file_path(instance,filename):
    print(instance)
    inst=instance.id
    name,ext=get_file_ext(filename)
    return "audio/{name}{ext}".format(name=inst,ext=ext)


class Song(models.Model):
    name=models.CharField(null=False,max_length=200)
    target=models.FileField(upload_to=upload_file_path,null=True,max_length=10000)
    album_id=models.ForeignKey(Album,null=True,on_delete=models.CASCADE)
