
import os
from budgetCalc import BudgetCalculator
from fileHandler import FileHandler
from PyQt5.QtWidgets import QDialog

from categories import CategoryManager
from income import IncomeManager
from options import OptionManager
from ui import *

class BGBudgeter(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_BGBudgeter()
        self.ui.setupUi(self)
    
        ######################################################################### USER DEFINED METHODS/VARIABLES
        self.catMan = CategoryManager(self.ui)
        self.catMan.setupTable()
        self.fileHand = FileHandler()
        self.incMan = IncomeManager(self.ui)
        self.incMan.loadIncomeSources()
        self.optMan = OptionManager(self.ui)
        self.optMan.loadSaveData()
        self.budgetCalculator = BudgetCalculator(self.ui, self.incMan, self.catMan, self.optMan)
        self.budgetCalculator.setupTable()

        self.setupPageButtons()
        self.setupCategoryPageButtons()
        self.setupIncomePageButtons()
        ######################################################################### 
        # show ui
        self.show()
        self.ui.stackedWidget.setCurrentIndex(0)

    def setupPageButtons(self):
        '''Connects page switchings buttons to their actions'''
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


    def setupCategoryPageButtons(self):
        '''Connects expense category page buttons to their actions'''
        self.ui.addCategoryButton.clicked.connect(self.catMan.onAddCategory)
        
        self.ui.plus10Button.clicked.connect(self.catMan.addTen)
        self.ui.minus10Button.clicked.connect(self.catMan.subTen)
        self.ui.plus100Button.clicked.connect(self.catMan.addHundred)
        self.ui.minus100Button.clicked.connect(self.catMan.subHundred)



    def setupIncomePageButtons(self):
        '''Connects income page buttons to their actions'''
        self.ui.addIncomeButton.clicked.connect(self.incMan.loadSourceTile)
        self.ui.updateIncomeButton.clicked.connect(self.incMan.onUpdate)


    ################## LOAD PAGES ##################

    def loadHomePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def loadIncomePage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def loadCategoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def loadOptionsPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def loadViewBudgetPage(self):
        self.budgetCalculator.displayTotalBudget()
        self.ui.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    mns = BGBudgeter()
    
    sys.exit(app.exec_())