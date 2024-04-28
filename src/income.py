from fileHandler import FileHandler
from ui import Ui_BGBudgeter

class IncomeManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()
        
        ## variables
        self.incomeSources = [] # stored list of tuples which have 3 elements

    ## setup
    def loadIncomeSources(self):
        self.incomeSources = self.fileHand.retrieveIncomeData()


    def onAddIncomeSource(self):
        amount = self.ui.incomeAmountSpinBox.value()
        period = self.ui.incomePeriodComboBox.currentText()
        occurences = self.ui.incomeOccurencesSpinBox.value()
        
        newSource = (amount, period, occurences)
        self.incomeSources.append(newSource)

