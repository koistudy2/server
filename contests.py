#Logic Related to contests.html

from flask import session
from functional import newrender
import configs
import dbhandler
from math import ceil

def contests(page=1):
	page -= 1
	contest_list = dbhandler.col_contests.find().skip(page * configs.contests_per_page).limit(configs.contests_per_page)
	contest_count = contest_list.count()
	if 'username' in session and session['username']:
		user=session['username']
	else:
		user=''
	key_list = [('contest_id','Code'), ('display_name','Name'), ('starts','Starts'), ('ends','Ends'),('duration','Duration'),('type','Type')]
	is_admin = (user in configs.admin)
	lastpage = ceil(1.0 * contest_count / configs.contests_per_page)
	page += 1
	if lastpage >= page+3:
		pager1 = page+1
		pager2 = page+2
		pager3 = page+3
	elif lastpage >= page+2:
		pager1 = page+1
		pager2 = page+2
		pager3 = 0
	elif lastpage >= page+1:
		pager1 = page+1
		pager2 = 0
		pager3 = 0
	else:
		pager1 = 0
		pager2 = 0
		pager3 = 0
	return newrender('title_contests', '', 'contests.html', 'contests',
		{'contest_list':contest_list, 'key_list':key_list, 'is_admin': is_admin, 'pagenow': page,
		'pagel0' : page-3, 'pagel1' : page-2, 'pagel2' : page-1,
		'pager1' : pager1, 'pager2' : pager2, 'pager3' : pager3})