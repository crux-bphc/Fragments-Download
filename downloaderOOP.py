### Import Libraries ###
import aiohttp
import asyncio
import sys,os,time
### Import Files ###
import utils

class downloadUrl(object):
    def __init__(self,url,title=None):
        self.url=url
        self.byteAllow=None
        self.headers=None
        self.frags=8
        self.title=utils.removeSlash(title)
        self.length=None
        self.done=False
        self.percent=None
        self.session=None
        self.fraglist=None
        self.fragsize=[-1 for i in range(self.frags)]
        self.donesize=[0 for i in range(self.frags)]
        if not self.title:
            self.title=url.split('/')[-1]
            print("title set to "+self.title)
        if "youtube" in self.url or "youtu.be" in self.url:
            self.isTube=True
        else:
            self.isTube=False
        

    def setFrags(self,frags):
        if frags<2 or frags>32:
            print("WARNING: fragments must be between 2 to 32 defaulting to 5")
            
        self.frags=frags
    def __str__(self):
        return str("url: "+self.url)

    async def sendHead(self):
        print("sending Head request")
        async with aiohttp.ClientSession() as self.session:
            async with self.session.head(self.url) as response:
                pass
        print(response)
        if response.status==200 and 'Content-Length' in response.headers:
            print("OK 200")
            self.headers=response.headers
            self.length=int(self.headers['Content-Length'])
            print("length: "+str(self.length))
            assert self.length>0,"Something went wrong"

            if self.headers['Accept-Ranges']=='bytes':
                self.byteAllow=True
            else:
                self.byteAllow=False
        elif response.status>300 and response.status<309:
            print(str(response.status_code)+" "+response.reason)
            print("Trying to follow redirection to %s"%(response.headers['Location']))
            self.url=response.headers['Location']
            self.sendHead()
        else:
            print(str(response.status_code)+"received"+response.reason)
            self.byteAllow=False
            self.headers=response.headers
            self.length=False
    async def downloadOld(self):
        chunk=16*1024    ### Chunk size = 1 kilobyte ###
        ###  Prepare request
        sendheaders={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=headers) as resp:
                print("starting download for frag %d\n" % (num))
                chunk=1024
                fp=open(self.title+".frag"+str(num),"ab")
                while(True):
                    cnk=await resp.content.read(chunk);
                    if not cnk:
                        break
                    fp.write(cnk)
                fp.close()
        self.done=True
        print()
        print("done!")

    async def downloadFrag(self,start,end,num):
        fname=self.title+".frag"+str(num)
        self.fragsize[num]=end-start+1
        if os.access(fname,os.F_OK):
            start+=os.stat(fname).st_size
            self.donesize[num]=os.stat(fname).st_size
            assert start-1<=end,"Looks like a problem to me start is greater than or equal to end. Cannot resume!"
            if start==end+1:
                return;
            print("Download for %d fragment will resume from %d" % (num,start))
        sendheaders={'Range':'bytes=%d-%d'%(start,end),'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=sendheaders) as resp:
                print("starting download for frag %d\n" % (num))
                chunk=16*1024
                fp=open(self.title+".frag"+str(num),"ab")
                while(True):
                    cnk=await resp.content.read(chunk);
                    if not cnk:
                        break
                    fp.write(cnk)
                    self.donesize[num]+=len(cnk)
                fp.close()
                print("finished download for frag %d\n" % (num))

    def setDefaultFraglist(self):
        assert (int(self.length)>0),"Your download file kinda sucks"
        assert (self.frags>1),"Alri8 you're an idiot. :p"
        self.fraglist=[]
        self.fraglist.append((0,int((self.length-1)*(float(1)/self.frags))));
        for i in range(1,self.frags):
            self.fraglist.append((self.fraglist[-1][1]+1,int((self.length-1)*(float(i+1)/self.frags))))    
        ##print("Debug: "+str(self.fraglist))
        
    async def downloadAllFrags(self):
        if self.length==False or self.byteAllow==False:
            print("Can not download by fragments.")
            print("Falling back to old download style.")
            self.downloadOld()
            return;
        else:
            self.setDefaultFraglist()
            if os.access(self.title,os.F_OK) and (os.stat(self.title).st_size * 1024)>=self.length:
                print("looks like file is downloaded already")
                return;
            print("downloading "+'%.2f'%(self.length/(1024*1024.0))+" MB");
            threadlist=[self.downloadFrag(self.fraglist[i][0], self.fraglist[i][1], i) for i in range(self.frags)]
            #threadlist.append(self.generateProgressBar())
            await asyncio.gather(*threadlist)
            print()
            print("done downloading")
            print("Starting to merge %d files"%(self.frags))
            utils.catAll(self.title,self.frags)
            print()
            sys.exit(0)
            
    '''def generateProgressBar(self):
        sleepTime=0.5         ### in seconds(Using variable to manage speeds ###
        prevDoneSize=0
        while True:
            #print(str(self.donesize)+str(self.fragsize))
            curDoneSize=sum(self.donesize)
            utils.printProgressBar(curDoneSize*100.0/self.length,speed=(curDoneSize-prevDoneSize)/sleepTime/1024)
            if self.donesize==self.fragsize:
                break
            time.sleep(sleepTime)
            prevDoneSize=curDoneSize'''

if __name__=='__main__':
    d = downloadUrl('https://s3.amazonaws.com/scschoolfiles/112/j-r-r-tolkien-lord-of-the-rings-01-the-fellowship-of-the-ring-retail-pdf.pdf', None)
    event = asyncio.get_event_loop()
    event.run_until_complete(d.downloadAllFrags())
