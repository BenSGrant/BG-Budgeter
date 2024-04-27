
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QMutex

from ui import *

class BGBudgeter(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_BGBudgeter()
        self.ui.setupUi(self)
    
        #########################################################################
        self.setupPageButtons()
        #########################################################################
        self.show()

    def setupPageButtons(self):
        #home page buttons
        self.ui.incomePageButton.clicked.connect(self.loadIncomePage)
        self.ui.categoryPageButton.clicked.connect(self.loadCategoryPage)
        self.ui.optionsPageButton.clicked.connect(self.loadOptionsPage)
        self.ui.viewBudgetPageButton.clicked.connect(self.loadViewBudgetPage)

        # back to home page buttons
        self.ui.incomeBackButton.clicked.connect(self.loadHomePage)
        self.ui.categoryBackButton.clicked.connect(self.loadHomePage)
        self.ui.optionsBackButton.clicked.connect(self.loadHomePage)
        self.ui.viewBudgetBackButton.clicked.connect(self.loadHomePage)




    def loadHomePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def loadIncomePage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def loadCategoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def loadOptionsPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def loadViewBudgetPage(self):
        self.ui.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    mns = BGBudgeter()
    
    sys.exit(app.exec_())