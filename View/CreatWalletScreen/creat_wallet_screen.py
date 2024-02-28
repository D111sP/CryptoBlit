import os

import asynckivy
from kivy.metrics import dp

from View.base_screen import BaseScreenView
from kivy.properties import StringProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

class CreatWalletScreenView(BaseScreenView):

    def __init__(self, **kwargs):
        super(CreatWalletScreenView, self).__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path, selector="folder", search="dirs"
        )

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        wallets = self.model.created_wallets
        self.show_items_wallets(wallets)

    def generate_wallets(self):
        self.controller.generate_wallets()

    def save_wallets(self):
        if not self.model.busy or not self.model.len_created_wallets:
            self.file_manager.show(
                os.path.expanduser("~"))  # output manager to the screen
            self.manager_open = True
        else:
            self.controller.show_allert_message("Ну бля или занят процесс или кошельки создай")



    def set_number_of_wallets(self, value):
        self.controller.set_number_of_wallets(int(value))

    def set_len_seed_phrase(self, value):
        self.ids.len_seed_phrase.text = f"Количество мемо слов: {str(value)}"
        self.controller.set_len_seed_phrase(int(value))
        self.menu_len_seed_phrase.dismiss()
        del self.menu_len_seed_phrase

    def open_len_seed_phrase(self, item):

        menu_items = [
            {
                "text": f"{el}",
                "on_release": lambda x=el: self.set_len_seed_phrase(x)
            } for el in [12, 15, 18, 21, 24]
        ]

        self.menu_len_seed_phrase = MDDropdownMenu(caller=item, items=menu_items)
        self.menu_len_seed_phrase.open()

    def show_items_wallets(self, wallets):

        def show_items_wallets(wallets: dict):
            for number, info in wallets.items():
                self.ids.wallets_list.data.append(
                    {
                        "number": str(number),
                        "address": info['address'],
                        "private_key": info['private_key'],
                        "mnemonic_phrase": info['mnemonic_phrase'],
                    }
                )


        self.ids.wallets_list.data = []
        show_items_wallets(wallets)
        print(self.ids.wallets_list.data)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def select_path(self, path: str):
        self.exit_manager()
        MDSnackbar(
            MDSnackbarText(
                text=path,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=1,
        ).open()

        self.controller.save_wallets(path)


class ItemWalletInfo(MDBoxLayout):
    number = StringProperty()
    address = StringProperty()
    private_key = StringProperty()
    mnemonic_phrase = StringProperty()


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass
