from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


def callbackTo2(instance):
    sm.current = "ScreenTwo"


def callbackTo1(instance):
    sm.current = "ScreenOne"


class ScreenRoot(Screen):
    def __init__(self, *args):
        super(ScreenRoot, self).__init__(name='ScreenOne')
        grid_root = GridLayout(rows=10)
        grid = GridLayout(cols=6)
        grid.add_widget(Button(text='Screen Two\n->', size_hint=(.15, 0), on_press=callbackTo2))
        grid.add_widget(TextInput())
        grid2 = GridLayout(cols=6)
        grid2.add_widget(Button(text='Screen Two\n->', size_hint=(.15, 0), on_press=callbackTo2))
        grid2.add_widget(TextInput())
        grid_root.add_widget(grid)
        grid_root.add_widget(grid2)
        self.add_widget(grid_root)


class ScreenTwo(Screen):
    def __init__(self, *args):
        super(ScreenTwo, self).__init__(name='ScreenTwo')
        self.add_widget(Button(text='Screen One\n->', size_hint=(0.15, 0.1), on_press=callbackTo1,
                               pos_hint={"x": 0.00, "top": 0.1}))


class ScreenAddDev(Screen):
    def __init__(self, *args):
        super(ScreenAddDev, self).__init__(name='ScreenTwo')
        self.add_widget(Button(text='Screen One\n->', size_hint=(0.15, 0.1), on_press=callbackTo1,
                               pos_hint={"x": 0.00, "top": 0.1}))


sm = ScreenManager()


class ScreenApp(App):
    def build(self):
        sm.add_widget(ScreenRoot())
        sm.add_widget(ScreenTwo())
        return sm


if __name__ == '__main__':
    app = ScreenApp()
    app.run()
