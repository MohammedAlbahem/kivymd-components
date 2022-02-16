from kivymd.app import MDApp
from kivy.lang import Builder

kv = """



"""

class MainApp(MDApp):
     
     def build(self):
          self.theme_cls.theme_style = "Dark"
          self.theme_cls.primary_palette = "BlueGray"
          return Builder.load_string(kv)

if __name__ == "__main__":
     MainApp().run()