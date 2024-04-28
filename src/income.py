from fileHandler import FileHandler
from ui import Ui_BGBudgeter
from incomeSourceTile import IncomeSourceTile

class IncomeManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()
        
        ## variables
        self.incomeSrcs = [] # stored list of tuples which have 3 elements

    ## setup
    def loadIncomeSources(self):
        self.incomeSrcs = self.fileHand.retrieveIncomeData()
        for src in self.incomeSrcs:
            newTile = IncomeSourceTile(self.ui.incomeScrollAreaContents, self.ui.verticalLayout_3)

            # set amount
            newTile.incomeAmountSpinBox.setValue(float(src[0]))

            ## set the correct combobox option based on the period stored
            for i in range(newTile.incomePeriodComboBox.count()):
                # if the stored period is equal to the combo box item that is currently being iterated
                # then set the combobox item equal to the stored period
                if src[1] == newTile.incomePeriodComboBox.itemText(i):
                    newTile.incomePeriodComboBox.setCurrentIndex(i)



    def onAddIncomeSource(self):
        '''Adds an income tile to the scroll area'''
        newTile = IncomeSourceTile(self.ui.incomeScrollAreaContents, self.ui.verticalLayout_3)

