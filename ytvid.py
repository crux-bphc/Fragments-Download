import pafy
import asyncio
from downloaderOOP import *


class ytvideo(object):
    def __init__(self, url, path):
        self.baseurl = url
        self.path = path
        self.streamNumber = None   # None will default to best available
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

    def printStreams(self):
        for i in range(len(self.obj.allstreams)):
            print("%d " % (i) + str(self.obj.allstreams[i]))

    def setStream(self, streamNumber):
        self.streamNumber = streamNumber

    async def download(self, music=False):
        if self.streamNumber:
            downlink = self.obj.allstreams[self.streamNumber]
            downloader = downloadUrl(
                downlink.url, self.path,
                downlink.title + "." + downlink.extension)
        else:
            downlink = self.obj.getbest()
            if music:
                downlink = self.obj.getbestaudio()
                downloader = downloadUrl(
                    downlink.url, self.path,
                    downlink.title + "." + downlink.extension)
            else:
                downloader = downloadUrl(
                    downlink.url, self.path,
                    downlink.title + "." + downlink.extension)
        await downloader.sendHead()
        downloader.setDefaultFraglist()
        await downloader.downloadAllFrags()

    def sendStreams(self):
        return self.obj.allstreams
