KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDNavigationLayout:
        id: nav_layout
        MDScreenManager:
            id: manager_screens

        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(16), dp(16), 0
            MDNavigationDrawerMenu:

                MDNavigationDrawerLabel:
                    text: "КриптоБлять"

                MDNavigationDrawerItem:
                    on_release: app.change("main screen")

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account"

                    MDNavigationDrawerItemText:
                        text: "Главная страница"

                MDNavigationDrawerItem:
                    on_release: app.change("creat wallet screen")

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account-box-multiple"

                    MDNavigationDrawerItemText:
                        text: "Создание кошельков"


'''
# """
# Script for managing hot reloading of the project.
# For more details see the documentation page -
#
# https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/
#
# To run the application in hot boot mode, execute the command in the console:
# DEBUG=1 python main.pyf
# """
#
# import importlib
# import os
# import sys
#
# # os.environ['KIVY_NO_CONSOLELOG'] = '1'
#
# from kivy import Config
# from kivy.lang import Builder
#
# from PIL import ImageGrab
# from kivymd.uix.navigationdrawer import MDNavigationLayout
#
# # TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size
#
# # Change the values of the application window size as you need.
# # Config.set("graphics", "height", "800")
# # Config.set("graphics", "width", "300")
# Config.set('kivy', 'log_level', 'error')
#
# from kivy.core.window import Window
# from kivymd.icon_definitions import md_icons
#
# # Place the application window on the right side of the computer screen.
#
# Window.left = resolution[0]-1200
#
# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager
#
#
# class CriptoBlit(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]
#     DEBUG = 1
#
#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """
#
#         import View.screens
#         structs = Builder.load_string(KV)
#
#         self.manager_screens = MDScreenManager()
#         Window.bind(on_key_down=self.on_keyboard_down)
#         importlib.reload(View.screens)
#         screens = View.screens.screens
#
#         for i, name_screen in enumerate(screens.keys()):
#             model = screens[name_screen]["model"]()
#             controller = screens[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screens = structs.ids['manager_screens']
#             view.name = name_screen
#             structs.ids['manager_screens'].add_widget(view)
#
#         self.manager_screens = structs.ids['manager_screens']
#         self.nav_drawer = structs.ids['nav_drawer']
#
#         return structs
#
#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.
#
#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """
#
#         # if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#         #     self.rebuild()
#         if "meta" in modifiers or "alt" in modifiers:
#             self.rebuild()
#
#     def nav_drawer_open(self, *args):
#         self.nav_drawer.set_state("toggle")
#
#     def nav_drawer_close(self, *args):
#         self.nav_drawer.set_state("close")
#
#     def change(self, to=None):
#         if to:
#             self.manager_screens.current = to
#         # elif len(self.go_to) > 0:
#         #     self.sm.current = self.go_to[-1]
#         #     self.go_to.pop()
#
#         self.nav_drawer_close()
#
#
# CriptoBlit().run()


"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
from kivy import Config
from kivy.lang import Builder

Config.set('kivy', 'log_level', 'debug')

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer, MDNavigationDrawerMenu, \
    MDNavigationDrawerLabel, MDNavigationDrawerItem, MDNavigationDrawerItemLeadingIcon, MDNavigationDrawerItemText, \
    MDNavigationDrawerItemTrailingText
from kivymd.uix.screenmanager import MDScreenManager

from View.screens import screens

class CriptoBlit(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()
        self.structs = None

    def build(self) -> MDScreenManager:
        self.structs = Builder.load_string(KV)
        self.generate_application_screens()

        return self.structs

    def generate_application_screens(self) -> None:
        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.structs.ids['manager_screens']
            view.name = name_screen
            self.structs.ids['manager_screens'].add_widget(view)

        self.manager_screens = self.structs.ids['manager_screens']

    def nav_drawer_open(self, *args):
        self.root.ids['nav_drawer'].set_state("toggle")

    def nav_drawer_close(self, *args):
        self.root.ids['nav_drawer'].set_state("close")

    def change(self, to=None):
        if to:
            self.manager_screens.current = to
        # elif len(self.go_to) > 0:
        #     self.sm.current = self.go_to[-1]
        #     self.go_to.pop()

        self.nav_drawer_close()


if __name__ == "__main__":
    CriptoBlit().run()




