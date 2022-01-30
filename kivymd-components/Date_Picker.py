from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivy.lang import Builder

kv="""

MDScreen:
	MDRaisedButton:
		text: "Open Date Picker"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.show_date_picker()
		
	MDLabel:
		id: show_date
		text: "show date"
		pos_hint:  {"center_x": .9, "center_y": .45}

"""


class Date_PickerApp(MDApp):
	def build(self):
		return Builder.load_string(kv)
		
	def show_date_picker(self):
		date=MDDatePicker()
		date.open()
		date.bind(on_save=self.on_save, on_cancel=self.on_cancel)
		
	def on_save(self, instance, value, date_range):
		self.root.ids.show_date.text = str(value)
		
	def on_cancel(self, instance, date_range):
		self.root.ids.show_date.text="You clicked cancel!"
		
Date_PickerApp().run()