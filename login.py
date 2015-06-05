# -*- coding: utf-8 -*-
#Logic Related to Signup

@app.route('/login')
def login():
	return render('KOISTUDYS2', '', 'login')

@app.route('/login/submit', methods=['POST'])
def login_submit():
	import dbhandler
	import bcrypt
	#human = {"username": request.form['username'], "password": bcrypt.hashpw(request.form['password'], bcrypt.gensalt()), "name": request.form['name'], "email": request.form['email']}
	try:
		pw = dbhandler.col_members.find({"username": request.form['username']})[0]['password']
		if bcrypt.hashpw(request.form['password'], pw) == pw:
			return 'login succeed'
		else:
			return 'login failed'
	except IndexError:
		return 'account not found'

	#result = json.load(result_json)
	#return result
	#return render('KOISTUDYS2', content, 'signup-submit')