
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QMutex

from ui import *

class BGBudgeter(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_BGBudgeter()
        self.ui.setupUi(self)
    
        self.show()

    

    def loadHomePage(self):
        ui.stackedWidget.setCurrentIndex(0)

    def loadIncomePage(self):
        ui.stackedWidget.setCurrentIndex(1)

    def loadCategoryPage(self):
        ui.stackedWidget.setCurrentIndex(2)

    def loadOptionsPage(self):
        ui.stackedWidget.setCurrentIndex(3)

    def loadViewBudgetPage(self):
        ui.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    mns = BGBudgeter()
    
    sys.exit(app.exec_())