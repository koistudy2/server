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

import sys #to supress unicodedecodeerror
reload(sys)
sys.setdefaultencoding('utf-8')

#session setup
if os.path.exists("/dev/random"):
	app.secret_key = open("/dev/random","rb").read(32)
else:
	app.secret_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(32))

#def newrender(title, content, filename='_basic.html', mode='', data=''):
#	return render_template(filename, title=configs.t_prefix + ' - ' + lang.lang[session.get('locale', 'ko')][title], content=content, lang=lang.lang[session.get('locale', 'ko')], menus=configs.menus, session=session, mode=mode, data=data)

@app.before_request
def initApp():
	session['locale'] = 'ko'
	if not 'locale' in session:
		session['locale'] = request.accept_languages.best_match(['ko', 'en'])

import index
app.route('/')(index.index)

import signup
app.route('/signup')(signup.signup)
app.route('/signup/submit', methods=['POST'])(signup.signup_submit)

import login
app.route('/login')(login.login)
app.route('/login/submit', methods=['POST'])(login.login_submit)
app.route('/logout')(login.logout)

import static
app.route('/static/<path:path>')(static.static_files)

import robots
app.route('/robots.txt')(robots.robots)
app.route('/humans.txt')(robots.humans)

import error_handler
app.errorhandler(404)(error_handler.error_404)
app.errorhandler(500)(error_handler.error_500)

import stats
app.route('/stats')(stats.stats)

import probs
app.route('/probs')(probs.probs)

import user #@app.route('/changeuser/submit')
app.route('/user')(user.user)
app.route('/changeuser')(user.changeuser)
app.route('/changeuser/submit', methods=['POST'])(user.changeuser_submit)

import viewprob
app.route('/viewprob/<probid>')(viewprob.viewprob)

if __name__ == '__main__':
	app.run(debug=configs.debugMode, port=5000)

