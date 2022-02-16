from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty

kv = """

MDBoxLayout:
    padding: 80
    MDProgressBar:
        id: progress
        orientation: "vertical"
        value: 10
        type: "indeterminate"
        # type: "determinate"
        running_duration: 1
        catching_duration: 1.5

    MDRaisedButton:
        text: "STOP" if app.state == "start" else "START"
        pos_hint: {"center_x": .5, "center_y": .45}
        on_press: app.state = "stop" if app.state == "start" else "start"
        
"""

class Progress_Bar(MDApp):

    state = StringProperty("stop")

    def on_state(self, instance, value):
        {
            "start": self.root.ids.progress.start,
            "stop": self.root.ids.progress.stop,
        }.get(value)()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)

Progress_Bar().run()