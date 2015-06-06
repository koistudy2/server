# -*- coding: utf-8 -*-

#configs
debugMode = True #디버그
s_prefix = './static/' #static 파일 디렉토리:
menus = [{'name': 'Probs', 'url': 'probs'},
	{'name': 'Status', 'url': 'status'},
	{'name': 'Ranks', 'url': 'ranks'},
	{'name': 'Contests', 'url': 'contest'},
	{'name': 'Board', 'url': 'board'},
	{'name': 'Stats', 'url': 'stats'}]
t_prefix = 'KOISTUDYS2' #title prefix
default_url = 'https://koistudy2.0101010101.com' #no slash, please

execfile('secretconfig.py')
#recaptcha_secret, gmail_id, gmail_pw have to be defined

#configure DB in dbhandler.py
