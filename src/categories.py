
from PyQt5.QtGui import QDoubleValidator

class CategoryManager:
    def __init__(self, dialog):
        self.ui = dialog

        # setup the categories table
        self.ui.categoryTable.setColumnCount(2)
        self.setupTable()

        # ensure that the amount line edit only accepts numbers with up to 2 d.p and no text
        # range = 1 to 1 trillion
        self.ui.categoryNameInputLE.setValidator(QDoubleValidator(0,1000000000000, 2))

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

    # other functions

    def addTen(self):
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount +10.0 <= self.ui.categoryAmountSpinBox.maximum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount + 10.0)

    def subTen(self):
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount - 10.0 >= self.ui.categoryAmountSpinBox.minimum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount - 10.0)

    def addHundred(self):
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount +100.0 <= self.ui.categoryAmountSpinBox.maximum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount + 100.0)

    def subHundred(self):
        currentAmount = self.ui.categoryAmountSpinBox.value()
        if currentAmount - 100.0 >= self.ui.categoryAmountSpinBox.minimum():
            self.ui.categoryAmountSpinBox.setValue(currentAmount - 100.0)
