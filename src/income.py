from fileHandler import FileHandler
from ui import Ui_BGBudgeter
from incomeSourceTile import IncomeSourceTile

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
        '''Adds an income tile to the scroll area'''
        newTile = IncomeSourceTile(self.ui.incomeScrollAreaContents, self.ui.verticalLayout_3)

