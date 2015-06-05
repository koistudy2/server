#Logic Related to error handler

@app.errorhandler(404)
def error_404(error):
	return newrender("title_404", "404 Not Found")

@app.errorhandler(500)
def error_500(error):
	return newrender("title_500", error)