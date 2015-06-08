from flask import session, redirect
import configs

def changelang(lang):
	if lang in configs.langs:
		session['locale'] = lang
	if 'username' in session:
		user = dbhandler.col_members.find_one({"username": session['username']})
		user['locale'] = lang
		dbhandler.col_members.update({'_id': user['_id']}, {"$set": user}, upsert=False)
	return redirect('/')