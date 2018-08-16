__author__ = "shwetabhk "


'''This file contains all the secrets such as database passwords, api keys, authentication file links, etc'''

class Secrets:

#########DATABASE SECRETS##########

    ENGINE = 'django.db.backends.postgresql'
    NAME = 'siriusmusic'
    USER = 'sirius'
    PASSWORD = 'sirius_black'
    HOST = 'localhost'
    PORT = 5432


########YOUTUBE API KEY############

    YOUTUBE_API_KEY='AIzaSyCrF_IsqWkWcMG3rlxOVCWs87Re7_xlU7A'

#######SONG DIRECTORY##############

    SONG_DIRECTORY='/home/shwetabh/Workspace/SiriusIntelligence/Music'
