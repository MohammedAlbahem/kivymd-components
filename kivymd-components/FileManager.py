from re import search
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivymd.toast import toast

kv = """

MDBoxLayout:
     orientation: "vertical"

     MDToolbar:
          title: "MDFileManager"
          elevation: 10
          left_action_items: [["menu", lambda x: None]]

     MDFloatLayout:
          MDIconButton:
               icon: "folder"
               user_font_size: dp(50)
               pos_hint: {"center_x": .5, "center_y": .5}
               on_release: app.file_manage_open()

"""

class MainApp(MDApp):

     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          Window.bind(on_keyboard = self.events)
          self.open_file_manager = False
          self.file_manager = MDFileManager(
               exit_manager = self.exit_manager,
               select_path = self.select_path,
               # preview = True,
               # search = ("all"),
               # use_access = True,
               
          )

     def file_manage_open(self):
          self.file_manager.show("/")
          self.open_file_manager = True

     def exit_manager(self):
          self.open_file_manager = False
          self.file_manager.close()

     def select_path(self, path):
          self.exit_manager()
          # toast(path)

     def events(self, instance, keyboard, keycode, text, modifiers):
          if keyboard in (1001, 27):
               if self.open_file_manager:
                    self.file_manager.back()
          return True

     def build(self):
          self.theme_cls.theme_style = "Dark"
          self.theme_cls.primary_palette = "BlueGray"

          return Builder.load_string(kv)

if __name__ == "__main__":
     MainApp().run()