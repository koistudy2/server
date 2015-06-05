# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request, redirect
import os.path #file exists
import httplib, urllib
import json
#custom modules
import lang
import configs
import dbhandler

import random
import string

app = Flask(__name__)

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)

import sys #to supress unicodedecodeerror
reload(sys)
sys.setdefaultencoding('utf-8')

#session setup
if os.path.exists("/dev/random"):
	app.secret_key = open("/dev/random","rb").read(32)
else:
	app.secret_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(32))

def newrender(title, content, filename='basic_new.html', mode=''):
	return render_template(filename, title=configs.t_prefix + ' - ' + lang.lang[session.get('locale', 'ko')][title], content=content, lang=lang.lang[session.get('locale', 'ko')], menus=configs.menus, session=session, mode=mode)

@app.before_request
def initApp():
	session['locale'] = 'ko'
	if not 'locale' in session:
		session['locale'] = request.accept_languages.best_match(['ko', 'en'])

include('index.py') #@app.route('/')

include('signup.py') #@app.route('/signup') @app.route('/signup/submit', methods=['POST'])

include('login.py') #@app.route('/login') @app.route('/login/submit', methods=['POST']) @app.route('/logout')

include('static.py') #@app.route('/static/<path:path>')

include('robots.py') #@app.route('/robots.txt')

include('error_handler.py') #@app.errorhandler(404) #@app.errorhandler(500)

include('stats.py') #@app.route('/stats')

include('probs.py') #@app.route('/probs')

include('user.py') #@app.route('/user')

if __name__ == '__main__':
	app.run(debug=configs.debugMode, port=5000)
	