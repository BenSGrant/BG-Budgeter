from fileHandler import FileHandler

class IncomeManager:
    def __init__(self, dialog):
        self.ui = dialog

        ## objects
        self.fileHand = FileHandler()
        
        ## variables
        self.incomeSources = [] # stored list of tuples which have 3 elements


    def onAddIncomeSource(self):
        # dummy code until actual functionality worked out
        amount = 40000
        period = "Annually"
        occurences = 1
        newSource = (amount, period, occurences)
        self.incomeSources.append(newSource)
