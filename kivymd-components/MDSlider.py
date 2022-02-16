from kivy.lang import Builder
from kivymd.app import MDApp


slider="""

MDScreen:
	MDSlider:
		id: slider
		min: 0
		max: 10
		pos_hint: {"center_x": .5, "center_y": .5}
		size_hint: .5, .1
		value: 2
		# hint: False  # this makes the hint above the slider bar point
		# active: False
		# hint_bg_color: [1,1,0,1]  # not working
		
	MDLabel:
		text: str(int(slider.value))
		pos_hint: {"center_x": .5, "center_y": .55}
		halign: "center"
		

"""


class MainApp(MDApp):
	def build(self):
		# self.theme_cls.theme_style = "Dark"
		# self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_string(slider)
		
		
MainApp().run()