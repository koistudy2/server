#Logic Related to probs.html

from flask import session
from functional import newrender
import configs
import dbhandler
import math

def probs(page=1):
	page -= 1
	if 'username' in session and session['username'] in configs.admin:
		submit_list = dbhandler.col_probs.find().skip(page * configs.probs_per_page).limit(configs.probs_per_page)
		probcnt = dbhandler.col_probs.count()
	elif 'username' in session and session['username']:
		user = dbhandler.col_members.find_one({"username": session['username']})
		if 'gshs' in user:
			submit_list = dbhandler.col_probs.find({"visib": False}).skip(page * configs.probs_per_page).limit(configs.probs_per_page)
			probcnt = dbhandler.col_probs.count({"visib": False})
		else:
			submit_list = dbhandler.col_probs.find({"visib": False, "gshs": False}).skip(page * configs.probs_per_page).limit(configs.probs_per_page)
			probcnt = dbhandler.col_probs.count({"visib": False, "gshs": False})
	else:
		submit_list = dbhandler.col_probs.find({"visib": False, "gshs": False}).skip(page * configs.probs_per_page).limit(configs.probs_per_page)
		probcnt = dbhandler.col_probs.count({"visib": False, "gshs": False})
	key_list = [('unique_id','Code'), ('verdict','Verdict'), ('display_name','Name'), ('solved','Solved'), ('submits','Submits'), ('diff','Diff')]
	user = dbhandler.col_members.find({"username": session.get('username')})
	if session.get('username') in configs.admin:
		is_admin = True
	else:
		is_admin = False
	lastpage = math.ceil(1.0 * probcnt / configs.probs_per_page)
	page += 1
	if lastpage > page+3:
		pager1 = page+1
		pager2 = page+2
		pager3 = page+3
	elif lastpage > page+2:
		pager1 = page+1
		pager2 = page+2
		pager3 = 0
	elif lastpage > page+1:
		pager1 = page+1
		pager2 = 0
		pager3 = 0
	else:
		pager1 = 0
		pager2 = 0
		pager3 = 0
	return newrender('title_probs', '', 'probs.html', 'probs', {'submit_list':submit_list, 'key_list':key_list, 'is_admin': is_admin, 'pagenow': page, 'pagel0': page-3, 'pagel1': page-2, 'pagel2': page-1, 'pager1': pager1, 'pager2': pager2, 'pager3': pager3})
