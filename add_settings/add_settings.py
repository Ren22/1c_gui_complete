from .add_settings_ui import Ui_add_settings
from PyQt5.QtWidgets import *


class Add_settings(QWidget, Ui_add_settings):
    def __init__(self, parent=None):
        super(Add_settings, self).__init__(parent)
        self.setupUi(self)