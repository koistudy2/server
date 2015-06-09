# -*- coding: utf-8 -*-
# Logic Related to Uploading Files

from flask import session, request, Response
from functional import newrender
import configs
import dbhandler
import lang
import time
import base64

def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def upload():
	return newrender('title_user', '', 'upload.html')
	
def submitfile():
	prefix=str(time.time())
	file = request.files['file']
	if file and allowed_file(file.filename):
		fullname=prefix+file.filename
		dbfile = {
			'filename': fullname,
			'content': base64.b64encode(file.read())
		}
		dbhandler.col_uploads.insert_one(dbfile)
		return "File upload success, filename: "+fullname
	return "File upload error(No Files or not allowed file extension;png, jpg, jpeg, gif)"
#1433828525.6CG5DpT4UYAIYWHI.jpg	

def userfile(filename):
	if dbhandler.col_uploads.count({"filename": filename}):
		file = dbhandler.col_uploads.find_one({"filename": filename})
		return Response(base64.b64decode(file['content']),mimetype='image/png')
	else:
		return "File not Found!"
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	