# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
dbclient = MongoClient('localhost', 27017)
db_members = dbclient.members
