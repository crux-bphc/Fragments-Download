# All purpose downloader 
It is an all purpose downloader written completely in python 
# Features 

  - Incorporates multi-threading and splits a large file into a number of pieces depending on the user
  - supports a feature of pausing and resuming the downloads any number of times 
  - consistently writes the files to hard drive from from RAM hence allowing machines with low RAM cpacity to download lage sized files 
 - written completely in python hence can be used in linux, mac and windows 
  - has very little dependencies on python libraries 
- Downloading speed can be improved dramatically (upto 5 folds) if used over a LAN

## Usage
  - Can be used to download almost any kind of file 
  - supports pausing the downloads which can come handy if internet speed is slow 
  
 
### Installation
##### Installing Python and pip
We are using Python 3 .
Reason we will be using the Python3, it’s the Future. The support for Python 2.7.x is provided till 2020, after that Python community won’t provide any updates for 2.7.x version.
Where to install Python from?
It depends on which operating system you are having.
*	If you have Linux/Mac Operating System, then you don’t need to install. They are shipped with python.
*	If you are a Windows user, then you have to install it all by yourself. There are 3 major ways:
* 1. 	Downloading the [Installation file](https://www.python.org/) from the official website of Python itself.
* 2.	Installing python from [conda] (installs other software with python) and mini-conda(will only install python). We will install python using miniconda 
* Install [pip] for various libraries needed.

[conda]: <https://conda.io/miniconda.html>
[pip]: <https://pip.pypa.io/en/stable/installing/>



Install the dependencies and devDependencies and open terminal.  

```sh
$ sudo pip install pafy
$ sudo pip install youtube-dl
```

## Usage 

Firstly go the folder which contains the all the code.

![](http://i.imgur.com/7o0WvmT.png)

Change the the no of fragments you want by altering the variable frag in line 21 of downloader.py. Recomended no of fragments are between 4 to 32. Default is set to 5.Then for almost any link this will be the standard way of downloading.


```sh
$ python3 downloader.py url_you_want_to_download
```
For videos just copy the youtube url and paste it and if you want the audio of that paticular video just add m after the code.For starting a single file download without fragmenting the file press ctrl + c and for stopping/ pausing the downloads press ctrl + c again 

## Example 

Downloading a video from youtube.com

![](http://i.imgur.com/9g6RA0I.png)

default number of fragments are 5 which are created in the folder containing the script 

![](http://i.imgur.com/WHJWmJu.png)

pressing ctrl + c will initiate a single file download 

![](http://i.imgur.com/620axs4.png)

Pressing ctrl + c will stop the download. Runnig the the command again will start the download. In the image below, the download is starting from 22% because the script already considers the downloded portion completed and shows percentage completion the rest of the file

![](http://i.imgur.com/9g6RA0I.png)


Downloading a mp3 file from youtube 

```sh
$ python3 downloader.py url_you_want_to_download m
```

![](http://i.imgur.com/3ltpxKP.png?1)

The fragments will be deleted after the download is finished.


License
----
MIT License

Copyright (c) 2017 Crux



### Created By    
## [CRUx - The Computing and Programming Club] 


[CRUx - The computing and programming club]: <https://github.com/CRUx-BPHC>
[BITS Pilani Hyderabad Campus]: <http://www.bits-pilani.ac.in/hyderabad/>

#### of
### [BITS Pilani Hyderabad Campus]
[![](https://scontent.fbom1-1.fna.fbcdn.net/v/t1.0-1/p200x200/17904452_1491990900819437_3846562565023385004_n.png?oh=4a26af21c3764e36319197a532de47c7&oe=59DFB8EC)](https://www.facebook.com/cruxbphc/?ref=br_rs)

Members involved in the project :
* [Neel Bhavsar](https://github.com/neel123456)
* [Himanshu Gupta](https://github.com/him1411)

