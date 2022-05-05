from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        reg_layout = AnchorLayout()
        btn_layout = BoxLayout(orientation='horizontal', size_hint=[.80, .30], spacing=40, padding=[0,100,0,50])
        lbl_layout = BoxLayout(orientation='vertical',  size_hint=[.80, .50], spacing=20, padding=[0,0,0,150])

        lbl_reg = Label(text='login\n\n')
        lbl_pas = Label(text='password')

        reg_button = Button(text="Зарегестрироваться", background_color=[1, 0, 0, 26])
        password_button = Button(text="Забыли пароль?", background_color=[1, 0, 0, 1])

        lbl_layout.add_widget(TextInput())
        lbl_layout.add_widget(TextInput())

        btn_layout.add_widget(reg_button)
        btn_layout.add_widget(password_button)

        reg_layout.add_widget(lbl_layout)
        reg_layout.add_widget(btn_layout)

        return reg_layout


if __name__ == '__main__':
    MyApp().run()


