from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

MDScreen:

    MDFlatButton:
        text: "Insert element"
        pos_hint: {"center_y": .9}

    MDFlatButton:
        text: "Delete element"
        pos_hint: {"center_y": .8}

    MDFlatButton:
        text: "Find position"
        pos_hint: {"center_y": .7}

    MDFlatButton:
        text: "Get element"
        pos_hint: {"center_y": .6}

    MDLabel:
        id: list
        text: app.list()

"""

class List_Functioning(MDApp):
    
    list = []

    def list(self):
        self.root.ids.list.text = self.list

    def insert_element(self):
        pass

    def build(self):
        return Builder.load_string(kv)

List_Functioning().run()