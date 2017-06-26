import urllib.request as ur
import requests
import progressBar
def downloadOldSchool(url,title='file'):
    res=requests.head(url)
    if res.status_code!=200 and 'Content-Length' in res.headers:
        print("could not get file size downloading blind")
        ur.urlretrieve(url,title);
    else:
        print(res.headers['Content-Length'])
        length=res.headers['Content-Length'];
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

        connection=ur.Request(url,None,hdr);
        down=ur.urlopen(url)
        chunk=1*1024
        fp=open(title,"wb")
        downloaded=0
        while(True):
            cnk=down.read(chunk);
            if not cnk:
                break
            fp.write(cnk)
            downloaded+=len(cnk)
            progressBar.printProgress(downloaded*100.0/int(length))
        print("done Downloading");
        fp.close()
