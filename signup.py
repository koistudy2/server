# -*- coding: utf-8 -*-
#Logic Related to Signup

import sys #to supress unicodedecodeerror
reload(sys)
sys.setdefaultencoding('utf-8')

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
	import re #wth is this? this actually solved the problem but i have no idea
	if not result['success']:
		return render('KOISTUDYS2', '', 'signup_err_captcha')
	else:
		if re.match('^[a-zA-Z가-힣ㄱ-ㅎㅏ-ㅣ0-9_\\-.]{4,20}$', request.form['username']):
			if re.match('^.{6,200}$', request.form['password']):
				if request.form['password'] == request.form['password_re']:
					if re.match('^[가-힣A-Za-z ]{2,30}$', request.form['name']):
						if re.match('^[a-zA-Z._+\\-0-9]+@[a-z0-9.\\-]+\\.[a-z]{2,5}$', request.form['email']):
							import dbhandler
							import bcrypt
							human = {"username": request.form['username'], "password": bcrypt.hashpw(request.form['password'], bcrypt.gensalt()), "name": request.form['name'], "email": request.form['email']}
							col_members.insert_one(human)
							return render('KOISTUDYS2', 'Signup completed', 'signup_complete')
						else:
							return render('KOISTUDYS2', '', 'signup_err_email')
					else:
						return render('KOISTUDYS2', '', 'signup_err_name')
				else:
					return render('KOISTUDYS2', '', 'signup_err_pwmatch')
			else:
				return render('KOISTUDYS2', '', 'signup_err_password')
		else:
			return render('KOISTUDYS2', '', 'signup_err_username')

	#result = json.load(result_json)
	#return result
	#return render('KOISTUDYS2', content, 'signup-submit')