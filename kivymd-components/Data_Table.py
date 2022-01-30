from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.label import MDLabel

class Data_Table(MDApp):
	def build(self):
		
		screen = Screen()
		
		self.label = MDLabel(text="selected data", pos_hint= {"center_x": .7, "center_y": .2})
		screen.add_widget(self.label)
		
		table = MDDataTable(
			size_hint=(.8, .5),
			pos_hint={"center_x": .5, "center_y": .5},		
			use_pagination = True,
			check = True,
			rows_num = 10,
			column_data=[
			("First Name", dp(30)),
			("Last Name", dp(30)),
			("Email", dp(30)),
			("Phone Number", dp(30))
			],
			row_data = [
			("Amrat", "Meriya", "amratamrat2000@gmail.com", "03123183066"),
			("Jairam", "Meriya", "jairamjairam1996@gmail.com", "03131163928"),
			("Shankar", "Meriya", "jairamjairam1996@gmail.com", "03131163928"),
			("Haresh", "Meriya", "jairamjairam1996@gmail.com", "03131163928"),
			("Anna", "Meriya", "jairamjairam1996@gmail.com", "03131163928"),
			("Raju", "Meriya", "jairamjairam1996@gmail.com", "03131163928"),
			("Preet", "Meriya", "jairamjairam1996@gmail.com", "03131163928"),
			("Vijay", "Meriya", "jairamjairam1996@gmail.com", "03131163928")
			],
		
		)
		
		table.bind(on_check_press = self.checked)
		table.bind(on_row_press = self.row_checked)
		
		screen.add_widget(table)
		
		#self.theme_cls.theme_style = "Dark"
		#self.theme_cls.primary_palette = "BlueGray"
		return screen
		
	def checked(self, instance_table, current_row):
		#self.label.text=str(instance_table)
		# self.label.text=str(current_row)
		print(instance_table, current_row)
		
	def row_checked(self, instance_table, instance_row):
		#self.label.text = str(instance_table)
		# self.label.text = str(instance_row)
		print(instance_table, instance_row)
		
Data_Table().run()