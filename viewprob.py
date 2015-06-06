#Logic Related to viewprob

@app.route('/viewprob/<probid>')
def viewprob(probid):
	prob = 			{'num'			: '1',
					'verdict'		: 'AC',
					'unique_id'		: 'TEST_1',
					'display_name'	: 'Hello World',
					'solved' 		: '1',
					'submits'		: '1',
					'diff'			: '1',
					'limit_time'	: '1000y',
					'champion'		: 'gs15067'
					}
	desc  = {'description'	: 'Sample description',
			'input'			: 'Sample input',
			'output'		: 'Sample output',
			'exin'			: 'Sample input example',
			'exout'			: 'Sample output example' }
	#desc = dbhandler.col_descs.find_one({"unique_id": probid})
	#prob = dbhandler.col_probs.find_one({"unique_id": probid})
	return newrender('title_viewprob','','viewprob.html','',{'prob':prob, 'desc':desc, 'session': session})
