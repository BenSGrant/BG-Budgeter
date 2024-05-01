from categories import CategoryManager
from options import OptionManager
from ui import Ui_BGBudgeter
from income import IncomeManager


class BudgetCalculator:
    def __init__(self, dialog : Ui_BGBudgeter, incMan : IncomeManager, catMan : CategoryManager, optMan : OptionManager):
        '''MUST be created after loading all save data'''
        self.ui = dialog


        self.catMan = catMan
        self.incMan = incMan
        self.optMan = optMan

        self.categoryList = self.catMan.categoryDict
        self.incomeList = self.incMan.incomeSrcs

    def calculateTotalYearlyIncome(self):
        totalIncome = 0

        for income in self.incomeList:
            amount = income[0]
            occurences = income[2]

            totalIncome += amount * occurences



        return totalIncome