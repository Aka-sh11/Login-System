from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

# set window size
Window.size = (300, 450)
KV = '''
Screen:

    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 35
        orientation: 'vertical'
        MDIcon:
            icon: 'account'
            icon_color: 0, 0, 0, 0
            halign: 'center'
            font_size: 180
        MDTextFieldRound:
            id: user
            icon_left: "account-check"
            hint_text: "Username"
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: password
            icon_left: "key-variant"
            hint_text: "Password"
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width: 220
            font_size: 20            
            pos_hint: {"center_x": 0.5}
            password: True
        MDFillRoundFlatButton:
            text: "LOG IN"
            font_size: 15
            pos_hint: {"center_x": 0.5}
            on_press: app.login()
'''


class LoginApp(MDApp):
    dialog = None

    def build(self):
        # define theme colors
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        # load and return kv string
        return Builder.load_string(KV)

    def login(self):
        # check entered username and password
        if self.root.ids.user.text == 'admin' and self.root.ids.password.text == 'admin123':
            if not self.dialog:
                # create dialog
                self.dialog = MDDialog(
                    title="Log In",
                    text=f"Welcome {self.root.ids.user.text}!",
                    buttons=[
                        MDFlatButton(
                            text="Ok", text_color=self.theme_cls.primary_color,
                            on_release=self.close
                        ),
                    ],
                )
            # open and display dialog
            self.dialog.open()

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()


# run app
LoginApp().run()
