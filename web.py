# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
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
	
def render(title='KOISTUDYS2', content='', mode=''):
	return render_template('basic_template.html', title=title, content=content, lang=lang.lang[session.get('locale', 'ko')], menus=configs.menus, session=session, mode=mode)

@app.before_request
def initApp():
	session['locale'] = 'ko'
	if not 'locale' in session:
		session['locale'] = request.accept_languages.best_match(['ko', 'en'])

include('index.py') #@app.route('/')

include('signup.py') #@app.route('/signup') @app.route('/signup/submit', methods=['POST'])

include('login.py') #@app.route('/login') @app.route('/login/submit', methods=['POST'])

include('static.py') #@app.route('/static/<path:path>')

include('robots.py') #@app.route('/robots.txt')

include('error_handler.py') #@app.errorhandler(404) #@app.errorhandler(500)

if __name__ == '__main__':
	app.run(debug=configs.debugMode, port=5000)
	