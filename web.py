# -*- coding: utf-8 -*-
from flask import Flask, session, request
import os.path #file exists
import random
import string

#custom modules
import lang
import configs
import dbhandler

#make context
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = configs.max_upload

#to suppress unicodedecodeerror
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#session setup
app.secret_key = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(32))

@app.before_request
def initApp():
	if not 'locale' in session or not session['locale']:
		session['locale'] = request.accept_languages.best_match(['ko', 'en']) or 'ko'

import index
app.route('/')(index.index)

import signup
app.route('/signup')(signup.signup)
app.route('/signup/submit', methods=['POST'])(signup.signup_submit)
app.route('/confirm/resend')(signup.resend)
app.route('/confirm/<path:path>')(signup.confirm)

import login
app.route('/login')(login.login)
app.route('/login/submit', methods=['POST'])(login.login_submit)
app.route('/logout')(login.logout)

import static
app.route('/static/<path:path>')(static.static_files)

import robots
app.route('/robots.txt')(robots.robots)
app.route('/humans.txt')(robots.humans)

import error_handler
app.errorhandler(404)(error_handler.error_404)
app.errorhandler(500)(error_handler.error_500)

import stats
app.route('/stats')(stats.stats)

import probs
app.route('/probs')(probs.probs)
app.route('/probs/<int:page>')(probs.probs)

import user
app.route('/user')(user.user)
app.route('/changeuser')(user.changeuser)
app.route('/changeuser/submit', methods=['POST'])(user.changeuser_submit)
app.route('/findacc')(user.findacc)
app.route('/findacc/submit', methods=['POST'])(user.findacc_submit)

import viewprob
app.route('/viewprob/<probid>')(viewprob.viewprob)
app.route('/settheme/<theme>')(viewprob.settheme)

import submit
app.route('/submit/<probid>', methods=['POST'])(submit.submit)

import addprob
app.route('/addprob')(addprob.addprob)
app.route('/addprob/submit', methods=['POST'])(addprob.addprob_submit)

import changelang
app.route('/changelang/<lang>')(changelang.changelang)

import upload
app.route('/upload')(upload.upload)
app.route('/upload/submit', methods=['POST'])(upload.submitfile)
app.route('/uploads/<filename>')(upload.userfile)

import editprob
app.route('/editprob/<probid>')(editprob.editprob)
app.route('/editprob/<probid>/submit',methods=['POST'])(editprob.editprob_submit)

import contests
app.route('/contests')(contests.contests)

import addcontest
app.route('/addcontest')(addcontest.addcontest)
app.route('/addcontest/submit',methods=['POST'])(addcontest.addcontest_submit)

if __name__ == '__main__':
	app.run(debug=configs.debugMode, port=5000)
