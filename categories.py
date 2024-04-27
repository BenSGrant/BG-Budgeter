
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView

class CategoryManager:
    def __init__(self, dialog):
        self.ui = dialog

        # setup the categories table
        self.ui.categoryTab.setColumnCount(2)
        self.ui.categoryTab.setRowCount(self.rowCount)


    def setupTable(self):
        columns = ["Expense", "Amount"]
