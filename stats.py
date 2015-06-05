#Logic Related to stats.html

@app.route('/stats')
def stats():
	return newrender('title_stats', '', 'stats.html')
