
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView

class CategoryManager:
    def __init__(self, dialog):
        self.ui = dialog

        # setup the categories table
        self.ui.categoryTable.setColumnCount(2)


    def setupTable(self):
        columns = ["Expense", "Amount"]
        self.ui.categoryTable.setHorizontalHeaderLabels(columns)

    def onCellClicked(self):
        '''On a cell being clicked, the category is removed from the list'''

    def onAddCategory(self):
        '''When the add button is clicked, a category is added to the table'''
        name = self.ui.categoryNameInputLE.text()
        print(name)