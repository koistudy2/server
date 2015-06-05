#Logic related to /

@app.route('/')
def index():
	content = ''
	return newrender("title_main", "Sample Content")
