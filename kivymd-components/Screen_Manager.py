from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kv = """

Screen_Manager:
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: "first"

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: "First Screen"

        Button:
            text: "go to second window"
            on_release: 
                app.root.current = "second"
                # root.manager.transition.direction = "left"
                root.manager.transition.direction = "up"

<SecondScreen>:
    name: "second"

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: "Second Screen"

        Button:
            text: "go to first window"
            on_release: 
                app.root.current = "first"
                # root.manager.transition.direction = "right"
                root.manager.transition.direction = "down"

"""

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class Screen_Manager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return Builder.load_string(kv)

MainApp().run()

