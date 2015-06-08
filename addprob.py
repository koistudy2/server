from flask import session, request
from functional import newrender
import configs
import dbhandler
import lang

def addprob():
	if (session.get('username') in configs.admin):
		return newrender("title_addprob", '', 'addprob.html')
	else:
		return newrender("title_404", "404 Not Found")

def addprob_submit():
	if (session.get('username') in configs.admin):
		prob = {"unique_id": request.form['uniqid'], 
				"display_name": request.form['title'], 
				"by": request.form['by'], 
				"visib" : request.form['visib'], 
				"gshs" : request.form['gshs'], 
				"limit_time": request.form['tlimit'], 
				"limit_memory": request.form['mlimit'], 
				"desc": request.form['desc'], 
				"input": request.form['input'], 
				"output": request.form['output'], 
				"exin": request.form['input_ex'], 
				"exout": request.form['output_ex'], 
				'solved': 0, 'submits': 0, 'diff': 0}
		dbhandler.col_probs.insert_one(prob)
		return newrender("title_addprob", lang.lang[session.get('locale', 'ko')]['addprob_added'])
	else:
		return newrender("title_404", "404 Not Found")