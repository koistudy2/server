#koistudy 2

Based on: **Python 2.6**, **Flask**, **Jinja2**, **MongoDB**, **py-bcrypt**

----------
##Installing requirements

###Python modules
<pre>$ sudo easy_install Flask</pre>
<pre>$ sudo easy_install pymongo</pre>

###MongoDB (For OS X, use apt-get or yum on GNU/Linux)
<pre>$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ sudo brew install mongodb
$ sudo mkdir -p /data/db
$ sudo chmod 777 -p /data/db
$ mongod</pre>

###[py-bcrypt](http://www.mindrot.org/projects/py-bcrypt/)
