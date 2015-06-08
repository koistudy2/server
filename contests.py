#Logic Related to contests.html

from flask import session
from functional import newrender
import configs
import dbhandler

def contests(page=1):
	page -= 1
	submit_list = dbhandler.col_contests.find().skip(page * configs.contests_per_page).limit(configs.contests_per_page)
	key_list = [('contest_id','Code'), ('contest_rule','Rules'),('display_name','Name'), ('contestants','Contestants'), ('starts','Starts'), ('ends','Ends')]
	user = dbhandler.col_members.find({"username": session.get('username')})
	if session.get('username') in configs.admin:
		is_admin = True
	else:
		is_admin = False
	return newrender('title_contests', '', 'contests.html', 'contests', {'submit_list':submit_list, 'key_list':key_list, 'is_admin': is_admin, 'pagenow': page, 'pagel1': page-2, 'pagel2': page-1})
