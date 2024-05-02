
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from fileHandler import FileHandler

from ui import Ui_BGBudgeter

class RegularExpenseManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()

        ## variables
        self.categoryDict = {}
        self.reservedCategories = ["Savings"]

        # initialise data
        self.retrieveStoredCategories()

        # setup the categories table
        self.maxRowCount=30
        self.ui.categoryTable.setColumnCount(2)
        self.ui.categoryTable.setRowCount(self.maxRowCount)
        self.ui.categoryTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # resize to fit widget
        self.currentRowCount = 0

    # setup functions
    def retrieveStoredCategories(self):
        '''Retrieves the save data and stores it in a dictionary. If the FileHandler function returns None, it is checked here and the dictionary is not set to None but rather to an empty dictionary'''
        self.categoryDict = self.fileHand.retrieveCategoriesData()
        if self.categoryDict is None: # if there is no data in the file then set to empty dictionary
            self.categoryDict = {}


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
        self.ui.categoryTable.removeRow(row)
        self.currentRowCount -= 1 # make sure that current row pointer points to the first empty one
        

    def onAddCategory(self):
        '''When the add button is clicked, a category is added to the table'''
        #retrieve inputs
        name = self.ui.categoryNameInputLE.text()

        ## check if valid
        if (not name in self.categoryDict) and (not name in self.reservedCategories):
            amount = self.ui.categoryAmountSpinBox.value()
            self.categoryDict[name] = amount
            self.ui.categoryTable.setItem(self.currentRowCount, 0, QTableWidgetItem(name))
            self.ui.categoryTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(amount)))
            self.currentRowCount += 1
            self.fileHand.saveCategoriesData(self.categoryDict)

        elif name in self.categoryDict:
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: You have already used this category name")
        elif name in self.reservedCategories:
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: This category name is reserved by the app")
        else:
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: Not sure why, please report the bug on github\nalong with a screenshot of the app")

        self.ui.categoryNameInputLE.clear()
        self.ui.categoryAmountSpinBox.setValue(50.0)



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
