# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
import os.path #file exists
import re #regex
app = Flask(__name__)

debugMode = True #디버그
s_prefix = './static/' #static 파일 디렉토리:

menus = [{'name': 'Probs'}]

#multilang support
lang = {}
with open('./lang.txt') as f:
	lines = f.readlines()
name = re.compile('')
for line in lines:
	each = re.match('([^.]+)\.([^=]+)=(.*)\n', line)
	if each:
		if not (each.group(2)) in lang:
			lang[each.group(2)] = {}
		lang[each.group(2)][each.group(1)] = each.group(3)

#session setup
app.secret_key = 'ssss542rf33rg242ss'

@app.before_request
def initApp():
	session['locale'] = 'gfdsgdsfgsdfgdsfgsdfg'
	if not 'locale' in session:
		session['locale'] = request.accept_languages.best_match(['ko', 'en'])

@app.route('/')
def index():
	content = ''
	print session['locale'] + session['locale'] + session['locale']
	return render_template('basic_template.html', title="Hello,world!", content=content, lang=lang[session['locale']])

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
	return error

if __name__ == '__main__':
	app.run(debug=debugMode, port=5000)
