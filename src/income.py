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
        self.srcTiles = [] # list of the actual IncomeSourceTile objects
        self.incomePeriodOptions = ["Weekly", "Fortnightly",
                                     "Monthly", "Annually",
                                     "Student Maintenance Loan (UK)"] # this needs to be updated if the options change
        


    ## setup
    def loadIncomeSources(self):
        '''Loads saved data and updates UI accordingly'''
        self.incomeSrcs = self.fileHand.retrieveIncomeData()

        if self.incomeSrcs is not None and len(self.incomeSrcs) > 0:    
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

                # period
                newTile.incomeOccurencesSpinBox.setValue(int(src[2]))
        else:
            print("Income save data is empty")

    def loadSourceTile(self):
        '''Adds an income tile to the scroll area and connects all buttons to their actions'''
        srcTile = IncomeSourceTile(self.ui.incomeScrollAreaContents, self.ui.verticalLayout_3)
        srcTile.incomeAdd1000Button.clicked.connect(lambda: self.onAddThousand(srcTile))
        srcTile.incomeAdd100Button.clicked.connect(lambda: self.onAddHundred(srcTile))
        srcTile.incomeMinus1000Button.clicked.connect(lambda: self.onSubThousand(srcTile))
        srcTile.incomeMinus100Button.clicked.connect(lambda: self.onSubHundred(srcTile))
        srcTile.removeIncomeButton.clicked.connect(lambda: self.onRemoveSource(srcTile))

        self.srcTiles.append(srcTile)
        return srcTile

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
         # remove from lists
        self.srcTiles.remove(tile)
        # get the income source data
        incTuple = (tile.incomeAmountSpinBox.value(),
                    tile.incomePeriodComboBox.currentText(),
                    tile.incomeOccurencesSpinBox.value())
        # if the income  source data has been stored already then remove it
        if incTuple in self.incomeSrcs:
            self.incomeSrcs.remove(incTuple)
        # decouple the object from it's parent
        tile.parent.layout().removeWidget(tile.incomeSourceParentWidget)
        # instruct Qt remove the object
        tile.incomeSourceParentWidget.deleteLater()
        del self


    def onIncomePeriodChange(self, tile : IncomeSourceTile):
        '''When the income period selected changes, the occurences spin box changes it's maximum value.'''
        if tile.incomePeriodComboBox.currentText() == self.incomePeriodOptions[0]:
            tile.incomeOccurencesSpinBox.setMaximum(52)
            self.ui.studentMaintenanceDetected.setText("")
        elif tile.incomePeriodComboBox.currentText() == self.incomePeriodOptions[1]:
            tile.incomeOccurencesSpinBox.setMaximum(26)
            self.ui.studentMaintenanceDetected.setText("")
        elif tile.incomePeriodComboBox.currentText() == self.incomePeriodOptions[2]:
            tile.incomeOccurencesSpinBox.setMaximum(12)
            self.ui.studentMaintenanceDetected.setText("")
        elif tile.incomePeriodComboBox.currentText() == self.incomePeriodOptions[3]:
            tile.incomeOccurencesSpinBox.setMaximum(1)
            self.ui.studentMaintenanceDetected.setText("")
        elif tile.incomePeriodComboBox.currentText() == self.incomePeriodOptions[4]:
            tile.incomeOccurencesSpinBox.setMaximum(1)
            self.ui.studentMaintenanceDetected.setText("You have chosen a student maintenance loan type income.\nThe number of occurences is no longer taken into account.")
        


    def onUpdate(self):
        '''Called when the update button is pressed. Saves the income data to file'''
        for src in self.srcTiles:
            # retrieve the data and put it in a tuple
            amount = src.incomeAmountSpinBox.value()
            period = src.incomePeriodComboBox.currentText()
            occurences = src.incomeOccurencesSpinBox.value()
            incTuple = (amount, period, occurences)
            if incTuple not in self.incomeSrcs:
                self.incomeSrcs.append((amount, period, occurences))
            else:
                print("not adding this income source:\n",incTuple,"\nbecause it is already in the list")
        
        # actually save the data
        self.fileHand.saveIncomeData(self.incomeSrcs)
