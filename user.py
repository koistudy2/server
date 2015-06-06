# -*- coding: utf-8 -*-
#Logic Related to users page

from flask import session, request
import lang
from functional import newrender

def user():
	import dbhandler
	try:
		user = dbhandler.col_members.find_one({"username": session['username']})
		data = {}
		data['name'] = user['name']
		data['username'] = user['username']
		data['nickname'] = user['nickname']
		return newrender('title_user', '', 'user.html', '', data)
	except KeyError:
		return newrender('title_error', 'Error')

def changeuser():
	import dbhandler
	try:
		user = dbhandler.col_members.find_one({"username": session['username']})
		data = {}
		data['name'] = user['name']
		data['username'] = user['username']
		data['nickname'] = user['nickname']
		data['email'] = user['email']
		return newrender('title_user', '', 'changeuser.html', '', data)
	except KeyError:
		return newrender('title_error', 'Error')

def changeuser_submit():
	import dbhandler
	import bcrypt
	import re
	try:
		user = dbhandler.col_members.find_one({"username": session['username']})
		data = {}
		if bcrypt.hashpw(request.form['password_now'].encode("UTF-8"), user['password']) == user['password']:
			if request.form['password_new'] != '':
				if re.match('^.{6,200}$', request.form['password_new']):
					if request.form['password_new'] == request.form['password_new_re']:
						user['password'] = bcrypt.hashpw(request.form['password_new'].encode("UTF-8"), user['password'])
					else:
						return newrender('title_user', '', 'changeuser_err.html', 'changeuser_err_pw_match')
				else:
					return newrender('title_user', '', 'changeuser_err.html', 'changeuser_err_pw_format')
			if re.match(u'^[가-힣A-Za-z ]{2,30}$', request.form['name']):
				user['name'] = request.form['name']
			else:
				return newrender('title_user', '', 'changeuser_err.html', 'changeuser_err_name')
			if re.match('^[a-zA-Z._+\\-0-9]+@[a-z0-9.\\-]+\\.[a-z]{2,5}$', request.form['email']):
				user['email'] = request.form['email']
			else:
				return newrender('title_user', '', 'changeuser_err.html', 'changeuser_err_email')
			dbhandler.col_members.update({'_id': user['_id']}, {"$set": user}, upsert=False)
			return newrender('title_user', lang.lang[session.get('locale', 'ko')]['changeuser_complete'])
		else:
			return newrender('title_user', '', 'changeuser_err.html', 'changeuser_err_pw')
	except KeyError:
		return newrender('title_error', 'Error')