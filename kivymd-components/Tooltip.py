from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

<TooltipMDIconButton@MDIconButton+MDTooltip>

MDScreen:

    TooltipMDIconButton:
        # the behaviour of Tooltip on desktop and mobile phones is different
        icon: "language-python"
        # tooltip_text: self.icon
        tooltip_text: "Python"
        pos_hint: {"center_x": .5, "center_y": .5}
        # tooltip_radius: [5,5,5,5]  # makes the corners round
        # tooltip_display_delay: 0  # displays the tooltip after specified time min: 0 and max: 4
        # shift_y: 80   # displays the tooltip in a given shift
        

"""

class Tooltip(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)

Tooltip().run()