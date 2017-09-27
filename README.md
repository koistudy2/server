# koistudy 2
 - Based on: **Python 2.7**, **Flask**, **Jinja2**, **MongoDB**, **bcrypt**
----------
## Installing requirements

### Python modules
#### Installing pip (on CentOS/RHEL/Fedora)
```
$ sudo yum install python-pip
```
#### Installing pip (on Ubuntu)
```
$ sudo apt-get install python-pip
```
(* Note: Python 2.7.9 and after includes pip by default.)
#### Installing pip (on macOS)
```sh
$ curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
$ sudo easy_install pip
```
#### Installing Flask
```
$sudo pip install Flask
```
#### Installing PyMongo
```
$ sudo pip install pymongo
```

### MongoDB
#### macOS
```sh
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install mongodb
$ sudo mkdir -p /data/db
$ sudo chmod 777 /data/db
$ mongod
```
#### CentOS / Fedora / RHEL (x86_64 system, change baseurl to i686 on i686 system)
- Add following to /etc/yum.repos.d/mongodb-org-3.0.repo
```
[mongodb-org-3.0]
name=MongoDB Repository
baseurl=http://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.0/x86_64/
gpgcheck=0
enabled=1
```
- run following:
```
$ sudo yum install -y mongodb-org
```
 - You may install mongodb 2.4 by yum install -y mongodb, but it may conflict with other packages.
#### CentOS 7
```
$ sudo yum install -y mongodb-server
```
#### Ubuntu
```
$ sudo apt-get install -y mongodb
```

### [bcrypt](https://github.com/dstufft/bcrypt/)
#### macOS
```sh
$ brew install pkg-config libffi
$ export PKG_CONFIG_PATH=/usr/local/[YOUR_USERNAME]/libffi/3.0.13/lib/pkgconfig/
$ sudo pip install bcrypt
```
#### CentOS/RHEL/Fedora/Ubuntu
```
$ sudo pip install bcrypt
```
----------
## Let's run!
 - You have to start mongod first
   - On Linux, type following:
```
$ sudo chkconfig mongod on
$ sudo service mongod start
```
   - On macOS, type following:
```
$ mongod
```
 - Now, type following in your working directory on another terminal:
```
$ python web.py
```
 - Type http://localhost:5000 in your browser and watch what happens.

## For Windows User
 - It is recommended to use virtualenv ([Documentation here](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/))
```
> pip install virtualenv
> pip install virtualenvwrapper-win
```
 - Create virtualenv:
```
> mkvirtualenv koistudy2
> setprojectdir .
```
 - Now install flask:
```
> pip install flask
```
 - Run:
```
> python web.py
```
 - Type http://127.0.0.1:5000 in your browser and watch what happens
