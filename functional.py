from flask import session,render_template

import configs
import lang

def newrender(title, content, filename='_basic.html', mode='', data=''):
	return render_template(filename, title=configs.t_prefix + ' - ' + lang.lang[session.get('locale', 'ko')][title], content=content, lang=lang.lang[session.get('locale', 'ko')], menus=configs.menus, session=session, mode=mode, data=data)
