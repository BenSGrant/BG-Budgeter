from fileHandler import FileHandler
from ui import Ui_BGBudgeter


class OptionManager:
    def __init__(self, dialog : Ui_BGBudgeter):
        self.fileHand = FileHandler()