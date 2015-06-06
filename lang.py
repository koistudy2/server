# -*- coding: utf-8 -*-
import re

lang = {}
with open('./lang.txt') as f:
	lines = f.readlines()
for line in lines:
	each = re.match('([^.]+)\.([^=]+)=(.*)\n', line)
	if each:
		if not (each.group(2)) in lang:
			lang[each.group(2)] = {}
		lang[each.group(2)][each.group(1)] = each.group(3)
        

