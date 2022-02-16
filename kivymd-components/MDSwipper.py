from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

<MySwiper@MDSwiperItem>
     FitImage:
          source: "D:/Python/KivymdApps/Photos/1.jpg"
          radius: [20, ]

MDScreen:
     MDToolbar:
          id: toolbar
          title: "Swiper App"
          elevation: 10
          pos_hint: {"top": 1}

     MDSwiper:
          size_hint_y: None
          height: root.height - toolbar.height - dp(20)
          y: root.height - self.height - toolbar.height - dp(20)

          MySwiper:
          
          MySwiper:
               
          MySwiper:

          MySwiper:

          MySwiper:

"""

class MainApp(MDApp):

     def build(self):
          self.theme_cls.theme_style = "Dark"
          self.theme_cls.primary_palette = "BlueGray"
          return Builder.load_string(kv)

if __name__ == "__main__":
     MainApp().run()