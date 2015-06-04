#Logic Related to Signup

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