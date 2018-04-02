import pafy
import asyncio, aiohttp
from downloaderOOP import *
class ytvideo(object):
    def __init__(self,url):
        self.baseurl=url
        self.streamNumber=None   ## None will default to best available ##
        try:
            self.obj=pafy.new(self.baseurl)
        except:
            print("Error getting downloadable urls.Check your url and internet connection")
            exit(1)
        self.title=self.obj.title+"."+self.obj.getbest().extension
        print(self.title)
        
    def __str__(self):
        print(self.obj)

    def printStreams(self):
        for i in range(len(self.obj.allstreams)):
            print("%d "%(i)+str(self.obj.allstreams[i]))

    def setStream(self,streamNumber):
        self.streamNumber=streamNumber

    async def download(self,music=False):
        if self.streamNumber:
            downurl=self.obj.allstreams[self.streamNumber].url
        else:
            downstream=self.obj.getbest()
            if music:
                downstream=self.obj.getbestaudio()
                download=downloadUrl(downstream.url,downstream.title+"."+downstream.extension)
            else:
                download=downloadUrl(downstream.url,downstream.title+"."+downstream.extension)
        await download.sendHead()
        download.setDefaultFraglist()
        await download.downloadAllFrags()

if __name__ == '__main__':
    y = ytvideo('https://www.youtube.com/watch?v=QwievZ1Tx-8')
    event = asyncio.get_event_loop()
    event.run_until_complete(y.download())
  
