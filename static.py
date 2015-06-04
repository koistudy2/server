#Logic Related to static files

@app.route('/static/<path:path>')
def static_files(path):
	if '.' in path:
		return error_404(0)
	if os.path.isfile(s_prefix + path):
		f = open(s_prefix + path)
		return f.read()
	else:
		return '404 Not Found', 404