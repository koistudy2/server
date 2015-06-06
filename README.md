#koistudy 2

Based on: **Python 2.6**, **Flask**, **Jinja2**, **MongoDB**, **py-bcrypt**

----------
##Installing requirements



###Python modules
####Installing easy_install (on CentOS/RHEL/Fedora)
<pre>$ sudo yum install python-setuptools </pre>
####Installing Flask
<pre>$ sudo easy_install Flask</pre>
####Installing PyMongo
<pre>$ sudo easy_install pymongo</pre>

###MongoDB
#### OS X
<pre>$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install mongodb
$ sudo mkdir -p /data/db
$ sudo chmod 777 /data/db
$ mongod</pre>

#### CentOS / Fedora / RHEL (x86_64 system, change baseurl to i686 on i686 system)
- Add following to /etc/yum.repos.d/mongodb-org-3.0.repo
<pre>[mongodb-org-3.0]
name=MongoDB Repository
baseurl=http://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.0/x86_64/
gpgcheck=0
enabled=1</pre>
- run following
<pre>$ sudo yum install -y mongodb-org</pre>

#### Ubuntu
<pre>$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org</pre>

###[py-bcrypt](http://www.mindrot.org/projects/py-bcrypt/)
 - Install Python development package.

####CentOS/RHEL/Fedora
<pre>$ sudo yum install python-devel</pre>

####Ubuntu
<pre>$ sudo apt-get install python-dev</pre>
 - Download the archive at https://code.google.com/p/py-bcrypt/downloads/list
 - Unpack the archive, and run setup.py

----------
##Let's run!
 - You have to start mongod first
<pre>$ mongod</pre>
 - Now, type following in your working directory on another terminal
<pre>$ python web.py</pre>
 - Type http://localhost:5000 in your browser and watch what happens
