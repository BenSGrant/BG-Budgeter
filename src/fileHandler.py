import os

class FileHandler:
    F_INCOME = 1
    F_CATEGORIES = 2
    F_OPTIONS = 3
    F_OTEXPENSES = 4

    def __init__(self):
        #this makes the app windows only as %appdata% is only defined in Windows
        #as far as im aware. If anyone knows anything about how to make this work
        #on Linux/Mac, please let me know by creating an issue on the GitHub repo
        self.dirPath = os.getenv('APPDATA') + "\\BG-Budgeter\\"
        self.categoriesPath = self.dirPath + "categories.txt"
        self.incomePath = self.dirPath + "income.txt"
        self.optionsPath = self.dirPath + "options.txt"
        self.otExpensesPath = self.dirPath + "otExpenses.txt"

        self.ensureFilesExist()
    
    # SETUP

    def ensureFilesExist(self):
        '''This function checks if save data files do not exist, then creates them if that is the case.'''
        if not os.path.exists(self.categoriesPath):
            #dirname returns the directory part, makedirs creates it
            os.makedirs(os.path.dirname(self.categoriesPath), exist_ok=True)
            with open(self.categoriesPath, 'w') as f:
                f.write("")
                f.close()
        if not os.path.exists(self.incomePath):
            os.makedirs(os.path.dirname(self.incomePath), exist_ok=True)
            with open(self.incomePath, 'w') as f:
                f.write("")
                f.close()
        if not os.path.exists(self.optionsPath):
            os.makedirs(os.path.dirname(self.optionsPath), exist_ok=True)
            with open(self.optionsPath, 'w') as f:
                f.write("")
                f.close()
        if not os.path.exists(self.otExpensesPath):
            os.makedirs(os.path.dirname(self.otExpensesPath), exist_ok=True)
            with open(self.otExpensesPath, 'w') as f:
                f.write("")
                f.close()


    ### GENERAL

    def overwrite(self, option : int, data):
        '''Completely replace all text in the document.

            option should be one of 3 values: F_INCOME, F_CATEGORIES, F_OPTIONS or F_OTEXPENSES
        '''
        if option == self.F_CATEGORIES:
            print("saving to " + self.categoriesPath)
            fileObj = open(self.categoriesPath, 'w')
            fileObj.write(data)
            fileObj.close()
        elif option == self.F_INCOME:
            fileObj = open(self.incomePath, 'w')
            fileObj.write(data)
            fileObj.close()
        elif option == self.F_OPTIONS:
            fileObj = open(self.optionsPath, 'w')
            fileObj.write(data)
            fileObj.close()
        elif option == self.F_OTEXPENSES:
            fileObj = open(self.otExpensesPath, 'w')
            fileObj.write(data)
            fileObj.close()
        else:
            print("ERROR: NOT A SUITABLE FILE OPTION IN overwrite() CALL")

    def appendData(self,option : int,data):
        '''Add text to the document.
        
            option should be one of 3 values: F_INCOME, F_CATEGORIES, F_OPTIONS or F_OTEXPENSES'''
        if option == self.F_CATEGORIES:
            fileObj = open(self.categoriesPath, 'a')
            fileObj.write(data)
            fileObj.close()
        elif option == self.F_INCOME:
            fileObj = open(self.incomePath, 'a')
            fileObj.write(data)
            fileObj.close()
        elif option == self.F_OPTIONS:
            fileObj = open(self.optionsPath, 'a')
            fileObj.write(data)
            fileObj.close()
        elif option == self.F_OTEXPENSES:
            fileObj = open(self.otExpensesPath, 'a')
            fileObj.write(data)
            fileObj.close()
        else:
            print("ERROR: NOT A SUITABLE FILE OPTION IN appendData() CALL")


    def getData(self, option : int):
        '''Retrieve data from document, filter through this raw data as you please.
        
            option should be one of 3 values: F_INCOME, F_CATEGORIES, F_OPTIONS or F_OTEXPENSES'''
        if option == self.F_CATEGORIES:
            fileObj = open(self.categoriesPath, 'r')
            return fileObj.readlines()
        elif option == self.F_INCOME:
            fileObj = open(self.incomePath, 'r')
            return fileObj.readlines()
        elif option == self.F_OPTIONS:
            fileObj = open(self.optionsPath, 'r')
            return fileObj.readlines()
        elif option == self.F_OTEXPENSES:
            fileObj = open(self.otExpensesPath, 'r')
            return fileObj.readlines()
        else:
            print("ERROR: NOT A SUITABLE FILE OPTION IN getData() CALL")
    


    ############################### DATA SAVING/RETREIVING ###############################
    '''     File saving convention:
            
            categories:
            name,amount,period|name,amount,period

            income:
            amount,period,occurences|amount,period,occurences

            options:
            budgetPeriod|opt2 etc

            one time expenses:
            name,amount|name,amount
    '''


    ## CATEGORY FILE SPECIFICS

    def retrieveCategoriesData(self):
        '''Takes all data from the file and puts it back into a list of tuples of 3 elements. name,amount,period. Returns None if there is no data present <- THIS NEEDS TO BE CHECKED FOR'''
        data = self.getData(self.F_CATEGORIES)
        if data is not None and len(data) > 0:
            # remove [0] if you change it back to \n separation again
            dataStr = data[0]
            
            listToReturn = []

            triplets = dataStr.split('|') # separated into name,amount,period triplets
            for expenseData in triplets:
                splitPair = expenseData.split(",") # separated into name, amount and period elements
                tupleCategory = (splitPair[0],float(splitPair[1]),splitPair[2])
                listToReturn.append(tupleCategory)
                
            return listToReturn
        else:
            return None

    def saveCategoriesData(self, listData):
        '''Completely overwrites categories file with the new data in the list of tuples'''
        #clear file first
        self.overwrite(self.F_CATEGORIES, "")
        print("Cleared expense category save file")
        i = 0
        print("Saving new expense category data")
        for expenseTuple in listData:
            # the last element in the dictionary that is being saved should not have a | after it
            if (i+1) >= len(listData):
                self.appendData(self.F_CATEGORIES, str(expenseTuple[0]) + "," + str(expenseTuple[1]) + "," + str(expenseTuple[2]))
            else:
                self.appendData(self.F_CATEGORIES, str(expenseTuple[0]) + "," + str(expenseTuple[1]) + "," + str(expenseTuple[2]) + "|")
            i+=1

        print("Expense category data saved")


    ## INCOME FILE SPECIFICS

    def retrieveIncomeData(self):
        '''Takes all data from the file and puts it back into list of tuples form. Returns None if there is no data present <- THIS NEEDS TO BE CHECKED FOR'''
        data = self.getData(self.F_INCOME)
        if data is not None and len(data) > 0:
            # remove [0] if you change it back to \n separation again
            dataStr = data[0]
            listToReturn = []
            pairs = dataStr.split('|') # separated into amount,period,occcurences pairs
            for pair in pairs:
                splitPair = pair.split(",") # separated into amount, period and occurences elements
                amount = int(float(splitPair[0])) # needs to be converted to float first to avoid ValueError
                period = str(splitPair[1])
                occurences = int(splitPair[2])
                listToReturn.append((amount, period, occurences))
            return listToReturn
        else:
            return None

    def saveIncomeData(self, incomeList):
        '''Completely overwrites income file with the new data in the list'''
        #clear file first
        self.overwrite(self.F_INCOME, "")
        print("Cleared income save file")
        i = 0
        print("Saving new income data")
        for item in incomeList:
            # the last element in the list that is being saved should not have a | after it
            if (i+1) >= len(incomeList):
                self.appendData(self.F_INCOME, str(item[0]) + "," + str(item[1]) + "," + str(item[2]))
            else:
                self.appendData(self.F_INCOME, str(item[0]) + "," + str(item[1]) + "," + str(item[2]) + "|")
            i+=1

        print("Income data saved")


    ######### OPTIONS FILE SPECIFICS
    
    def retrieveOptionsData(self):
        '''Retrieves option save data. \n
        OPTIONS DATA SHOULD BE LOWERCASE'''
        data = self.getData(self.F_OPTIONS)
        print(len(data))
        listToReturn = []
        if data is not None and len(data) > 0:
            dataItems = data[0].split("|")
            listToReturn.append(str(dataItems[0]).lower())
            listToReturn.append(int(dataItems[1]))
            return listToReturn
        else:
            print("No options data saved, using default")
            return ["weekly", 52]
        
    def saveOptionsData(self, dataList):
        '''Saves the options data

            period|occurences
        '''
        # clear file
        print("saving options data")
        self.overwrite(self.F_OPTIONS, "")
        if len(dataList) > 0:
            i = 0
            for dataItem in dataList:
                if i+1 == len(dataList):
                    self.appendData(self.F_OPTIONS, str(dataItem))
                else:
                    self.appendData(self.F_OPTIONS, str(dataItem) + "|")
                i+=1
        else:
            print("NO OPTIONS DATA TO SAVE")
        
        print("finished saving options data")


    ######### ONE TIME EXPENSE FILE SPECIFICS
    
    def retrieveOTExpensesData(self):
        '''Takes all data from the file and puts it back into dictionary form. Returns None if there is no data present <- THIS NEEDS TO BE CHECKED FOR'''
        data = self.getData(self.F_OTEXPENSES)
        if data is not None and len(data) > 0:
            # remove [0] if you change it back to \n separation again
            dataStr = data[0]
            
            dictToReturn = {}

            pairs = dataStr.split('|') # separated into name,amount pairs
            for pair in pairs:
                splitPair = pair.split(",") # separated into name and amount elements
                key = splitPair[0]
                val = round(float(splitPair[1]), 2) # will be a value for money so store as rounded float to 2dp
                dictToReturn[key] = val
            return dictToReturn
        else:
            return None
        
    def saveOTExpensesData(self, dictionary):
        '''Completely overwrites one time expenses file with the new data in the dictionary'''
        #clear file first
        self.overwrite(self.F_OTEXPENSES, "")
        print("Cleared one time expense save file")
        i = 0
        print("Saving new one time expense data")
        for key in dictionary:
            # the last element in the dictionary that is being saved should not have a | after it
            if (i+1) >= len(dictionary):
                self.appendData(self.F_OTEXPENSES, str(key) + "," + str(dictionary[key]))
            else:
                self.appendData(self.F_OTEXPENSES, str(key) + "," + str(dictionary[key]) + "|")
            i+=1

        print("One time expense data saved")