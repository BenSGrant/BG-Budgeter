from fileHandler import FileHandler
from ui import Ui_BGBudgeter

class IncomeManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()
        
        ## variables
        self.incomeSources = [] # stored list of tuples which have 3 elements


    def onAddIncomeSource(self):
        # dummy code until actual functionality worked out
        amount = self.ui.incomeAmountSpinBox.value()
        period = "Annually"
        occurences = 1
        newSource = (amount, period, occurences)
        self.incomeSources.append(newSource)
