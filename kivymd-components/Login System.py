from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400, 600)

kv="""
MDScreen:
	
	MDCard:
		size_hint: None,None
		size: 350,500
		orientation: "vertical"
		radius: [20,20,20,20]
		pos_hint: {"center_x": .5, "center_y": .5}
		elevation: 25
		spacing: 30
		padding: 20
		
		MDLabel:
			id: title
			text: "Welcome"
			font_size: 40
			halign: "center"
			size_hint_y: None
			height: self.texture_size[1]
			
		MDTextFieldRound:
			id: username
			hint_text: "username"
			icon_right: "account"
			size_hint_x: None
			width: 300
			pos_hint: {"center_x": .5}
			
		MDTextFieldRound:
			id: password
			hint_text: "password"
			icon_right: "eye-off"
			password: True
			size_hint_x: None
			width: 300
			pos_hint: {"center_x": .5}
			
		MDRoundFlatButton:
			text: "Login"
			font_size: 20
			pos_hint: {"center_x": .5}
			on_release: app.login()
			
		MDRoundFlatButton:
			text: "Clear"
			font_size: 20
			pos_hint: {"center_x": .5}
			on_release: app.clear()
			
		Widget:
			size_hint_y: None
			height: 100
	
"""


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style="Dark"
		self.theme_cls.primary_palette="BlueGray"
		return Builder.load_string(kv)
		
	def login(self):
		self.root.ids.title.text=f"Welcome {self.root.ids.username.text}"
		
	def clear(self):
		self.root.ids.title.text="Welcome"
		self.root.ids.username.text=""
		self.root.ids.password.text=""
		
		
MainApp().run()