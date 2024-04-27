
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt, QMutex

from ui import *

class BGBudgeter(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    