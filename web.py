# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',username='HYEA')

@app.route('/static/<filename>')
def static_files(filename):
	f = open('./static/' + filename)
	return f.read()

if __name__ == '__main__':
    app.run(debug=True)