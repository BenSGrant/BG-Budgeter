
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from fileHandler import FileHandler

class CategoryManager:
    def __init__(self, dialog):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()

        ## variables
        self.categoryDict = {}

        # initialise data
        self.retrieveStoredCategories()

        # setup the categories table
        self.maxRowCount=30
        self.ui.categoryTable.setColumnCount(2)
        self.ui.categoryTable.setRowCount(self.maxRowCount)
        self.ui.categoryTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # resize to fit widget
        self.currentRowCount = 0
        self.setupTable()

    # setup functions
    def retrieveStoredCategories(self):
        '''Retrieves the save data and stores it in a dictionary'''
        self.categoryDict = self.fileHand.retrieveCategoriesData()


    def setupTable(self):
        '''Intialises the category table. Make sure retrieveStoredCategories() is called before this'''
        columns = ["Expense", "Amount"]
        self.ui.categoryTable.setHorizontalHeaderLabels(columns)
        for key in self.categoryDict:
            if self.currentRowCount <= self.maxRowCount:
                self.ui.categoryTable.setItem(self.currentRowCount, 0, QTableWidgetItem(key))
                self.ui.categoryTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(self.categoryDict[key])))
                self.currentRowCount += 1

        self.ui.categoryTable.itemClicked.connect(self.onItemClicked)


    # functions tied to an event
    def onItemClicked(self, cell):
        '''On a cell being clicked, the category is removed from the list'''
        row = cell.row()
        categoryName = self.ui.categoryTable.item(row, 0).text() # retrieve text from left column
        del self.categoryDict[categoryName] # delete from the dictionary
        self.fileHand.saveCategoriesData(self.categoryDict)

    def onAddCategory(self):
        '''When the add button is clicked, a category is added to the table'''
        #retrieve inputs
        name = self.ui.categoryNameInputLE.text()
        amount = self.ui.categoryAmountSpinBox.value()
        self.categoryDict[name] = amount
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
