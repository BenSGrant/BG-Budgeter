from expenses import OneTimeExpenseManager, RegularExpenseManager
from options import OptionManager
from ui import Ui_BGBudgeter
from income import IncomeManager

from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
from PyQt5.QtGui import QColor

class BudgetCalculator:
    def __init__(self, dialog : Ui_BGBudgeter, incMan : IncomeManager, catMan : RegularExpenseManager, optMan : OptionManager, OTEMan : OneTimeExpenseManager):
        '''MUST be created after loading all save data'''
        self.ui = dialog


        self.catMan = catMan
        self.incMan = incMan
        self.optMan = optMan
        self.OTEMan = OTEMan

        self.perCategoryBudget = {}


        
        # budget table class variables
        self.maxRowCount=31 # has to be one more thanthe categories.py version of the file
        self.currentRowCount = 0

    ####### UI STUFF

    def setupTable(self):
        '''Sets up the budget view table'''
        self.ui.budgetTable.setColumnCount(2)
        self.ui.budgetTable.setRowCount(self.maxRowCount)
        self.ui.budgetTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # resize to fit widget
        self.ui.budgetTable.setHorizontalHeaderLabels(["Expense Category", "Allowance"])



    ###### INCOME CALCULATIONS


    def calculateTotalYearlyIncome(self):
        '''Takes all income sources and calculates how much is received per year'''
        totalIncome = 0


        # take the sum of all income
        for income in self.incMan.incomeSrcs:
            amount = income[0]
            period = income[1]
            occurences = income[2]

            if period != self.incMan.incomePeriodOptions[4]:
                totalIncome += amount * occurences
            else:
                print("Student maintenance loan detected, (option: " + period + ")")
                totalIncome += amount
        
        # subtract one time expenses

        for key in self.OTEMan.otExpenseDict:
            totalIncome -= self.OTEMan.otExpenseDict[key]


        return totalIncome
    
    def calculateSavings(self):
        '''Calculates leftovers from income'''
        incomeForThePeriod = self.calculateTotalYearlyIncome() / self.optMan.budgetPeriodOccurences
        leftovers = incomeForThePeriod # technically savings

        for key in self.catMan.categoryDict:
            leftovers -= self.catMan.categoryDict[key]
        return round(leftovers,2)
    
    def displayTotalBudget(self):
        self.ui.budgetTable.clearContents()
        self.currentRowCount = 0
        for key in self.catMan.categoryDict:
            if self.currentRowCount < self.maxRowCount: # < not <= to account for the savings row
                self.ui.budgetTable.setItem(self.currentRowCount, 0, QTableWidgetItem(key))
                self.ui.budgetTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(self.catMan.categoryDict[key])))
                self.currentRowCount += 1

        # add savings
        savings = self.calculateSavings()
        self.ui.budgetTable.setItem(self.currentRowCount, 0, QTableWidgetItem(self.catMan.reservedCategories[0]))
        self.ui.budgetTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(savings)))

        if savings < 0: # not enough income for the budget
            self.ui.budgetTable.item(self.currentRowCount, 0).setBackground(QColor(250,50,50))
            self.ui.budgetTable.item(self.currentRowCount, 1).setBackground(QColor(250,50,50))
        elif savings > 0: # money is being saved
            self.ui.budgetTable.item(self.currentRowCount, 0).setBackground(QColor(50,200,100))
            self.ui.budgetTable.item(self.currentRowCount, 1).setBackground(QColor(50,200,100))

        self.currentRowCount += 1