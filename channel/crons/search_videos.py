import urllib.request
from django_cron import CronJobBase, Schedule
from config import Secrets

class SearchVideos(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'channel.Search_videos'

    def do(self):
        print(self.get_video_links("AvengedSevenfold"))


    @staticmethod
    def get_video_links(query):
        api_key = Secrets.YOUTUBE_API_KEY

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        first_url = base_search_url+'key={}&q={}&part=snippet,id&order=date&maxResults=25'.format(api_key, query)
        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        return video_links
