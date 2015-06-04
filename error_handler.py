#Logic Related to error handler

@app.errorhandler(404)
def error_404(error):
	return render("KOISTUDYS2", "404 Not Found")

@app.errorhandler(500)
def error_500(error):
	return error