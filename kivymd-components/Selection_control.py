# MDCheckbox and MDSwitch both are used for selection controls
from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

# MDCheckbox without group
# MDCheckbox:
#     size_hint: None, None
#     size: dp(48), dp(48)
#     pos_hint: {"center_x": .5, "center_y": .7}
#     on_active: app.on_checkbox_active(*args)

# MDCheckbox with group
<Check@MDCheckbox>:
    group: "group"
    size_hint: None, None
    size: dp(48), dp(48)

MDFloatLayout:

    MDCheckbox:
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {"center_x": .5, "center_y": .7}
        on_active: app.on_checkbox_active(*args)


    Check:
        pos_hint: {"center_x": .4, "center_y": .5}

    Check: 
        pos_hint: {"center_x": .45, "center_y": .5}

    Check: 
        pos_hint: {"center_x": .5, "center_y": .5}

    Check: 
        pos_hint: {"center_x": .55, "center_y": .5}

    MDFloatLayout:
        MDSwitch:
            pos_hint: {"center_x": .5, "center_y": .4}
            # width: dp(100)  # increase the width of MDSwitch

"""

class Md_Check_box(MDApp):


    # MDCheckbox without group
    def on_checkbox_active(self, checkbox, value):
        if value:
            # states may be down or normal
            print(value)
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            # states may be down or normal
            print(value)
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)

Md_Check_box().run()