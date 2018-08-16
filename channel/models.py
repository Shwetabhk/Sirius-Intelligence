from django.db import models


class Channel(models.Model):
    subscriber_id = models.EmailField(null=False,unique=True)
    subscriber_name = models.CharField(max_length=40,null=True,)
    channel_secrets = models.CharField(max_length=150,null=False)
    channel_type = models.IntegerField(null=False)  # 1-Google, 2-Facebook 
