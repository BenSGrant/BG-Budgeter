from fileHandler import FileHandler
from ui import Ui_BGBudgeter


class OptionManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        #### objects
        self.fileHand = FileHandler()
        self.budgetPeriod = ""

        self.ui.updateOptionsButton.clicked.connect(self.onUpdate)
        self.ui.weeklyBudgetRadioButton.toggled.connect(self.onRadioButtonChange)
        self.ui.fortnightlyBudgetRadioButton.toggled.connect(self.onRadioButtonChange)
        self.ui.monthlyBudgetRadioButton.toggled.connect(self.onRadioButtonChange)


    def onUpdate(self):
        '''Saves current option data'''
        if self.ui.weeklyBudgetRadioButton.isChecked():
            self.budgetPeriod = "weekly"
        elif self.ui.fortnightlyBudgetRadioButton.isChecked():
            self.budgetPeriod = "fortnightly"
        elif self.ui.monthlyBudgetRadioButton.isChecked():
            self.budgetPeriod = "monthly"

        self.fileHand.saveOptionsData(self.budgetPeriod)
    
    def loadSaveData(self):
        '''Loads current options'''
        data = self.fileHand.retrieveOptionsData()

        self.budgetPeriod = data

        if self.budgetPeriod == "weekly":
            self.ui.weeklyBudgetRadioButton.setChecked(True)
        elif self.budgetPeriod == "fortnightly":
            self.ui.fortnightlyBudgetRadioButton.setChecked(True)
        elif self.budgetPeriod == "monthly":
            self.ui.monthlyBudgetRadioButton.setChecked(True)
        else:
            print("Options save data is invalid, using default settings")
            self.ui.weeklyBudgetRadioButton.setChecked(True)

    def onRadioButtonChange(self):
        '''Changes the maximum occurences value'''
        if self.ui.weeklyBudgetRadioButton.isChecked():
            self.ui.budgetPeriodOccurencesSpinBox.setMaximum(52)
        if self.ui.fortnightlyBudgetRadioButton.isChecked():
            self.ui.budgetPeriodOccurencesSpinBox.setMaximum(26)
        if self.ui.monthlyBudgetRadioButton.isChecked():
            self.ui.budgetPeriodOccurencesSpinBox.setMaximum(12)