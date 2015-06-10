from flask import session,render_template

import configs
import lang

def newrender(title, content='', filename='_basic.html', mode='', data={'is_admin': False}):
	if 'locale' in session and session['locale']:
		locale = session['locale']
	else:
		locale = 'ko'
	data['is_admin'] = session.get('username') in configs.admin
	return render_template(filename, title=configs.t_prefix + ' - ' + lang.lang[locale][title], content=content, lang=lang.lang[locale], menus=configs.menus, session=session, mode=mode, data=data, lang_now=locale)
