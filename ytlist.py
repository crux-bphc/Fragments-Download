import aiohttp, asyncio
from ytvid import *
class ytlist(object):
    async def __init__(self,url=None):
        self.url=url
        self.videos=[]
        if not url==None:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    pass
            if resp.status==200:
                print("OK 200")
                page=resp.read()
                self.page=page
            else:
                print("FOUND %d" % (resp.status))
                ## for now
                exit(1)
            #####       Getting List of Videos      #####
            

    def setVideos(self,page=None):
        if not page==None:
            self.page=page
        soup=BeautifulSoup(self.page,"html.parser")
        anchors=soup.find_all('a',class_="pl-video-title-link")
        for i in anchors:
            self.videos.append("https://youtube.com"+i['href'])
    def downloadPlaylist(self,start=0,end=-1,music=False):
        if end==-1:
            end=len(self.videos)
        for i in range(start,end):
            print("ytlist:: Downloading %d of %d " % (i+1,len(self.videos)))
            current=ytvideo(self.videos[i])
            event = asyncio.get_event_loop()
            event.run_until_complete(current.download(music))
            print("ytlist:: Completed downloading %d" %(i+1))

    
