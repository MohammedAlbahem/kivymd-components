from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker


kv="""

BoxLayout:
	orientation: "vertical"
	
	MDToolbar:
		title: "Bottom Navigation"
		md_bg_color: 0, 0, 1, .2
		
	MDBottomNavigation:
	#	panel_color: 0, 0, 1, .1
		padding: 10
		
		MDBottomNavigationItem:
			name: "Screen 1"
			text: "Python"
			icon: "language-python"
			# badge_icon: "numeric-5"   # not working now in kivymd
			
			MDLabel:
				text: "Python content"
				halign: "center"
				font_size: 50
				
		MDBottomNavigationItem:
			name: "Screen 2"
			text: "C++"
			icon: "language-cpp"
			
			MDLabel:
				text: "C++ content"
				halign: "center"
				font_size: 50
				
		MDBottomNavigationItem:
			name: "Screen 3"
			text: "Java"
			icon: "language-java"
			
			MDLabel:
				text: "Java content"
				halign: "center"
				font_size: 50
				
		MDBottomNavigationItem:
			name: "Screen 4"
			text: "Time"
			icon: "clock"
			
			MDRaisedButton:
				text: "Open Time"
				pos_hint: {"center_x": .5, "center_y": .5}
				on_release: app.show_time()
				
			MDLabel:
				id: show_time
				text: "Time"
				pos_hint: {"center_x": .8, "center_y": .4}
				font_size: dp(50)
			
			#MDLabel:
			#	text: "Time"
			#	halign: "center"
				
		MDBottomNavigationItem:
			name: "Screen 5"
		#	text: "PHP"
			text: "Calendar"
			#icon: "language-php"
			icon: "calendar"
			#icon: "twitter"
			
		#	MDLabel:
			#	text: "PHP content"
		#		halign: "center"
		
			MDRaisedButton:
				text: "Open Date Picker"
				pos_hint: {"center_x": .5, "center_y": .5}
				on_release: app.show_date_picker()
		
			MDLabel:
				id: show_date
				text: "show date"
				pos_hint:  {"center_x": .7, "center_y": .4}
				font_size: dp(50)

"""

class Bottom_Navigation(MDApp):
	def build(self):
		#self.theme_cls.theme_style = "Light"
		#self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_string(kv)
		
	def show_date_picker(self):
		date=MDDatePicker()
		date.open()
		date.bind(on_save=self.date_save, on_cancel=self.date_cancel)
		
	def date_save(self, instance, value, date_range):
		self.root.ids.show_date.text = str(value)
		
	def date_cancel(self, instance, date_range):
		self.root.ids.show_date.text="You clicked cancel!"
		
	def show_time(self):
		time=MDTimePicker()
		time.open()
		time.bind(on_save=self.time_save, on_cancel=self.time_cancel)
		
	def time_save(self, instance, time):
		self.root.ids.show_time.text=str(time)
		
	def time_cancel(self, instance, time):
		self.root.ids.show_time.text="You clicked cancel!"
		
Bottom_Navigation().run()