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
$ sudo pip install urllib
$ sudo pip install requests
$ sudo pip install threading 
$ sudo pip install progressBar
$ sudo pip install seqdown
```

## Usage 

Firstly go the folder which contains the all the code.Then for almost any link this will be the standard way of downloading
```sh
$ python3 downloader.py url_which_you_want_to_download
```






License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
### Created By    
## [CRUx - The computing and programming club] 


[CRUx - The computing and programming club]: <https://github.com/CRUx-BPHC>
[BITS Pilani Hyderabad Campus]: <http://www.bits-pilani.ac.in/hyderabad/>

#### of
### [BITS Pilani Hyderabad Campus]
[![N|Solid](https://scontent.fbom1-1.fna.fbcdn.net/v/t1.0-1/p200x200/17904452_1491990900819437_3846562565023385004_n.png?oh=4a26af21c3764e36319197a532de47c7&oe=59DFB8EC)](https://www.facebook.com/cruxbphc/?ref=br_rs)

Members :
* [Neel Bhawsar](https://github.com/neel123456)
* [Himanshu Gupta](https://github.com/him1411)

