from flask import session, request
from functional import newrender
import lang
import dbhandler
import configs

def editprob(probid):
	if (session.get('username') in configs.admin):
		if dbhandler.col_probs.count({"unique_id": probid}):
			prob = dbhandler.col_probs.find_one({"unique_id": probid})
			return newrender("title_editprob", filename='editprob.html', data=prob)
		else:
			return newrender("title_editprob", filename='basic_display.html', mode='editprob_err_nosuch')
	else:
		return newrender("title_404", "404 Not Found")

def editprob_submit(probid):
	if (session.get('username') in configs.admin):
		if dbhandler.col_probs.count({"unique_id": probid}):
			print(request.form)
			prob = {"display_name": request.form['title'], 
				"by": request.form['by'], 
				"diff": request.form['diff'], 
				"visib" : ('visib' not in request.form), 
				"gshs" : ('gshs' in request.form), 
				"limit_time": int(request.form['tlimit']), 
				"limit_memory": int(request.form['mlimit']), 
				"desc": request.form['desc'], 
				"input": request.form['input'], 
				"output": request.form['output'], 
				"exin": request.form['input_ex'], 
				"exout": request.form['output_ex']}
			dbhandler.col_probs.update({"unique_id": probid},{"$set":prob})
			return newrender("title_editprob", filename='basic_display.html', mode='editprob_success')
		else:
			return newrender("title_editprob", filename='basic_display.html', mode='editprob_err_nosuch')
	else:
		return newrender("title_404", "404 Not Found")
