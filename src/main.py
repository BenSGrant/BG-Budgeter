
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QMutex

from ui import *

class BGBudgeter(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_BGBudgeterClass()
        self.ui.setupUi(self)
    
        self.show()