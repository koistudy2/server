# -*- coding: utf-8 -*-
#Logic Related to Signup

from flask import render_template, session, request
from functional import newrender
from flask import request,session
import httplib
import urllib
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import configs
import random
import string
import re
import lang

def signup():
	return newrender('title_signup', filename='signup.html')

def signup_submit():
	params = urllib.urlencode({'secret': configs.recaptcha_secret, 'response': request.form['g-recaptcha-response']})
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	conn = httplib.HTTPSConnection('www.google.com')
	conn.request("POST", "/recaptcha/api/siteverify", params, headers)
	res = conn.getresponse()
	result = json.loads(res.read())
	if not result['success']:
		return newrender("title_signup", filename='basic_display.html', mode='signup_err_captcha')
	else:
		if re.match(u'^[a-zA-Z가-힣ㄱ-ㅎㅏ-ㅣぁ-ゔァ-ヴー々〆〤0-9_\\-.]{4,20}$', request.form['username']):
			if re.match('^.{6,200}$', request.form['password']):
				if request.form['password'] == request.form['password_re']:
					if re.match(u'^[가-힣A-Za-zぁ-ゔァ-ヴー々〆〤 ]{2,30}$', request.form['name']):
						if re.match('^[a-zA-Z._+\\-0-9]+@[a-z0-9.\\-]+\\.[a-z]{2,5}$', request.form['email']):
							import dbhandler
							try:
								idchecker = dbhandler.col_members.find_one({"username": request.form['username']})
								if idchecker['username']:
									return newrender("title_signup", filename='basic_display.html', mode='signup_err_iddup')
							except TypeError:
								try:
									emailchecker = dbhandler.col_members.find_one({"email": request.form['email']})
									if emailchecker['username']:
										return newrender("title_signup", filename='basic_display.html', mode='signup_err_emaildup')
								except TypeError:
									import bcrypt
									activation_link = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
									if 'locale' in session and session['locale']:
										locale = session['locale']
									else:
										locale = 'ko'
									human = {"username": request.form['username'], "password": bcrypt.hashpw(request.form['password'].encode('UTF-8'), bcrypt.gensalt()), "name": request.form['name'], "nickname": request.form['nickname'], "email": request.form['email'], 'activated': False, 'activation_link': activation_link, 'locale': locale}
									msg = MIMEText(render_template('email.txt', link=configs.default_url + '/confirm/' + activation_link).encode('utf-8'), 'html', 'utf-8')
									msg['Subject'] = Header(lang.lang[session.get('locale', 'ko')]['signup_welcome'], 'utf-8')
									msg['From'] = configs.gmail_id + '@gmail.com'
									msg['To'] = request.form['email']
									s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
									s.set_debuglevel(1)
									#try:
									s.login(configs.gmail_id, configs.gmail_pw)
									s.sendmail(msg['From'], msg['To'], msg.as_string())
									s.quit()
									dbhandler.col_members.insert_one(human)
									return newrender('title_signup', filename='basic_display.html', mode='signup_complete')
						else:
							return newrender("title_signup", filename='basic_display.html', mode='signup_err_email')
					else:
						return newrender("title_signup", filename='basic_display.html', mode='signup_err_name')
				else:
					return newrender("title_signup", filename='basic_display.html', mode='signup_err_pwmatch')
			else:
				return newrender("title_signup", filename='basic_display.html', mode='signup_err_password')
		else:
			return newrender("title_signup", filename='basic_display.html', mode='signup_err_username')

def confirm(path):
	import dbhandler
	try:
		user = dbhandler.col_members.find_one({"activation_link": path})
		if user['activated'] == False:
                        newuser = dict(user)
			newuser['activated'] = True
			del newuser['activation_link']
			del newuser['_id']
			dbhandler.col_members.update({'_id': user['_id']}, {"$set": newuser}, upsert=False)
			return newrender('title_signup', filename='basic_display.html', mode='signup_verification_complete')
		else:
			return newrender("title_signup", filename='basic_display.html', mode='signup_err_link')
	except TypeError:
		return newrender("title_signup", filename='basic_display.html', mode='signup_err_link')

def resend():
	try:
		msg = MIMEText(render_template('email.txt', link=configs.default_url + '/confirm/' + session['activation_link']).encode('utf-8'), 'html', 'utf-8')
		msg['Subject'] = Header(lang.lang[session.get('locale', 'ko')]['signup_welcome'], 'utf-8')
		msg['From'] = configs.gmail_id + '@gmail.com'
		msg['To'] = session['activation_email']
		s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
		s.set_debuglevel(1)
		s.login(configs.gmail_id, configs.gmail_pw)
		s.sendmail(msg['From'], msg['To'], msg.as_string())
		s.quit()
		return newrender('title_login', '', 'login_err.html', 'login_err_resent')
	except KeyError:
		return newrender('title_login', '', 'login_err.html', 'login_err_session')

