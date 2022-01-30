from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel

kv = """

MDScreen:
    MDCircularLayout:
        id: container
        pos_hint: {"center_x": .5, "center_y": .5}
        row_spacing: min(self.size)*0.1

"""

class Circular_Layout(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        for x in range(1,49):
            self.root.ids.container.add_widget(MDLabel(text = f"{x}"))

Circular_Layout().run()