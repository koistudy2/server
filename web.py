# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'test'

@app.route('/static/<filename>')
def static_files(filename):
	f = open('./static/' + filename)
	return f.read()

if __name__ == '__main__':
    app.run()