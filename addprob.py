from flask import session, request
from functional import newrender
import configs
import dbhandler
import lang
import re
import httplib
import urllib
import json

def addprob():
	if (session.get('username') in configs.admin):
		return newrender("title_addprob", '', 'addprob.html')
	else:
		return newrender("title_404", "404 Not Found")

def addprob_submit():
	if (session.get('username') in configs.admin):
		if dbhandler.col_probs.count({"unique_id": request.form['uniqid']}):
			return newrender('title_addprob', filename='basic_display.html', mode='addprob_err_dup')
		else:
			if re.match('[0-9]+',request.form['tlimit']) and re.match('[0-9]+',request.form['mlimit']) and re.match('[^/]+', request.form['uniqid']):
				prob = {"unique_id": request.form['uniqid'], 
					"display_name": request.form['title'], 
					"by": request.form['by'], 
					"diff": request.form['diff'], 
					"adminonly" : ('adminonly' in request.form),
					"gshs" : ('gshs' in request.form), 
					"limit_time": int(request.form['tlimit']), 
					"limit_memory": int(request.form['mlimit']), 
					"desc": request.form['desc'], 
					"input": request.form['input'], 
					"output": request.form['output'], 
					"exin": request.form['input_ex'], 
					"exout": request.form['output_ex'], 
					'solved': 0, 'submits': 0, 'diff': 0}
				dbhandler.col_probs.insert_one(prob)

				#elasticsearch indexing
				#creating new index
				conn = httplib.HTTPConnection('localhost', 9200)
				conn.request("PUT", "/koistudy")
				res = conn.getresponse()
				result = res.read()

				#creating document
				params = urllib.urlencode(json.dumps(prob))
				conn = httplib.HTTPConnection('localhost', 9200)
				conn.request("POST", "/koistudy/probs/" + request.form['unique_id'], params)
				res = conn.getresponse()
				result = res.read()
				return newrender("title_addprob", filename='basic_display.html', mode='addprob_added')
			else:
				return newrender('title_addprob', filename='basic_display.html', mode='addprob_err_timemem')
	else:
		return newrender("title_404", "404 Not Found")
