import pafy
import urllib
import requests
import _thread
import threading
try:
    import http.client as hlib
except:
    import httplib as hlib

try:
    import urllib.request as ur
except:
    import urllib2 as ur
title="Video.mp4"
frags=5
childList=[]
parts=[-1 for i in range(frags)]

def getFrags(size):
    global frags
    assert (size>0),"Your video kinda sucks"
    assert (frags>1),"Alri8 you're an idiot"
    l=[]
    l.append((0,int(size*(float(1)/frags))));
    for i in range(1,frags):
        l.append((l[-1][1]+1,int(size*(float(i+1)/frags))))    
    return l

def getUrl(yurl):
    global title
    try:
        vObj=pafy.new(yurl);
        title=vObj.title
        return str(vObj.getbest().url)
    except:
        print("An error occured. Check your internet connection and the url :(")
        exit(1);

def downloadFrag(url,start,end,num):
    try:
        import urllib.request as ur
    except:
        import urllib2 as ur
    global parts
    connection=ur.Request(url);
    connection.headers['Range']="bytes=%d-%d" % (start,end)
    print("starting download for frag %d\n" % (num))
    down=ur.urlopen(connection)
    parts[num]=down.read();
    print("finished download for frag %d\n" % (num))
    
def getContentLength(url):
    print('requested headers')
    res=requests.head(url)
    print('got headers')
    head=res.headers
    print(head)
    length=head['Content-Length']
    assert int(length)>0,"Something's wrong with video length (is zero :p)"
    return int(length);

def downloadAll(url):
    global frags
    global childList
    length=getContentLength(url)
    print(length);
    fraglist=getFrags(length);
    childList=[]
    for i in range(frags):
        t=threading.Thread(target=downloadFrag,kwargs={'url':url,'start':fraglist[i][0],'end':fraglist[i][1],'num':i}) 
        t.start()
        childList.append(t)


def catAll():
    global title
    global parts
    global frags
    filename=title;
    p=parts[0]
    for i in range(1,frags):
        p+=parts[i];

    f=open(filename,"wb")
    f.write(p)
    print("done!")

print("enter video url")
yurl=input()
gurl=getUrl(yurl)
downloadAll(gurl)
for t in childList:
    t.join()

catAll()
   
