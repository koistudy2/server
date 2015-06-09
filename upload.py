# -*- coding: utf-8 -*-
# Logic Related to Uploading Files

from flask import session, send_file, make_response, request
from functional import newrender
import configs
import dbhandler
import lang
import random
import string
import os
import error_handler

def upload():
	if 'username' in session and session['username'] in configs.admin:
		return newrender('title_file', '', 'upload.html')
	else:
		return error_handler.error_404(0)
	
def submitfile():
	if 'username' in session and session['username'] in configs.admin:
		filename_saved = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
		while dbhandler.col_uploads.count({"filename_saved": filename_saved}):
			filename_saved = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
		file = request.files['file']
		if file:
			filename_real=file.filename
			file.save('./uploads/' + filename_saved)
			dbfile = {
				'filename_real': filename_real,
				'filename_saved': filename_saved,
				'size': os.path.getsize('./uploads/' + filename_saved)
			}
			dbhandler.col_uploads.insert_one(dbfile)
			return newrender('title_file', '', 'upload_result.html', '', {'url': configs.default_url + '/uploads/' + filename_saved})
		return newrender('title_file', 'Error')
	else:
		return error_handler.error_404(0)

def userfile(filename):
	if dbhandler.col_uploads.count({"filename_saved": filename}):
		f = dbhandler.col_uploads.find_one({"filename_saved": filename})
		return send_file('./uploads/' + filename, None, True, f['filename_real'])
		#response = make_response(f.read())
		#response.headers['Content-Type'] =  'application/octet-stream'
		#response.headers['Content-Transfer-Encoding'] = 'Binary'
		#response.headers['Content-Length'] = file['size']
		#response.headers['Content-Disposition'] = 'attachment; filename="' + file['filename_real'] + '"'
		#return response
	else:
		return error_handler.error_404
	