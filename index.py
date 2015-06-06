#Logic related to /

from functional import newrender

def index():
	content = ''
	return newrender("title_main", "Sample Content")
