#koistudy 2

 - Based on: **Python 2.7**, **Flask**, **Jinja2**, **MongoDB**, **bcrypt**

----------
##Installing requirements



###Python modules
####
####Installing pip (on CentOS/RHEL/Fedora)
<pre>$ sudo yum install python-pip </pre>
####Installing pip (on Ubuntu)
<pre>$ sudo apt-get install python-pip </pre>
Note: Python 2.7.9 and after includes pip by default.
####Installing pip (on macOS)
<pre>$ curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
$ sudo easy_install pip</pre>
####Installing Flask
<pre>$ sudo pip install Flask</pre>
####Installing PyMongo
<pre>$ sudo pip install pymongo</pre>

###MongoDB
#### macOS
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
 - You may install mongodb 2.4 by yum install -y mongodb, but it may conflict with other packages.

#### CentOS 7
- run following
<pre>$ sudo yum install -y mongodb-server</pre>

#### Ubuntu
<pre>$ sudo apt-get install -y mongodb</pre>

###[bcrypt](https://github.com/dstufft/bcrypt/)

####macOS
<pre>$ brew install pkg-config libffi
$ export PKG_CONFIG_PATH=/usr/local/[YOUR_USERNAME]/libffi/3.0.13/lib/pkgconfig/
$ sudo pip install bcrypt</pre>
####CentOS/RHEL/Fedora/Ubuntu
<pre>$ sudo pip install bcrypt</pre>

----------
##Let's run!
 - You have to start mongod first
   - On Linux, type following
<pre>$ sudo chkconfig mongod on
$ sudo service mongod start</pre>
   - On macOS, type following
<pre>$ mongod</pre>
 - Now, type following in your working directory on another terminal
<pre>$ python web.py</pre>
 - Type http://localhost:5000 in your browser and watch what happens

## For Windows User
 - You have to install virtualenv [Documentation](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)
<pre>> pip install virtualenv
> pip install virtualenvwrapper-win</pre>
 - Create virtualenv
<pre>> mkvirtualenv koistudy2
> setprojectdir .</pre>
 - Now install flask
<pre>> pip install flask </pre>
 - Run
<pre>> python web.py </pre>
 - Type http://127.0.0.1:5000 in your browser and watch what happens
