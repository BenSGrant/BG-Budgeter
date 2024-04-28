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
            newTile = self.loadSourceTile()

            # set amount
            newTile.incomeAmountSpinBox.setValue(float(src[0]))

            ## set the correct combobox option based on the period stored
            for i in range(newTile.incomePeriodComboBox.count()):
                # if the stored period is equal to the combo box item that is currently being iterated
                # then set the combobox item equal to the stored period
                if src[1] == newTile.incomePeriodComboBox.itemText(i):
                    newTile.incomePeriodComboBox.setCurrentIndex(i)

    def loadSourceTile(self):
            srcTile = IncomeSourceTile(self.ui.incomeScrollAreaContents, self.ui.verticalLayout_3)
            srcTile.incomeAdd1000Button.clicked.connect(lambda: self.onAddThousand(srcTile))
            srcTile.incomeAdd100Button.clicked.connect(lambda: self.onAddHundred(srcTile))
            srcTile.incomeMinus1000Button.clicked.connect(lambda: self.onSubThousand(srcTile))
            srcTile.incomeMinus100Button.clicked.connect(lambda: self.onSubHundred(srcTile))
            srcTile.removeIncomeButton.clicked.connect(lambda: self.onRemoveSource(srcTile))

            return srcTile


    def onAddIncomeSource(self):
        '''Adds an income tile to the scroll area'''
        self.loadSourceTile()


    def onAddHundred(self, tile : IncomeSourceTile):
        if tile.incomeAmountSpinBox.value() + 100 <= tile.incomeAmountSpinBox.maximum():
            tile.incomeAmountSpinBox.setValue(tile.incomeAmountSpinBox.value() + 100)
            
    def onSubHundred(self, tile : IncomeSourceTile):
        if tile.incomeAmountSpinBox.value() - 100 >= tile.incomeAmountSpinBox.minimum():
            tile.incomeAmountSpinBox.setValue(tile.incomeAmountSpinBox.value() - 100)
            

    def onAddThousand(self, tile : IncomeSourceTile):
        if tile.incomeAmountSpinBox.value() + 1000 <= tile.incomeAmountSpinBox.maximum():
            tile.incomeAmountSpinBox.setValue(tile.incomeAmountSpinBox.value() + 1000)
            
    def onSubThousand(self, tile : IncomeSourceTile):
        if tile.incomeAmountSpinBox.value() - 1000 >= tile.incomeAmountSpinBox.minimum():
            tile.incomeAmountSpinBox.setValue(tile.incomeAmountSpinBox.value() - 1000)

    def onRemoveSource(self, tile : IncomeSourceTile):
        '''Removes the widget from the scroll area and from memory'''
        print("deleting source")
        tile.parent.layout().removeWidget(tile.incomeSourceParentWidget)
        tile.incomeSourceParentWidget.deleteLater()
        del self