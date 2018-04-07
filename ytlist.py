import pafy
from ytvid import *


class ytlist(object):
    def __init__(self, url=None):
        self.url = url
        self.obj = pafy.get_playlist(self.url)
        self.videos = []

    def populateVideoList(self):
        for i in range(len(self.obj['items'])):
            self.videos.append(self.obj['items'][i]['pafy'].getbest().url)
        return self.videos
