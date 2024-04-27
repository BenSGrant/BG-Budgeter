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
        '''this function checks if save data files do not exist, then creates them if that is the case'''
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


    def overwrite(self, isCategoriesFile, data):
        '''completely replace all text in the document.

            if isCategoriesFile is false, then income file will be assumed

            File saving convention:
            
            categories
            
            name,amount \\n

            income
            amount,period,occurences \\n

        '''
        if isCategoriesFile:
            fileObj = open(self.categoriesPath, 'w')
            fileObj.write(data)
            fileObj.close()
        else:
            fileObj = open(self.incomePath, 'w')
            fileObj.write(data)
            fileObj.close()

    def appendData(self,isCategoriesFile,data):
        '''add text to the document
        
            if isCategoriesFile is false, then income file will be assumed'''
        if isCategoriesFile:
            fileObj = open(self.categoriesPath, 'a')
            fileObj.write(data)
            fileObj.close()
        else:
            fileObj = open(self.incomePath, 'a')
            fileObj.write(data)
            fileObj.close()
        

    def getData(self, isCategoriesFile):
        '''retrieve data from document, filter through this raw data as you please.
        
            if isCategoriesFile is false, then income file will be assumed'''
        if isCategoriesFile:
            fileObj = open(self.categoriesPath, 'r')
            return fileObj.readlines()
        else:
            fileObj = open(self.incomePath, 'r')
            return fileObj.readlines()