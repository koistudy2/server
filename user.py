#Logic Related to users page

@app.route('/user')
def user():
	return newrender('title_user', '', 'user.html')
