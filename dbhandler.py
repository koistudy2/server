# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
dbclient = MongoClient('localhost', 27017)
db = dbclient.db_main

col_members = db.members
col_logs = db.logs
col_probs = db.probs
col_contests = db.contests
col_descs = db.descs
col_judges = db.judges