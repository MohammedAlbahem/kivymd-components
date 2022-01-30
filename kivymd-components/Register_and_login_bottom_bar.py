from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

Window.size = (400,550)

kv = """

MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Bottom Navigation"

        MDBottomNavigation:

            MDBottomNavigationItem:
                name: "Screen 1"
                icon: "account-circle"
                text: "Create Account"

                # MDCard can not be centered in GridLayout

                # GridLayout:
                #     size_hint_y: None
                #     height: self.minimum_height
                #     width: self.minimum_width
                #     cols: 1
                #     padding: 20
                #     spacing: 20

                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: 350, 420
                    pos_hint: {"center_x": .5, "center_y": .5}
                    elevation: 20
                    radius: [20,20,20,20]
                    padding: 20
                    spacing: 10

                    MDLabel:
                        text: "Create Account"
                        id: login_label
                        font_size: 30
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDTextField:
                        id: username
                        icon_right: "account"
                        hint_text: "username"
                        line_color_focus: 0,0,0,1  # changes the text color
                        mode: "rectangle"  # rectangle text
                        # helper_text_mode: "on_focus" # "this field is required" will be shown 
                        # helper_text_mode: "on_error"  # "this field is required" will be shown if wrong input is given
                        # required: True   # if True then helper_text wil shown on_focus 
                        # max_text_length: 5   # fixing the length of text field
                        # helper_text: "this field is required"
                        # multiline: True  # this will make text field multiliner
                        # mode: "fill"
                        # icon_right: "eye"   # will show icon on right side of the text field
                        # size_hint: 1, None    # not working size_hint and height
                        # height: "30dp"
                        # readonly: True    # readonly property makes it uneditable

                    MDTextField:
                        id: email
                        icon_right: "gmail"
                        hint_text: "email"
                        mode: "rectangle"
                        helper_text_mode: "on_error"
                        line_color_focus: 0,0,0,1  # changes the text color

                    MDTextField:
                        id: create_password
                        icon_right: "lock"
                        hint_text: "create-password"
                        helper_text_mode: "on_error"
                        password: True
                        mode: "rectangle"
                        line_color_focus: 0,0,0,1  # changes the text color

                    MDTextField:
                        id: confirm_password
                        icon_right: "lock"
                        hint_text: "confirm-password"
                        helper_text_mode: "on_error"
                        password: True
                        mode: "rectangle"
                        line_color_focus: 0,0,0,1  # changes the text color

                    MDRoundFlatButton:
                        text: "Create Account"
                        pos_hint: {"center_x": .5}
                        on_release: app.create_account()

                    MDRoundFlatButton:
                        text: "Clear"
                        pos_hint: {"center_x": .5}
                        on_release: app.clear()

            MDBottomNavigationItem:
                name: "Screeen 2"
                icon: "login"
                text: "Login"

                MDCard:
                    orientation: "vertical"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    elevation: 20
                    padding: 20
                    spacing: 10
                    radius: [20,20,20,20]
                    size_hint: None, None
                    size: 350, 420

                    MDLabel:
                        text: "Login"
                        font_size: 30
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDTextField:
                        id: username_login
                        hint_text: "username"
                        mode: "rectangle"
                        helper_text_mode: "on_error"
                        line_color_focus: 0,0,0,1
                        icon_right: "account"
                    
                    MDTextField:
                        id: password
                        hint_text: "password"
                        mode: "rectangle"
                        helper_text_mode: "on_error"
                        line_color_focus: 0,0,0,1
                        icon_right: "eye"
                        password: True

                    MDRoundFlatButton: 
                        text: "Login"
                        pos_hint: {"center_x": .5}
                        on_release: app.login_account()

                    MDRoundFlatButton:
                        text: "Clear"
                        pos_hint: {"center_x": .5}
                        on_release: app.clear_login_info()

                    MDTextButton:
                        text: "Forgot password?"
                        font_size: 12
                        pos_hint: {"center_x": .5}

                    Widget:
                        size_hint: 1, None
                        height: 60
                    
"""

class Register_and_login(MDApp):
    
    def create_account(self):
        import mysql.connector
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "amrat26728"
        )
        cursor = db.cursor()
        cursor.execute("use first_db;")
        cursor.execute('insert into 19sw values("{self.root.ids.username.text}","{self.root.ids.email.text}","{self.root.ids.create_password.text}";')
        print("Your account is successfuly created.")

    def login_account(self):
        pass

    def Clear_create_account_dialog(self, obj):
        pass

    def clear_logged_in_dialog(self, obj):
        pass

    def clear(self):
        self.root.ids.username.text = ""
        self.root.ids.email.text = ""
        self.root.ids.create_password.text = ""
        self.root.ids.confirm_password.text = ""

    def clear_login_info(self):
        self.root.ids.username_login.text = ""
        self.root.ids.password.text = ""

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)

Register_and_login().run()