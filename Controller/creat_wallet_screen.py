import importlib

from kivy.metrics import dp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

import View.CreatWalletScreen.creat_wallet_screen

importlib.reload(View.CreatWalletScreen.creat_wallet_screen)




class CreatWalletScreenController:

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = View.CreatWalletScreen.creat_wallet_screen.CreatWalletScreenView(controller=self, model=self.model)

    def get_view(self) -> View.CreatWalletScreen.creat_wallet_screen:
        return self.view

    def generate_wallets(self):
        if self.model.busy:
            self.show_allert_message("иди нахуй, процесс занят")
            return

        if not self.model.number_of_wallets:
            self.show_allert_message("Иди нахуй, поля заполни, чурка")
            return

        if not self.model.len_seed_phrase:
            self.show_allert_message("Иди нахуй, поля заполни, чурка ")
            return
        if self.model.number_of_wallets > 50:
            self.show_allert_message("Жди, ёпта")
        self.model.generate_wallets()

    def save_wallets(self, file_path):
        self.model.save_wallets_to_excel(file_path)

    def set_number_of_wallets(self, value):
        self.model.number_of_wallets = value

    def set_len_seed_phrase(self, value):
        self.model.len_seed_phrase = value

    def show_allert_message(self, text):
        MDSnackbar(
            MDSnackbarText(
                text=text,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5, "top": 0.5},
            size_hint_x=1,
        ).open()