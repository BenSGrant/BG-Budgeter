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
    
    def retrieveCategoriesData(self):
        '''Takes all data from the file and puts it back into dictionary form. Returns None if there is no data present'''
        data = self.getData(True)[0] # remove [0] if you change it back to \n separation again
        print(data)
        dictToReturn = {}
        if data is not None:
            pairs = data.split('|') # separated into name,amount pairs
            for pair in pairs:
                splitPair = pair.split(",") # separated into name and amount elements
                key = splitPair[0]
                val = round(float(splitPair[1]), 2) # will be a value for money so store as rounded float to 2dp
                dictToReturn[key] = val
                print(dictToReturn)
            return dictToReturn
        else:
            return None

    def saveCategoriesData(self, dictionary):
        # retrieve or overwrite data first before doing this depending on how this is handled in the CategoryManager class
        
        for key in dictionary:
            self.appendData(str(key) + "," + str(dictionary[key]) + "|")
