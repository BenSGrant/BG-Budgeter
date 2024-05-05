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
        self.perPeriodRegularExpenses = {}

        
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

    def calculatePerPeriodRegularExpenses(self):
        '''For example, monthly expense converted to weekly amount'''
        for expense in self.catMan.categoryList:
            amount = expense[1] # default to budget period amount
            if expense[2].lower() == "weekly" and self.optMan.budgetPeriod.lower() == "fortnightly":
                # weekly -> fortnightly
                amount = round(expense[1] * 2, 2)
            elif expense[2].lower() == "weekly" and self.optMan.budgetPeriod.lower() == "monthly":
                #convert weekly amount to monthly
                amount = round((expense[1] * 52) / 12, 2)
                
            elif expense[2].lower() == "monthly" and self.optMan.budgetPeriod.lower() == "weekly":
                #convert monthly amount to weekly
                amount = round((expense[1] * 12) / 52, 2)
            elif expense[2].lower() == "monthly" and self.optMan.budgetPeriod.lower() == "fortnightly":
                #convert monthly amount to fortnightly
                amount = round((expense[1] * 12) / 26, 2)
                
            elif expense[2].lower() == "every 3 months" and self.optMan.budgetPeriod.lower() == "weekly":
                #3months -> weekly
                amount = round((expense[1] * 4) / 52, 2)
            elif expense[2].lower() == "every 3 months" and self.optMan.budgetPeriod.lower() == "fortnightly":
                #3months -> fortnightly
                amount = round((expense[1] * 4) / 26, 2)
            elif expense[2].lower() == "every 3 months" and self.optMan.budgetPeriod.lower() == "monthly":
                #convert 3monthly to monthly
                amount = round((expense[1]) / 3, 2)
                
            elif expense[2].lower() == "every 6 months" and self.optMan.budgetPeriod.lower() == "weekly":
                #6months -> weekly
                amount = round((expense[1] * 2) / 52, 2)
            elif expense[2].lower() == "every 6 months" and self.optMan.budgetPeriod.lower() == "fortnightly":
                #6months -> fortnightly
                amount = round((expense[1] * 2) / 26, 2)
            elif expense[2].lower() == "every 6 months" and self.optMan.budgetPeriod.lower() == "monthly":
                #convert biannually to monthly
                amount = round((expense[1]) / 6, 2)
                
            elif expense[2].lower() == "annually" and self.optMan.budgetPeriod.lower() == "weekly":
                #yearly -> weekly
                amount = round((expense[1]) / 52, 2)
            elif expense[2].lower() == "annually" and self.optMan.budgetPeriod.lower() == "fortnightly":
                #yearly -> fortnightly
                amount = round((expense[1]) / 26, 2)
            elif expense[2].lower() == "annually" and self.optMan.budgetPeriod.lower() == "monthly":
                #convert annually to monthly
                amount = round((expense[1]) / 12, 2)

            self.perPeriodRegularExpenses[expense[0]] = amount
            

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

        for key in self.perPeriodRegularExpenses:
            totalIncome -= self.perPeriodRegularExpenses[key]


        return totalIncome
    
    def calculateSavings(self):
        '''Calculates leftovers from income'''
        incomeForThePeriod = self.calculateTotalYearlyIncome() / self.optMan.budgetPeriodOccurences
        leftovers = incomeForThePeriod # technically savings

        for key in self.perPeriodRegularExpenses:
            leftovers -= self.perPeriodRegularExpenses[key]
        return round(leftovers,2)
    
    def displayTotalBudget(self):
        self.ui.budgetTable.clearContents()
        self.currentRowCount = 0

        self.calculatePerPeriodRegularExpenses()
        for expenseTuple in self.catMan.categoryList:
            if self.currentRowCount < self.maxRowCount: # < not <= to account for the savings row

                self.ui.budgetTable.setItem(self.currentRowCount, 0, QTableWidgetItem(expenseTuple[0]))
                self.ui.budgetTable.setItem(self.currentRowCount, 1, QTableWidgetItem(str(self.perPeriodRegularExpenses[expenseTuple[0]])))
            

                # alternating colours - every odd row is grey, even is white (except for savings row if <0 or >0)
                if self.currentRowCount % 2 == 1:
                    self.ui.budgetTable.item(self.currentRowCount, 0).setBackground(QColor(210,210,210))
                    self.ui.budgetTable.item(self.currentRowCount, 1).setBackground(QColor(210,210,210))

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