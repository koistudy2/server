#Logic Related to static files

from error_handler import error_404

def static_files(path):
	if '.' in path:
		return error_404(0)
	if os.path.isfile(s_prefix + path):
		f = open(s_prefix + path)
		return f.read()
	else:
		return error_404(0)
