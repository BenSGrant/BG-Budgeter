
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from fileHandler import FileHandler

from ui import Ui_BGBudgeter

class RegularExpenseManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()

        ## variables
        #self.categoryDict = {}
        self.categoryList = []
        self.reservedCategories = ["Savings"]

        # initialise data
        self.retrieveStoredCategories()

        # setup the categories table
        self.maxRowCount=30
        self.ui.categoryTable.setColumnCount(3)
        self.ui.categoryTable.setRowCount(self.maxRowCount)
        self.ui.categoryTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # resize to fit widget
        self.currentRowCount = 0

    # setup functions
    def retrieveStoredCategories(self):
        '''Retrieves the save data and stores it in a dictionary. If the FileHandler function returns None, it is checked here and the dictionary is not set to None but rather to an empty dictionary'''
        self.categoryList = self.fileHand.retrieveCategoriesData()
        if self.categoryList is None: # if there is no data in the file then set to empty dictionary
            self.categoryList = []


    def setupTable(self):
        '''Intialises the category table. Make sure retrieveStoredCategories() is called before this'''
        columns = ["Expense", "Amount", "Paying Period"]
        self.ui.categoryTable.setHorizontalHeaderLabels(columns)
        for expense in self.categoryList:
            if self.currentRowCount <= self.maxRowCount:
                self.ui.categoryTable.setItem(self.currentRowCount, 0, QTableWidgetItem(expense[0]))
                self.ui.categoryTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(expense[1])))
                self.ui.categoryTable.setItem(self.currentRowCount, 2, QTableWidgetItem(expense[2]))
                self.currentRowCount += 1

        self.ui.categoryTable.itemClicked.connect(self.onItemClicked)


    # functions tied to an event
    def onItemClicked(self, cell):
        '''On a cell being clicked, the category is removed from the list'''
        row = cell.row()
        categoryName = self.ui.categoryTable.item(row, 0).text() # retrieve text from left column
        index = 0
        
        for expense in self.categoryList:
            if expense[0] == categoryName:
               # print(expense[0])
                break
            if index + 1 >= len(self.categoryList):
                index = -1
                print(expense)
                break
            index += 1
        
        if index >= 0:
            print("removing", expense)
            del self.categoryList[index]
        else:
            print("THE ITEM YOU ARE REMOVING FROM THE LIST DOES NOT EXIST")
        self.fileHand.saveCategoriesData(self.categoryList)
        self.ui.categoryTable.removeRow(row)
        self.currentRowCount -= 1 # make sure that current row pointer points to the first empty one
        

    def onAddCategory(self):
        '''When the add button is clicked, a category is added to the table'''
        #retrieve inputs
        name = self.ui.categoryNameInputLE.text()

        ## check if it exists or not and if the name is empty


        ##any(name in i for i in self.categoryList) tests if the name exists in a tuple in the tuple list
        if (not any(name in i for i in self.categoryList)) and (not name in self.reservedCategories) and (len(name) > 0):
            amount = self.ui.categoryAmountSpinBox.value()
            period = self.ui.categoryPeriodComboBox.currentText()
            self.categoryList.append((name, round(amount, 2), period))
            self.ui.categoryTable.setItem(self.currentRowCount, 0, QTableWidgetItem(name))
            self.ui.categoryTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(amount)))
            self.ui.categoryTable.setItem(self.currentRowCount, 2, QTableWidgetItem(period))
            self.currentRowCount += 1
            self.fileHand.saveCategoriesData(self.categoryList)

        elif any(name in i for i in self.categoryList):
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: You have already used this category name")
        elif name in self.reservedCategories:
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: This category name is reserved by the app")
        elif len(name) <= 0:
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: The name field is empty")
        else:
            self.ui.categoryErrLbl.setText("INVALID CATEGORY NAME: Not sure why, please report the bug on github\nalong with a screenshot of the page")

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

class OneTimeExpenseManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()

        ## variables
        self.otExpenseDict = {}

        # initialise data
        self.retrieveStoredOTExpenses()

        # setup the categories table
        self.maxRowCount=30
        self.ui.otExpenseTable.setColumnCount(2)
        self.ui.otExpenseTable.setRowCount(self.maxRowCount)
        self.ui.otExpenseTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # resize to fit widget
        self.currentRowCount = 0

    # setup functions
    def retrieveStoredOTExpenses(self):
        '''Retrieves the save data and stores it in a dictionary. If the FileHandler function returns None, it is checked here and the dictionary is not set to None but rather to an empty dictionary'''
        self.otExpenseDict = self.fileHand.retrieveOTExpensesData()
        if self.otExpenseDict is None: # if there is no data in the file then set to empty dictionary
            self.otExpenseDict = {}

    def setupTable(self):
        '''Intialises the one time expense table. Make sure retrieveStoredOTExpenses() is called before this'''
        columns = ["Expense", "Amount"]
        self.ui.otExpenseTable.setHorizontalHeaderLabels(columns)
        for key in self.otExpenseDict:
            if self.currentRowCount <= self.maxRowCount:
                self.ui.otExpenseTable.setItem(self.currentRowCount, 0, QTableWidgetItem(key))
                self.ui.otExpenseTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(self.otExpenseDict[key])))
                self.currentRowCount += 1

        self.ui.otExpenseTable.itemClicked.connect(self.onItemClicked)

    # functions tied to an event
    def onItemClicked(self, cell):
        '''On a cell being clicked, the expense is removed from the list'''
        row = cell.row()
        otExpenseName = self.ui.otExpenseTable.item(row, 0).text() # retrieve text from left column
        del self.otExpenseDict[otExpenseName] # delete from the dictionary
        self.fileHand.saveOTExpensesData(self.otExpenseDict)
        self.ui.otExpenseTable.removeRow(row)
        self.currentRowCount -= 1 # make sure that current row pointer points to the first empty one

    def onAddCategory(self):
        '''When the add button is clicked, an expense is added to the table'''
        #retrieve inputs
        name = self.ui.otExpenseNameInputLE.text()

        ## check if the name is usable or not
        if (not name in self.otExpenseDict) and (len(name) > 0):
            amount = self.ui.otExpenseSpinBox.value()
            self.otExpenseDict[name] = amount
            self.ui.otExpenseTable.setItem(self.currentRowCount, 0, QTableWidgetItem(name))
            self.ui.otExpenseTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(amount)))
            self.currentRowCount += 1
            self.fileHand.saveOTExpensesData(self.otExpenseDict)

        elif name in self.otExpenseDict:
            self.ui.otExpenseErrLbl.setText("INVALID EXPENSE NAME: You have already used this category name")
        elif len(name) <= 0:
            self.ui.otExpenseErrLbl.setText("INVALID EXPENSE NAME: The name field is empty")
        else:
            self.ui.otExpenseErrLbl.setText("INVALID EXPENSE NAME: Not sure why, please report the bug on github\nalong with a screenshot of the page")

        self.ui.otExpenseNameInputLE.clear()
        self.ui.otExpenseSpinBox.setValue(50.0)

    # other functions

    def addTen(self):
        '''add 10 to the spinbox value'''
        currentAmount = self.ui.otExpenseSpinBox.value()
        if currentAmount + 10.0 <= self.ui.otExpenseSpinBox.maximum():
            self.ui.otExpenseSpinBox.setValue(currentAmount + 10.0)

    def subTen(self):
        '''sub 10 to the spinbox value'''
        currentAmount = self.ui.otExpenseSpinBox.value()
        if currentAmount - 10.0 >= self.ui.otExpenseSpinBox.minimum():
            self.ui.otExpenseSpinBox.setValue(currentAmount - 10.0)

    def addHundred(self):
        '''add 100 to the spinbox value'''
        currentAmount = self.ui.otExpenseSpinBox.value()
        if currentAmount + 100.0 <= self.ui.otExpenseSpinBox.maximum():
            self.ui.otExpenseSpinBox.setValue(currentAmount + 100.0)

    def subHundred(self):
        '''sub 100 to the spinbox value'''
        currentAmount = self.ui.otExpenseSpinBox.value()
        if currentAmount - 100.0 >= self.ui.otExpenseSpinBox.minimum():
            self.ui.otExpenseSpinBox.setValue(currentAmount - 100.0)