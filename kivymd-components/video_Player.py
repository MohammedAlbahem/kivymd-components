from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


class Video_Player(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		
		video = VideoPlayer(source = "E:\VIDEO.mp4")
		video.state = "play"
		
		video.options = {"eos": "stop"}
		video.allow_stretch = True
		
		return video
		
Video_Player().run()