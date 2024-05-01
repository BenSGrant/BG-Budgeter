from categories import CategoryManager
from options import OptionManager
from ui import Ui_BGBudgeter
from income import IncomeManager

from PyQt5.QtWidgets import QHeaderView

class BudgetCalculator:
    def __init__(self, dialog : Ui_BGBudgeter, incMan : IncomeManager, catMan : CategoryManager, optMan : OptionManager):
        '''MUST be created after loading all save data'''
        self.ui = dialog


        self.catMan = catMan
        self.incMan = incMan
        self.optMan = optMan

        self.categoryDict = self.catMan.categoryDict
        self.incomeList = self.incMan.incomeSrcs
        self.perCategoryBudget = {}


        
        # budget table class variables
        self.maxRowCount=30
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

        for income in self.incomeList:
            amount = income[0]
            period = income[1]
            occurences = income[2]

            if period != self.incMan.incomePeriodOptions[4]:
                totalIncome += amount * occurences
            else:
                print("Student maintenance loan detected, (option: " + period + ")")
                totalIncome = amount
        
        return totalIncome
    
    def calculateAverageWeeklyIncome(self):
        return self.calculateAverageWeeklyIncome() / 52
    
    def calculateAverageMonthlyIncome(self):
        return self.calculateTotalYearlyIncome() / 12
    
    def calculateSavings(self):
        incomeForThePeriod = 0
        if self.optMan.budgetPeriod == "weekly":
            incomeForThePeriod = self.calculateAverageWeeklyIncome()
        if self.optMan.budgetPeriod == "fornightly":
            incomeForThePeriod = self.calculateAverageWeeklyIncome() * 2
        if self.optMan.budgetPeriod == "monthly":
            incomeForThePeriod = self.calculateAverageMonthlyIncome()
        
        leftovers = incomeForThePeriod # technically savings

        for key in self.categoryDict:
            leftovers -= self.categoryDict[key]
        
        return leftovers
