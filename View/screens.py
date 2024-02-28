# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController

from Model.creat_wallet_screen import CreatWalletScreenModel
from Controller.creat_wallet_screen import CreatWalletScreenController


screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "creat wallet screen": {
        "model": CreatWalletScreenModel,
        "controller": CreatWalletScreenController,
    },
}