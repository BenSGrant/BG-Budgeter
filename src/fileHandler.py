import os

class FileHandler:
    def __init__(self):
        #this makes the app windows only as %appdata% is only defined in Windows
        #as far as im aware. If anyone knows anything about how to make this work
        #on Linux/Mac, please let me know by creating an issue on the GitHub repo
        self.dirPath = os.getenv('APPDATA') + "\\BG-Budgeter\\"
    
    def overwrite(data):
        '''completely replace all text in the document.

            File saving convention:
        '''

    def appendData(data):
        '''add text to the document'''

    def getData(data):
        '''retrieve data from document, filter through this raw data as you please'''