#Logic Related to users page

@app.route('/user')
def user():
	return 'User-agent: *\r\nAllow: /'
