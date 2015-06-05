#Logic Related to robots.txt

@app.route('/robots.txt')
def robots():
	return 'User-agent: *\r\nAllow: /'

@app.route('/humans.txt')
def humans():
	return """User-agent: *
Allow: /
Disallow: /admin
User-agent: Administrator
Allow: /admin"""
