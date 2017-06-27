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
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ npm run predeploy
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md] [PlDb] |
| Github | [plugins/github/README.md] [PlGh] |
| Google Drive | [plugins/googledrive/README.md] [PlGd] |
| OneDrive | [plugins/onedrive/README.md] [PlOd] |
| Medium | [plugins/medium/README.md] [PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md] [PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 80, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 80 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MOAR Tests
 - Add Night Mode

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
#### of
### BITS Pilani Hyderabad Campus

[CRUx - The computing and programming club]: <https://github.com/CRUx-BPHC>


[![N|Solid](https://scontent.fbom1-1.fna.fbcdn.net/v/t1.0-1/p200x200/17904452_1491990900819437_3846562565023385004_n.png?oh=4a26af21c3764e36319197a532de47c7&oe=59DFB8EC)](https://github.com/orgs/CRUx-BPHC/dashboard)

Members :
* [Neel Bhawsar](https://github.com/neel123456)
* [Himanshu Gupta](https://github.com/him1411)

