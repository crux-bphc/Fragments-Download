# Import Libraries
import aiohttp
import asyncio
import sys
import os
import time
# Import Files
import utils


class DownloadUrl(object):
    def __init__(self, url, path, title=None):
        self.url = url
        self.byteAllow = None
        self.headers = None
        self.path = path
        self.frags = 8
        self.title = utils.removeslash(title)
        self.length = None
        self.done = False
        self.percent = None
        self.session = None
        self.fraglist = None
        self.fragsize = None
        self.donesize = None
        if not self.title:
            self.title = url.split('/')[-1]
            print("title set to "+self.title)
        if "youtube" in self.url or "youtu.be" in self.url:
            self.isTube = True
        else:
            self.isTube = False

    def setfrags(self, frags):
        self.frags = frags

    def __str__(self):
        return str("url: "+self.url)

    async def sendhead(self):
        # Send Head request
        print("sending Head request")
        async with aiohttp.ClientSession() as self.session:
            async with self.session.head(self.url) as response:
                pass
        if response.status == 200 and 'Content-Length' in response.headers:
            print("OK 200")
            self.headers = response.headers
            self.length = int(self.headers['Content-Length'])
            print("length: " + str(self.length))
            assert self.length > 0, "Something went wrong"

            if self.headers['Accept-Ranges'] == 'bytes':
                self.byteAllow = True
            else:
                self.byteAllow = False
        elif response.status > 300 and response.status < 309:
            print(str(response.status) + " " + response.reason)
            print("Trying to follow redirection to %s" %
                  (response.headers['Location']))
            self.url = response.headers['Location']
            await self.sendhead()
        else:
            print(str(response.status_code)+"received"+response.reason)
            self.byteAllow = False
            self.headers = response.headers
            self.length = False

    async def downloadold(self):
        chunk = 16*1024
        # Prepare request
        sendheaders = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/35.0.1916.47 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=headers) as resp:
                print("starting download for frag %d\n" % (num))
                chunk = 1024
                fp = open(self.path + self.title + ".frag" + str(num), "ab")
                while(True):
                    cnk = await resp.content.read(chunk)
                    if not cnk:
                        break
                    fp.write(cnk)
                fp.close()
        self.done = True
        print()
        print("done!")

    async def downloadfrag(self, start, end, num):
        # Get fragment name and check if it already exists
        fname = self.path + self.title + ".frag" + str(num)
        self.fragsize[num] = end - start + 1
        if os.access(fname, os.F_OK):
            start += os.stat(fname).st_size
            self.donesize[num] = os.stat(fname).st_size
            assert start-1 <= end, "Cannot resume!"
            if start == end + 1:
                return
            print("Download for %d will resume from %d" % (num, start))
        sendheaders = {'Range': 'bytes=%d-%d' % (
            start, end), 'User-Agent': 'Mozilla/5.0 \
                          (Macintosh; Intel Mac OS X 10_9_3) \
                          AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/35.0.1916.47 Safari/537.36'}
        # Download fragment
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=sendheaders) as resp:
                print("starting download for frag %d\n" % (num))
                chunk = 16*1024
                fp = open(fname, "ab")
                while(True):
                    cnk = await resp.content.read(chunk)
                    if not cnk:
                        break
                    fp.write(cnk)
                    self.donesize[num] += len(cnk)
                fp.close()
                print("finished download for frag %d\n" % (num))

    def setdefaultfraglist(self):
        # Create a fragment list, populated with fragment number and size
        assert (int(self.length) > 0), "Your download file kinda sucks"
        assert (self.frags > 1), "Alri8 you're an idiot. :p"
        print("Frags : %d" % self.frags)
        self.fraglist = []
        self.fraglist.append((0, int((self.length-1)*(float(1)/self.frags))))
        for i in range(1, self.frags):
            self.fraglist.append(
                (self.fraglist[-1][1]+1,
                 int((self.length-1)*(float(i+1)/self.frags))))

    async def downloadallfrags(self):
        # Download file by dividing it into fragments
        if self.length is None:
            await self.sendhead()
            self.setdefaultfraglist()
        if self.length is False or self.byteAllow is False:
            print("Can not download by fragments.")
            print("Falling back to old download style.")
            self.downloadold()
            return
        else:
            self.setdefaultfraglist()
            if (os.access((self.path + self.title), os.F_OK) and
                    (os.stat((self.path +
                              self.title)).st_size * 1024) >= self.length):
                print("looks like file is downloaded already")
                return
            print("downloading "+'%.2f' % (self.length/(1024*1024.0))+" MB")
            self.fragsize = [-1 for i in range(self.frags)]
            self.donesize = [0 for i in range(self.frags)]
            threadlist = [self.downloadfrag(
                self.fraglist[i][0], self.fraglist[i][1], i)
                          for i in range(self.frags)]
            # Asynchronously download each fragment, consolidating the threads
            await asyncio.gather(*threadlist)
            print()
            print("done downloading")
            print("Starting to merge %d files" % (self.frags))
            utils.catall(self.title, self.frags, self.path)
            print()
