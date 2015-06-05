#Logic Related to probs.html

@app.route('/probs')
def probs():
	submit_list = [ {'num': '1', 'verdict': 'AC', 'name': 'Hello World', 'solved' : '1', 'tried' : '1', 'diff' : '1'},
	             {'num': '2', 'verdict': 'WA', 'name': 'Goodbye Cruel World', 'solved' : '4', 'tried' : '4444', 'diff' : '9'} ];
	key_list = [('num','Number'), ('verdict','Verdict'), ('name','Name'),
		('solved','Solved'), ('tried','Tried'), ('diff','Diff')]

	return newrender('title_probs', '', 'probs.html', 'probs', {'submit_list':submit_list, 'key_list':key_list})
