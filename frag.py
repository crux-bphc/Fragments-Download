import pafy
import urllib
import requests
import _thread
import threading
import sys
import os
import time
import seqdown
#import progressBar
try:
    import http.client as hlib
except:
    import httplib as hlib

try:
    import urllib.request as ur
except:
    import urllib2 as ur
title=""
frags=5
childList=[]
expected=[0 for i in range(frags)]
fragsize=[0 for i in range(frags)]

def printProgress(percent,width=40):
    chars=percent*width/100;
    print('[',end='')
    print('N'*int(chars),end='');
    print('-'*(width-int(chars)),end='')
    print(']',end='')
    print(" "+str(percent)+"%",end='')
    print('\r',end='')

    
def getFrags(size):
    global frags
    assert (size>0),"Your video kinda sucks"
    assert (frags>1),"Alri8 you're an idiot"
    l=[]
    l.append((0,int(size*(float(1)/frags))));
    for i in range(1,frags):
        l.append((l[-1][1]+1,int(size*(float(i+1)/frags))))    
    return l

def getUrl(yurl,music=False):
    global title
    try:
        vObj=pafy.new(yurl);
        title=vObj.title
        print(title)
        if music==True:
            title+=".mp3"
            return str(vObj.getbestaudio().url)
        title+=".mp4"
        return str(vObj.getbest().url)
    except:
        print("An error occured. Check your internet connection and the url :(")
        exit(1);

def downloadFrag(url,start,end,num):
    try:
        import urllib.request as ur
    except:
        import urllib2 as ur
    global frags
    global title
    global fragsize
    global expected
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    connection=ur.Request(url,None,headers);
    connection.headers['Range']="bytes=%d-%d" % (start,end)
    expected[num]=end-start+1
    #print("starting download for frag %d\n" % (num))
    down=ur.urlopen(connection)
    chunk=1*1024
    fp=open(title+".frag"+str(num),"wb")
    while(True):
        cnk=down.read(chunk);
        if not cnk:
            break
        fp.write(cnk)
        fragsize[num]+=chunk
    #print("finished download for frag %d\n" % (num))
    
def getContentLength(url):
    print('requested headers')
    res=requests.head(url)
    print('got headers')
    head=res.headers
    print(head)
    assert head['Accept-Ranges']=='bytes',"Looks like an old server that does not support byte ranges.\nCan't download\nTry using wget"
    length=head['Content-Length']   
    assert int(length)>0,"Something's wrong with video length (is zero :p)"
    return int(length);

def catAll():
    global title
    global frags
    fp=open(title,"wb")
    for i in range(frags):
        fi=open(title+'.frag'+str(i),"rb")
        tempcontent=fi.read()
        fp.write(tempcontent)
        fi.close()
        #progressBar.printProgress(100*(i+1)/frags)
        printProgress(100*(i+1)/frags)
    fp.close()
    print();
    cleanYourMess()
    
def cleanYourMess():
    global title
    global frags
    for i in range(frags):
        os.remove(title+".frag"+str(i))
    print("Deleted the fragments!");
    
def checklen():
    global title
    global frags
    global fragsize
    global expected
    hundred=[100 for i in range(frags)]
    while(True):
        percent=[]
        for i in range(frags):
            percent.append(int(fragsize[i]*100/expected[i]))
        avg=sum(percent)/frags
        #progressBar.printProgress(avg)
        printProgress(avg)
        if percent==hundred:
            break
        time.sleep(1)
        
def downloadAll(url):
    global frags
    global childList
    length=getContentLength(url)
    print('%.2f'%(length/(1024*1024.0))+" MB");
    fraglist=getFrags(length);
    childList=[]
    for i in range(frags):
        t=threading.Thread(target=downloadFrag,kwargs={'url':url,'start':fraglist[i][0],'end':fraglist[i][1],'num':i}) 
        t.start()
        childList.append(t)
    time.sleep(1)
    check=threading.Thread(target=checklen)
    check.start()
    childList.append(check)
    for t in childList:
        t.join()
    print();
    print("Done Downloading")
    print("Starting to merge %d fragments"%(frags))
    catAll()
    print();

getmusic=False
try:
    url=sys.argv[1]
except:
    print("usage python3 frag.py <url>")
    exit(1)
try:
    m=sys.argv[2]
    if m=='m':
        getmusic=True
    else:
        print("use 'python3 frag.py -h' for help")
        exit(1)
except:
    pass

if "youtube" in url or "youtu.be" in url:
    url=getUrl(url,getmusic)            #use pafy to get a url for video
    #print(url+' is to be downloaded');
else:
    l=url.split('/')
    title=l[-1];
print("fragments: "+str(frags))
try:
    downloadAll(url);
except:
    print("Coud not fragment the file.Rolling back to sequential download")
    seqdown.downloadOldSchool(url,title)
