# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
app = Flask(__name__)

import os.path #file exists

import sys #to supress unicodedecodeerror
reload(sys)
sys.setdefaultencoding('utf-8')

import httplib, urllib

import json

#custom modules
import lang
import configs
import dbhandler

#session setup
app.secret_key = open("/dev/random","rb").read(32)

def render(title='KOISTUDYS2', content='', mode=''):
	return render_template('basic_template.html', title=title, content=content, lang=lang.lang[session.get('locale', 'ko')], menus=configs.menus, session=session, mode=mode)

@app.before_request
def initApp():
	session['locale'] = 'ko'
	if not 'locale' in session:
		session['locale'] = request.accept_languages.best_match(['ko', 'en'])

@app.route('/')
def index():
	content = ''
	return render("KOISTUDYS2", "Sample Content")

@app.route('/signup')
def signup():
	return render('KOISTUDYS2', '', 'signup')

@app.route('/signup/submit', methods=['POST'])
def signup_submit():
	params = urllib.urlencode({'secret': '6LfC4AcTAAAAAFtmCCOlsAE4kLXSJuNPQu49uiCp', 'response': request.form['g-recaptcha-response']})
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	conn = httplib.HTTPSConnection('www.google.com')
	conn.request("POST", "/recaptcha/api/siteverify", params, headers)
	res = conn.getresponse()
	result = json.loads(res.read())
	if not result['success']:
		return render('KOISTUDYS2', '', 'signup_err_captcha')
	else:
		return render('KOISTUDYS2', 'Signup completed', 'signup_complete')
	#result = json.load(result_json)
	#return result
	#return render('KOISTUDYS2', content, 'signup-submit')

@app.route('/static/<path:path>')
def static_files(path):
	if '.' in path:
		return error_404(0)
	if os.path.isfile(s_prefix + path):
		f = open(s_prefix + path)
		return f.read()
	else:
		return '404 Not Found', 404

@app.route('/robots.txt')
def robots():
	return 'User-agent: *\r\nAllow: /'

@app.errorhandler(500)
def error_500(error):
	return error

@app.errorhandler(404)
def error_404(error):
	return render("KOISTUDYS2", "404 Not Found")

if __name__ == '__main__':
	app.run(debug=configs.debugMode, port=5000)
