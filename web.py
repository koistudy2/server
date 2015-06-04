# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, redirect, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',username='HYEA')

@app.route('/static/<filename>')
def static_files(filename):
	static_filename='./static/' + filename
	if os.path.exists(static_filename):
		f = open(static_filename)
		return f.read()
	else:
		return error_404()

@app.route('/404')
def error_404():
	return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)