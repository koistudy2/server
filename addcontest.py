from flask import session, request
from functional import newrender
import configs
import dbhandler
import lang

def addcontest():
	if (session.get('username') in configs.admin):
		return newrender("title_addcontest", '', 'addcontest.html')
	else:
		return newrender("title_404", "404 Not Found")

def addcontest_submit():
	if (session.get('username') in configs.admin):
		cur_contest = {"contest_id": request.form['contest_id'],
				"display_name": request.form['display_name'],
				"start" : request.form['start'],
				"end": request.form['end'],
				"duration" : request.form['duration'],
				"type": request.form['type']}
		if(cur_contest['type'] == 'Private'):
			cur_contest['password']=request.form['password']
		dbhandler.col_contest.insert_one(cur_contest)
		return newrender("title_addcontest", lang.lang[session.get('locale', 'ko')]['addcontest_added'])
	else:
		return newrender("title_404", "404 Not Found")