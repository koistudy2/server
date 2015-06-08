# -*- coding: utf-8 -*-
#Logic Related to Signup

from flask import session, request, redirect
from functional import newrender
from flask import session, request

import dbhandler
import bcrypt
import datetime
import md5

import lang

def login():
	return newrender('title_login', '', 'login.html')

def login_submit():
	try:
		user = dbhandler.col_members.find_one({"username": request.form['username']})
		if user['activated'] == False:
			session['activation_link'] = user['activation_link']
			session['activation_email'] = user['email']
			return newrender('title_login', '', 'login_err.html', 'login_err_email')
		if 'migrated' in user: #migrated from koistudy1
			if md5.new(request.form['password']).digest() == user['password']:
				session['username'] = request.form['username']
				session['nickname'] = user['nickname']
				session['locale'] = user['locale']
				log = {"date": datetime.datetime.now(), "type": "login_migrated", "result": "succeed", "username": request.form['username'], "ip": request.remote_addr}
				user['password'] = bcrypt.hashpw(request.form['password'].encode("UTF-8"), bcrypt.gensalt())
				del user['migrated']
				dbhandler.col_members.update({'_id': user['_id']}, {"$set": user}, upsert=False)
				dbhandler.col_logs.insert_one(log)
				return redirect('/')
		else:
			if bcrypt.hashpw(request.form['password'].encode("UTF-8"), user['password'].encode('utf-8')) == user['password']:
				session['username'] = request.form['username']
				session['nickname'] = user['nickname']
				session['locale'] = user['locale']
				log = {"date": datetime.datetime.now(), "type": "login", "result": "succeed", "username": request.form['username'], "ip": request.remote_addr}
				dbhandler.col_logs.insert_one(log)
				return redirect('/')
			else:
				log = {"date": datetime.datetime.now(), "type": "login", "result": "wrongpw", "username": request.form['username'], "ip": request.remote_addr}
				dbhandler.col_logs.insert_one(log)
				return newrender('title_login', '', 'login_err.html', 'login_err_pw')
	except (IndexError, TypeError):
		log = {"date": datetime.datetime.now(), "type": "login", "result": "wrongusername", "username": request.form['username'], "ip": request.remote_addr}
		dbhandler.col_logs.insert_one(log)
		return newrender('title_login', '', 'login_err.html', 'login_err_username')

def logout():
	del session['username']
	return redirect('/')
