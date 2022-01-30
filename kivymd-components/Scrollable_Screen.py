from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size=(400,600)

kv="""

MDScreen:
	ScrollView:
		size: root.size
			
		GridLayout:
			size_hint_y: None
            height: self.minimum_height
            width: self.minimum_width
            cols: 2
            spacing: 20
            padding: 20

			MDCard:
				radius: [20, 20, 20, 20]
				elevation: 20
				size_hint_y: None
				height: 300
					
			MDCard:
				radius: [20, 20, 20, 20]
				elevation: 20
				size_hint_y: None
				height: 300

			MDCard:
				radius: [20, 20, 20, 20]
				elevation: 20
				size_hint_y: None
				height: 300
					
			MDCard:
				radius: [20, 20, 20, 20]
				elevation: 20
				size_hint_y: None
				height: 300
				
			MDCard:
				radius: [20, 20, 20, 20]
				elevation: 20
				size_hint_y: None
				height: 300
					
			MDCard:
				radius: [20, 20, 20, 20]
				elevation: 20
				size_hint_y: None
				height: 300

"""

class Scrollable_Screen(MDApp):
	def build(self):
		self.theme_cls.theme_style ="Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_string(kv)
		
Scrollable_Screen().run()