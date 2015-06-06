#Logic Related to users page

@app.route('/user')
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

@app.route('/changeuser')
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