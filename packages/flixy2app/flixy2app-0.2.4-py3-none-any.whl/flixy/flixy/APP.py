from .PAGE import Page
import flet
import threading


class app (object):
	
	def __init__ (self, target, develop=True, web_port=8000, based_file="", view=""):
		ThePage = Page()
		ThePage.show(target)