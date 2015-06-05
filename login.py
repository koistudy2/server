# -*- coding: utf-8 -*-
#Logic Related to Signup

@app.route('/login')
def login():
	return newrender('title_login', '', 'login.html')

@app.route('/login/submit', methods=['POST'])
def login_submit():
	import dbhandler
	import bcrypt
	import datetime
	import md5
	try:
		user = dbhandler.col_members.find_one({"username": request.form['username']})
		if 'migrated' in user: #migrated from koistudy1
			if md5.new(request.form['password']).digest() == user['password']:
				session['username'] = request.form['username']
				log = {"date": datetime.datetime.now(), "type": "login_migrated", "result": "succeed", "username": request.form['username'], "ip": request.remote_addr}
				salt=bcrypt.gensalt()
				user['password'] = bcrypt.hashpw(request.form['password'], salt)
				user['salt']=salt
				del user['migrated']
				dbhandler.col_members.update({'_id': user['_id']}, {"$set": user}, upsert=False)
				dbhandler.col_logs.insert_one(log)
				return redirect('/')
		else:
			if bcrypt.hashpw(request.form['password'].encode("UTF-8"), user['salt'].encode("UTF-8")) == user['password']:
				session['username'] = request.form['username']
				log = {"date": datetime.datetime.now(), "type": "login", "result": "succeed", "username": request.form['username'], "ip": request.remote_addr}
				dbhandler.col_logs.insert_one(log)
				return redirect('/')
			else:
				log = {"date": datetime.datetime.now(), "type": "login", "result": "wrongpw", "username": request.form['username'], "ip": request.remote_addr}
				dbhandler.col_logs.insert_one(log)
				return newrender('title_login', '', 'login_err.html', 'login_err_pw')
	except IndexError:
		log = {"date": datetime.datetime.now(), "type": "login", "result": "wrongusername", "username": request.form['username'], "ip": request.remote_addr}
		dbhandler.col_logs.insert_one(log)
		return newrender('title_login', '', 'login_err.html', 'login_err_username')

@app.route('/logout')
def logout():
	del session['username']
	return redirect('/')
