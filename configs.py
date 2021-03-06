# -*- coding: utf-8 -*-

#configs
debugMode = True #디버그
s_prefix = './static/' #static 파일 디렉토리:
menus = [{'name': 'Probs', 'url': 'probs'},
	{'name': 'Status', 'url': 'status'},
	{'name': 'Ranks', 'url': 'ranks'},
	{'name': 'Contests', 'url': 'contests'},
	{'name': 'Board', 'url': 'board'},
	{'name': 'Stats', 'url': 'stats'}]
t_prefix = 'KOISTUDYS2' #title prefix
default_url = 'https://koistudy2.0101010101.com' #no slash, please

probs_per_page = 20
contests_per_page = 20
admin = ['hletrd', 'hletrd002', 'Namnamseo', 'koosaga', 'HYEA', 'seungwonpark']
langs = ['ko', 'en']
max_upload = 100 * 1024 * 1024
bcrypt_round = 12 #4096(2^12) iterations

execfile('secretconfig.py')
#recaptcha_secret, gmail_id, gmail_pw have to be defined

#configure DB in dbhandler.py
