from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

MDScreen:
	MDLabel:
		id: show_data
		text: "Show stuff"
		halign: "center"
		
	MDFloatingActionButtonSpeedDial:
		data: app.data
		# root_button_anim: True
		hint_animation: True
		on_open: app.open()
		on_close: app.close()
		callback: app.callback
		# colors
		#label_text_color: 1, 0, 0, 1
		#bg_color_stack_button: 1, 0, 0, 1
		#color_icon_stack_button: 1, 0, 0, 1
		#bg_color_root_button: 1, 0, 0, 1
		#color_icon_root_button: 1, 0, 0, 1
		#bg_hint_color: 1, 0, 0, 1

"""

class Speed_Dial(MDApp):
	data = {
	"Python": "language-python",
	"C++": "language-cpp",
	"Java": "language-java"
	}
	
	def callback(self, instance):
		if instance.icon=="language-python":
			lang = "Python"
			
		elif instance.icon == "language-cpp":
			lang = "C++"

		else:
			lang = "Java"
			
		self.root.ids.show_data.text = f"you clicked on {lang}"
		
	def open(self):
		self.root.ids.show_data.text = "Open!"
	
	def close(self):
		self.root.ids.show_data.text = "Close!"
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_string(kv)
		
Speed_Dial().run()