from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

MDFloatLayout:

    MDCheckbox:
        size_hint: None, None
        size: dp(40), dp(40)
        pos_hint: {"center_x": .5, "center_y": .4}
        on_active: app.on_active(*args)

    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(40), dp(40)
        pos_hint: {"center_x": .5, "center_y": .5}

        # determinate makes it rotate contineous or not
        determinate: True
        # determinate_time: 5
        # line_width: 5  # increases the width of spinner
        # color: [1,1,1,1]  # controls the color spinner

        # palette:   # changes the color of spinner in every complete circle
        #     [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1], \
        #     [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1], \
        #     [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1], \
        #     [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],

        # active makes visible and invisible
        active: False

"""

class Md_Spinner(MDApp):

    def on_active(self, chekcbox, value):
        if value:
            self.root.ids.spinner.active = True
        else:
            self.root.ids.spinner.active = False

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)

Md_Spinner().run()