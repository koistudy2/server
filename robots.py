#Logic Related to robots.txt

@app.route('/robots.txt')
def robots():
	return 'User-agent: *\r\nAllow: /'