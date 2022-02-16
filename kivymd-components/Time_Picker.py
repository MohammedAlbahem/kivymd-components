from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDTimePicker

kv="""

MDScreen:
	MDRaisedButton:
		text: "Open Time"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.show_time()
		
	MDLabel:
		id: show_time
		text: "Time"
		pos_hint: {"center_x": .95, "center_y": .45}

"""

class Time_PickerApp(MDApp):
	def build(self):
		return Builder.load_string(kv)
		
	def show_time(self):
		time=MDTimePicker()
		time.open()
		time.bind(on_save=self.time_save, on_cancel=self.time_cancel)
		
	def time_save(self, instance, time):
		self.root.ids.show_time.text=str(time)
		
	def time_cancel(self, instance, time):
		self.root.ids.show_time.text="You clicked cancel!"
		
Time_PickerApp().run()