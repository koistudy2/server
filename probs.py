#Logic Related to probs.html

from flask import session
from functional import newrender
import configs
import dbhandler

def probs(page=1):
	page -= 1
	submit_list = dbhandler.col_probs.find().skip(page * configs.probs_per_page).limit(configs.probs_per_page)
	key_list = [('unique_id','Code'), ('verdict','Verdict'), ('display_name','Name'), ('solved','Solved'), ('submits','Submits'), ('diff','Diff')]
	user = dbhandler.col_members.find({"username": session.get('username')})
	if session.get('username') in configs.admin:
		is_admin = True
	else:
		is_admin = False
	return newrender('title_probs', '', 'probs.html', 'probs', {'submit_list':submit_list, 'key_list':key_list, 'is_admin': is_admin, 'pagenow': page, 'pagel1': page-2, 'pagel2': page-1})
