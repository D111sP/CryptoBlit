import os
import threading
import eth_account.hdaccount as hdaccount

from eth_account import Account
import pandas as pd

from Model.base_model import BaseScreenModel


class CreatWalletScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    def __init__(self):
        super().__init__()
        self._len_seed_phrase = None
        self._number_of_wallets = None
        self._created_wallets = {}
        self._busy = False

    @property
    def len_created_wallets(self):
        return len(self._created_wallets)

    @property
    def len_seed_phrase(self):
        return self._len_seed_phrase

    @len_seed_phrase.setter
    def len_seed_phrase(self, value):
        self._len_seed_phrase = value

    @property
    def number_of_wallets(self):
        return self._number_of_wallets

    @number_of_wallets.setter
    def number_of_wallets(self, value):
        self._number_of_wallets = value

    @property
    def created_wallets(self):
        return self._created_wallets

    @property
    def busy(self):
        return self._busy


    def generate_wallets(self):
        self._created_wallets = {}
        threading.Thread(target=self.generate_wallets_thread).start()


    def generate_wallets_thread(self):
        self._busy = True
        for i in range(self._number_of_wallets):
            Account.enable_unaudited_hdwallet_features()
            mnemonic_phrase = hdaccount.generate_mnemonic(
                                num_words=self._len_seed_phrase,
                                lang="english")

            wallet = Account.from_mnemonic(
                mnemonic=mnemonic_phrase
            )
            self._created_wallets[i+1] = {
                "mnemonic_phrase": mnemonic_phrase,
                "address": wallet.address,
                "private_key": wallet.key.hex()
            }

        self._busy = False
        self.notify_observers("creat wallet screen")

    def save_wallets_to_excel(self, file_path):
        # Convert your wallet data into a pandas DataFrame
        # Assuming self._created_wallets is a dict with keys as integers starting from 1
        data = [{
            'number': key,
            'address': self._created_wallets[key]['address'],
            'private_key': self._created_wallets[key]['private_key'],
            'mnemonic_phrase': self._created_wallets[key]['mnemonic_phrase']
        } for key in self._created_wallets]

        # Create DataFrame
        df = pd.DataFrame(data)

        file_path = os.path.join(file_path, 'wallets.xlsx')
        # Save DataFrame to Excel
        df.to_excel(file_path, index=False)