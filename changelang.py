from flask import session, redirect
import configs

def changelang(lang):
	if lang in configs.langs:
		session['locale'] = lang
		return 'true'
	return redirect('/')