import flet

class Audio (object):
	def __init__ (self, src="https://luan.xyz/files/audio/ambient_c_motion.mp3"):
		self.__self = flet.Audio(src=f"{src}", autoplay=False)
		self.__src = src
		self.page = None
		
		# actions
		self.on_duration_changed = None
		
	def play(self):
		if self.page == None:
			raise OSError("There must be a page.")
		if self.__self.page == None:
			print("Pass warning: page not found, you cant play the audio.")
			return
		self.__self.play()
	
	def pause (self):
		self.__self.pause()
	
	def current_time(self):
		return self.__self.get_current_position()
		
	def respown (self, page):
		self.page = page
		page.self_ui.overlay.append(self.__self)
		page.update()
	
	def get_full_time (self):
		return self.__self.get_duration()