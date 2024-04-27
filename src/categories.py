
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

class CategoryManager:
    def __init__(self, dialog):
        self.ui = dialog

        # setup the categories table
        self.maxRowCount=30
        self.ui.categoryTable.setColumnCount(2)
        self.ui.categoryTable.setRowCount(self.maxRowCount)
        self.ui.categoryTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # resize to fit widget
        self.currentRowCount = 0
        self.setupTable()


        self.categoryDict = {}

    # setup functions
    def setupTable(self):
        columns = ["Expense", "Amount"]
        self.ui.categoryTable.setHorizontalHeaderLabels(columns)

    # functions tied to an event
    def onCellClicked(self):
        '''On a cell being clicked, the category is removed from the list'''

    def onAddCategory(self):
        '''When the add button is clicked, a category is added to the table'''
        #retrieve inputs
        name = self.ui.categoryNameInputLE.text()
        amount = self.ui.categoryAmountSpinBox.value()
        self.categoryDict[name] = amount
        print(self.categoryDict)
        self.ui.categoryTable.setItem(self.currentRowCount, 0, QTableWidgetItem(name))
        self.ui.categoryTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(amount)))
        self.currentRowCount += 1




    # other functions

    def addTen(self):
        '''add 10 to the spinbox value'''
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount + 10.0 <= self.ui.categoryAmountSpinBox.maximum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount + 10.0)

    def subTen(self):
        '''sub 10 to the spinbox value'''
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount - 10.0 >= self.ui.categoryAmountSpinBox.minimum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount - 10.0)

    def addHundred(self):
        '''add 100 to the spinbox value'''
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount + 100.0 <= self.ui.categoryAmountSpinBox.maximum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount + 100.0)

    def subHundred(self):
        '''sub 100 to the spinbox value'''
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount - 100.0 >= self.ui.categoryAmountSpinBox.minimum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount - 100.0)
