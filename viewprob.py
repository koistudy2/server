#Logic Related to viewprob

from flask import session
from functional import newrender
import dbhandler
import os

def viewprob(probid):
	prob = dbhandler.col_probs.find_one({"unique_id": probid})
	if 'username' in session:
		user = dbhandler.col_members.find_one({"username": session['username']})
		if 'defaulttheme' in user:
			theme = user['defaulttheme']
		else:
			theme = 'chrome'
	else:
		theme = 'chrome'
	return newrender('title_viewprob', '', 'viewprob.html', '', {'prob':prob, 'session': session, 'theme': theme})

def settheme(theme):
	if os.path.exists("./static/ace/theme-" + theme + ".js"):
		if 'username' in session:
			user = dbhandler.col_members.find_one({"username": session['username']})
			user['defaulttheme'] = theme
			dbhandler.col_members.update({'_id': user['_id']}, {"$set": user}, upsert=False)
			return '{"result": "succeed"}'
		else:
			return '{"result": "error_user"}'
	else:
		return '{"result": "error_notheme"}'