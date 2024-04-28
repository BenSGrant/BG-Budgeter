import os

class FileHandler:
    def __init__(self):
        #this makes the app windows only as %appdata% is only defined in Windows
        #as far as im aware. If anyone knows anything about how to make this work
        #on Linux/Mac, please let me know by creating an issue on the GitHub repo
        self.dirPath = os.getenv('APPDATA') + "\\BG-Budgeter\\"
        self.categoriesPath = self.dirPath + "categories.txt"
        self.incomePath = self.dirPath + "income.txt"


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


    ### GENERAL

    def overwrite(self, isCategoriesFile: bool, data):
        '''Completely replace all text in the document.

            If isCategoriesFile is false, then income file will be assumed

            File saving convention:
            
            categories:
            name,amount|name,amount

            income:
            amount,period,occurences|amount,period,occurences
        '''
        if isCategoriesFile:
            fileObj = open(self.categoriesPath, 'w')
            fileObj.write(data)
            fileObj.close()
        else:
            fileObj = open(self.incomePath, 'w')
            fileObj.write(data)
            fileObj.close()

    def appendData(self,isCategoriesFile: bool,data):
        '''Add text to the document.
        
            If isCategoriesFile is false, then income file will be assumed'''
        if isCategoriesFile:
            fileObj = open(self.categoriesPath, 'a')
            fileObj.write(data)
            fileObj.close()
        else:
            fileObj = open(self.incomePath, 'a')
            fileObj.write(data)
            fileObj.close()
        

    def getData(self, isCategoriesFile: bool):
        '''Retrieve data from document, filter through this raw data as you please.
        
            If isCategoriesFile is false, then income file will be assumed'''
        if isCategoriesFile:
            fileObj = open(self.categoriesPath, 'r')
            return fileObj.readlines()
        else:
            fileObj = open(self.incomePath, 'r')
            return fileObj.readlines()
    

    ## CATEGORY FILE SPECIFICS

    def retrieveCategoriesData(self):
        '''Takes all data from the file and puts it back into dictionary form. Returns None if there is no data present'''
        data = self.getData(True)[0] # remove [0] if you change it back to \n separation again
        dictToReturn = {}
        if data is not None:
            pairs = data.split('|') # separated into name,amount pairs
            for pair in pairs:
                splitPair = pair.split(",") # separated into name and amount elements
                key = splitPair[0]
                val = round(float(splitPair[1]), 2) # will be a value for money so store as rounded float to 2dp
                dictToReturn[key] = val
            return dictToReturn
        else:
            return None

    def saveCategoriesData(self, dictionary):
        '''Completely overwrites categories file with the new data in the dictionary'''
        #clear file first
        self.overwrite(True, "")
        print("Cleared expense category save file")
        i = 0
        print("Saving new expense category data")
        for key in dictionary:
            # the last element in the dictionary that is being saved should not have a | after it
            if (i+1) >= len(dictionary):
                self.appendData(True, str(key) + "," + str(dictionary[key]))
            else:
                self.appendData(True, str(key) + "," + str(dictionary[key]) + "|")
            i+=1

        print("Expense category data saved")


    ## INCOME FILE SPECIFICS

    def retrieveIncomeData(self):
        '''Takes all data from the file and puts it back into list of tuples form. Returns None if there is no data present'''
        data = self.getData(False)[0] # remove [0] if you change it back to \n separation again
        listToReturn = []
        if data is not None:
            pairs = data.split('|') # separated into amount,period,occcurences pairs
            for pair in pairs:
                splitPair = pair.split(",") # separated into amount, period and occurences elements
                amount = int(splitPair[0])
                period = str(splitPair[1])
                occurences = int(splitPair[2])
                listToReturn.append((amount, period, occurences))
            return listToReturn
        else:
            return None

    def saveIncomeData(self, list):
        '''Completely overwrites income file with the new data in the list'''
        #clear file first
        self.overwrite(False, "")
        print("Cleared income save file")
        i = 0
        print("Saving new income data")
        for item in list:
            # the last element in the list that is being saved should not have a | after it
            if (i+1) >= len(list):
                self.appendData(False, str(item[0]) + "," + str(item[1]) + "," + str(item[2]))
            else:
                self.appendData(False, str(item[0]) + "," + str(item[1]) + "," + str(item[2]) + "|")
            i+=1

        print("Income data saved")

