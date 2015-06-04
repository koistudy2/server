# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
import os.path #file exists
app = Flask(__name__)

import lang #multilang support
import configs

import sys #to supress unicodedecodeerror
reload(sys)
sys.setdefaultencoding('utf-8')

#session setup
app.secret_key = open("/dev/random","rb").read(32)

def render(title, content):
	return render_template('basic_template.html', title=title, content=content, lang=lang.lang[session.get('locale', 'ko')], menus=configs.menus)

@app.before_request
def initApp():
	session['locale'] = 'ko'
	if not 'locale' in session:
		session['locale'] = request.accept_languages.best_match(['ko', 'en'])

@app.route('/')
def index():
	content = ''
	return render("KOISTUDYS2", "Sample Content")

@app.route('/static/<path:path>')
def static_files(path):
	if '.' in path:
		return '404 Not Found', 404 
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
