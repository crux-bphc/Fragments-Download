import pafy
import asyncio
from downloaderOOP import *


class YtVideo(object):
    def __init__(self, url, path):
        self.baseurl = url
        self.path = path
        self.frags = 8
        self.streamnumber = None   # None will default to best available
        try:
            self.obj = pafy.new(self.baseurl)
        except:
            print(
                "Error getting urls.Check your url and internet connection")
            exit(1)
        self.title = self.obj.title + "." + self.obj.getbest().extension
        print(self.title)

    def __str__(self):
        print(self.obj)

    def printstreams(self):
        for i in range(len(self.obj.allstreams)):
            print("%d " % (i) + str(self.obj.allstreams[i]))

    def setstream(self, streamNumber):
        self.streamnumber = streamNumber

    def setfrags(self, frags):
        self.frags = frags

    async def download(self, music=False):
        if self.streamnumber:
            downlink = self.obj.allstreams[self.streamnumber]
            downloader = DownloadUrl(
                downlink.url, self.path,
                downlink.title + "." + downlink.extension)
        else:
            downlink = self.obj.getbest()
            if music:
                downlink = self.obj.getbestaudio()
                downloader = DownloadUrl(
                    downlink.url, self.path,
                    downlink.title + "." + downlink.extension)
            else:
                downloader = DownloadUrl(
                    downlink.url, self.path,
                    downlink.title + "." + downlink.extension)
        downloader.setfrags(self.frags)
        await downloader.sendhead()
        downloader.setdefaultfraglist()
        await downloader.downloadallfrags()

    def sendstreams(self):
        return self.obj.allstreams
