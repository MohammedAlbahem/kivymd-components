from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

MDScreen:
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "MDNavigationDrawer"
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["magnify", lambda z: nav_drawer.set_state("open")], ["dots-vertical", lambda y: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            
"""

class Navigation_Drawer(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)

Navigation_Drawer().run()