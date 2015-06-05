#koistudy 2

Based on: **Python 2.6**, **Flask**, **Jinja2**, **MongoDB**, **py-bcrypt**

----------
##Installing requirements

###Python modules
<pre>$ sudo easy_install Flask</pre>
<pre>$ sudo easy_install pymongo</pre>

###MongoDB
#### OS X
<pre>$ sudo ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ sudo brew install mongodb
$ sudo mkdir -p /data/db
$ sudo chmod 777 -p /data/db
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
 - Download the archive
 - Unpack the archive, and run setup.py

----------
##Let's run!
 - Type following in your working directory
 - You have to start mongod first
<pre>$ python web.py</pre>
