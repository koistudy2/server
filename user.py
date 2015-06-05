#Logic Related to users page

@app.route('/user')
def user():
	import dbhandler
	try:
		user = dbhandler.col_members.find_one({"username": session['username']})
		data = {}
		data['name'] = user['name']
		data['username'] = user['username']
		return newrender('title_user', '', 'user.html', '', data)
	except KeyError:
		return newrender('title_error', 'Error')
