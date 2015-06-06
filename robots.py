#Logic Related to robots.txt

def robots():
	return 'User-agent: *\r\nAllow: /'

def humans():
	return """User-agent: *
Allow: /
Disallow: /admin
User-agent: Administrator
Allow: /admin"""
