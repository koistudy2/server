from flask import session, request
from functional import newrender
import configs
import dbhandler
import lang

def addcontests():
	if (session.get('username') in configs.admin):
		return newrender("title_addcontests", '', 'addcontests.html')
	else:
		return newrender("title_404", "404 Not Found")

def addcontests_submit():
	if (session.get('username') in configs.admin):

		cont = {"contest_id": request.form['contid'], 
				"display_name": request.form['title'], 
				"contest_rule": request.form['rule'], 
				"contestants" : request.form['contestants'], 
				"starts" : request.form['start'], 
				"ends": request.form['ends'], 
				"private": request.form['private'], 
				"time" : request.form['time']}

		dbhandler.col_probs.insert_one(prob)
		return newrender("title_addcontests", lang.lang[session.get('locale', 'ko')]['addcontests_added'])
	else:
		return newrender("title_404", "404 Not Found")