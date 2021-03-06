#Logic Related to probs.html

from flask import session
from functional import newrender
import configs
import dbhandler
import math
import lang

def probs(page=1):
	page -= 1
	a = lang.lang[session['locale']]
	key_list = [('unique_id', a['probs_code']), ('verdict', a['probs_verdict']), ('display_name', a['probs_name']), ('solved', a['probs_solved']), ('submits', a['probs_submits']), ('diff',a['probs_diff'])]
	is_admin = False
	if 'username' in session and session['username'] in configs.admin:
		prob_list = dbhandler.col_probs.find().skip(page * configs.probs_per_page).limit(configs.probs_per_page)
		probcnt = dbhandler.col_probs.count()
		is_admin = True
	elif 'username' in session and session['username']:
		user = dbhandler.col_members.find_one({"username": session['username']})
		if 'gshs' in user:
			prob_list = dbhandler.col_probs.find({"adminonly": False}).skip(page * configs.probs_per_page).limit(configs.probs_per_page)
			probcnt = dbhandler.col_probs.count({"adminonly": False})
		else:
			prob_list = dbhandler.col_probs.find({"adminonly": False, "gshs": False}).skip(page * configs.probs_per_page).limit(configs.probs_per_page)
			probcnt = dbhandler.col_probs.count({"adminonly": False, "gshs": False})
	else:
		prob_list = dbhandler.col_probs.find({"adminonly": False, "gshs": False}).skip(page * configs.probs_per_page).limit(configs.probs_per_page)
		probcnt = dbhandler.col_probs.count({"adminonly": False, "gshs": False})
	prob_list = prob_list.sort('unique_id',1)
	user = dbhandler.col_members.find({"username": session.get('username')})
	if session.get('username') in configs.admin:
		is_admin = True
	else:
		is_admin = False
	lastpage = math.ceil(1.0 * probcnt / configs.probs_per_page)
	page += 1
	pager1 = 0
	pager2 = 0
	pager3 = 0
	if lastpage >= page+1:
		pager1 = page+1
	if lastpage >= page+2:
		pager2 = page+2
	if lastpage >= page+3:
		pager3 = page+3
	return newrender('title_probs', '', 'probs.html', 'probs', 
		{'prob_list':prob_list, 
		 'key_list':key_list,
		 'is_admin': is_admin,
		 'pagenow': page,
		 'pagel0': page-3, 'pagel1': page-2, 'pagel2': page-1,
		 'pager1': pager1, 'pager2': pager2, 'pager3': pager3})
