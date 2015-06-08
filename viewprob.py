#Logic Related to viewprob

from flask import session
from functional import newrender
import dbhandler

def viewprob(probid):
	prob = dbhandler.col_probs.find_one({"unique_id": probid})
	return newrender('title_viewprob','','viewprob.html','',{'prob':prob, 'session': session})
