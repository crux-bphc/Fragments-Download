import os,sys,time
def printProgressBar(percent,width=40,speed=None):
    size=os.get_terminal_size()
    width=size[0]-25
    chars=percent*width/100.0;
    print('[',end='')
    print('N'*int(chars),end='');
    print('-'*(width-int(chars)),end='')
    print(']',end='')
    print(" %.1f"%(percent)+"%",end='')
    print(" %.1f"%(speed)+" KB/s   ",end='')
    print('\r',end='')

def printProgress(amount):
    print("Downloaded "+str(amount)+" bytes"+"\r",end='')

def checkSize(filename,size=None):
    if size:
        while True:
            sz=os.stat(filename).st_size;
            printProgressBar(sz*100.0/size)
            if sz==size:
                break
            time.sleep(1)
    else:
        while True:
            sz=os.stat(filename).st_size;
            printProgress(sz)
            if sz==size:
                break
            time.sleep(1)

def fragProgress(title,num,expected):
    hundred=[100 for i in range(num)]
    prevTotal=0
    thisTotal=0
    while True:
        percent=[]
        for i in range(num):
            percent.append(int(os.stat(title+".frag"+str(i)).st_size)*100.000/expected[i])
        avg=sum(percent)/num
        if percent==hundred:
            break
        time.sleep(0.1)
        
def catAll(title,num):
    fp=open(title,"wb")
    for i in range(num):
        ftemp=open(title+".frag"+str(i),"rb")
        fragdata=ftemp.read()
        fp.write(fragdata)
        ftemp.close()
    fp.close()
    print("Done Merging the fragments")
    for i in range(num):
        os.remove(title+".frag"+str(i))
    print("Removed the fragments!")

def removeSlash(title):
    try:
        return title.replace("/"," ")
    except:
        return title
