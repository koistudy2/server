#Logic Related to probs.html

@app.route('/probs')
def probs():
	submit_list = [{'num'			: '1',
					'verdict'		: 'AC',
					'unique_id'		: 'TEST_1',
					'display_name'	: 'Hello World',
					'solved' 		: '1',
					'submits'		: '1',
					'diff'			: '1'},
				   {'num'			: '2',
					'verdict'		: 'WA',
					'unique_id'		: 'TEST_2',
					'display_name'	: 'Goodbye Cruel World',
					'solved'		: '4',
					'submits'		: '4444',
					'diff'			: '9'} ];
	key_list = [('num','Number'), ('verdict','Verdict'), ('display_name','Name'),
		('solved','Solved'), ('tried','Tried'), ('diff','Diff')]

	return newrender('title_probs', '', 'probs.html', 'probs', {'submit_list':submit_list, 'key_list':key_list})
