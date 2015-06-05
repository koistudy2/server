#Logic Related to robots.txt

@app.route('/probs')
def probs():
	problist = {}
	problist[0] = {'num': '1', 'verdict': 'AC', 'name': 'Hello World', 'solved' : '1', 'tried' : '1', 'diff' : '1'};
	problist[1] = {'num': '2', 'verdict': 'WA', 'name': 'Goodbye Cruel World', 'solved' : '4', 'tried' : '4444', 'diff' : '9'};

	return renderprob(problist,'KOISTUDYS2', '', 'probs')
