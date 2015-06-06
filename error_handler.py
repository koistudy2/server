#Logic Related to error handler

from functional import newrender

def error_404(error):
        return newrender("title_404", "404 Not Found")

def error_500(error):
        return newrender("title_500", error)
