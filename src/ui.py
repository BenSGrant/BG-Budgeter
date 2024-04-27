# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUiFiles/budgeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BGBudgeter(object):
    def setupUi(self, BGBudgeter):
        BGBudgeter.setObjectName("BGBudgeter")
        BGBudgeter.resize(900, 600)
        self.stackedWidget = QtWidgets.QStackedWidget(BGBudgeter)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setStyleSheet("QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(210,200,220);\n"
"}\n"
"")
        self.mainPage.setObjectName("mainPage")
        self.mainPageTtl = QtWidgets.QLabel(self.mainPage)
        self.mainPageTtl.setGeometry(QtCore.QRect(0, 0, 900, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mainPageTtl.setFont(font)
        self.mainPageTtl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 200, 50, 255), stop:1 rgba(255, 80, 100, 255));")
        self.mainPageTtl.setAlignment(QtCore.Qt.AlignCenter)
        self.mainPageTtl.setObjectName("mainPageTtl")
        self.mainPageInfoLbl = QtWidgets.QLabel(self.mainPage)
        self.mainPageInfoLbl.setGeometry(QtCore.QRect(25, 459, 850, 131))
        self.mainPageInfoLbl.setText("")
        self.mainPageInfoLbl.setObjectName("mainPageInfoLbl")
        self.incomePageButton = QtWidgets.QPushButton(self.mainPage)
        self.incomePageButton.setGeometry(QtCore.QRect(275, 60, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.incomePageButton.setFont(font)
        self.incomePageButton.setObjectName("incomePageButton")
        self.categoryPageButton = QtWidgets.QPushButton(self.mainPage)
        self.categoryPageButton.setGeometry(QtCore.QRect(275, 160, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.categoryPageButton.setFont(font)
        self.categoryPageButton.setObjectName("categoryPageButton")
        self.optionsPageButton = QtWidgets.QPushButton(self.mainPage)
        self.optionsPageButton.setGeometry(QtCore.QRect(275, 260, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.optionsPageButton.setFont(font)
        self.optionsPageButton.setObjectName("optionsPageButton")
        self.viewBudgetPageButton = QtWidgets.QPushButton(self.mainPage)
        self.viewBudgetPageButton.setGeometry(QtCore.QRect(275, 360, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.viewBudgetPageButton.setFont(font)
        self.viewBudgetPageButton.setObjectName("viewBudgetPageButton")
        self.stackedWidget.addWidget(self.mainPage)
        self.incomeInputPage = QtWidgets.QWidget()
        self.incomeInputPage.setObjectName("incomeInputPage")
        self.incomePageTtl = QtWidgets.QLabel(self.incomeInputPage)
        self.incomePageTtl.setGeometry(QtCore.QRect(0, 0, 900, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.incomePageTtl.setFont(font)
        self.incomePageTtl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 200, 50, 255), stop:1 rgba(255, 80, 100, 255));")
        self.incomePageTtl.setAlignment(QtCore.Qt.AlignCenter)
        self.incomePageTtl.setObjectName("incomePageTtl")
        self.incomeSourcesScrollArea = QtWidgets.QScrollArea(self.incomeInputPage)
        self.incomeSourcesScrollArea.setGeometry(QtCore.QRect(10, 110, 880, 340))
        self.incomeSourcesScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.incomeSourcesScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.incomeSourcesScrollArea.setWidgetResizable(True)
        self.incomeSourcesScrollArea.setObjectName("incomeSourcesScrollArea")
        self.incomeScrollAreaContents = QtWidgets.QWidget()
        self.incomeScrollAreaContents.setGeometry(QtCore.QRect(0, 0, 857, 338))
        self.incomeScrollAreaContents.setObjectName("incomeScrollAreaContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.incomeScrollAreaContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.incomeSourcesScrollArea.setWidget(self.incomeScrollAreaContents)
        self.incomeBackButton = QtWidgets.QPushButton(self.incomeInputPage)
        self.incomeBackButton.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.incomeBackButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,100,0);\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(225,75,0);\n"
"    border-color: rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,50,0);\n"
"    border-color: black;\n"
"}\n"
"")
        self.incomeBackButton.setObjectName("incomeBackButton")
        self.stackedWidget.addWidget(self.incomeInputPage)
        self.categoryPage = QtWidgets.QWidget()
        self.categoryPage.setObjectName("categoryPage")
        self.categoryPageTtl = QtWidgets.QLabel(self.categoryPage)
        self.categoryPageTtl.setGeometry(QtCore.QRect(0, 0, 900, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.categoryPageTtl.setFont(font)
        self.categoryPageTtl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 200, 50, 255), stop:1 rgba(255, 80, 100, 255));")
        self.categoryPageTtl.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryPageTtl.setObjectName("categoryPageTtl")
        self.categoryBackButton = QtWidgets.QPushButton(self.categoryPage)
        self.categoryBackButton.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.categoryBackButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,100,0);\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(225,75,0);\n"
"    border-color: rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,50,0);\n"
"    border-color: black;\n"
"}\n"
"")
        self.categoryBackButton.setObjectName("categoryBackButton")
        self.categoryTable = QtWidgets.QTableWidget(self.categoryPage)
        self.categoryTable.setGeometry(QtCore.QRect(10, 110, 880, 340))
        self.categoryTable.setObjectName("categoryTable")
        self.categoryTable.setColumnCount(0)
        self.categoryTable.setRowCount(0)
        self.categoryNameInputLE = QtWidgets.QLineEdit(self.categoryPage)
        self.categoryNameInputLE.setGeometry(QtCore.QRect(10, 65, 700, 40))
        self.categoryNameInputLE.setObjectName("categoryNameInputLE")
        self.addCategoryButton = QtWidgets.QPushButton(self.categoryPage)
        self.addCategoryButton.setGeometry(QtCore.QRect(730, 65, 160, 40))
        self.addCategoryButton.setObjectName("addCategoryButton")
        self.stackedWidget.addWidget(self.categoryPage)
        self.optionsPage = QtWidgets.QWidget()
        self.optionsPage.setObjectName("optionsPage")
        self.optionsPageTtl = QtWidgets.QLabel(self.optionsPage)
        self.optionsPageTtl.setGeometry(QtCore.QRect(0, 0, 900, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.optionsPageTtl.setFont(font)
        self.optionsPageTtl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 200, 50, 255), stop:1 rgba(255, 80, 100, 255));")
        self.optionsPageTtl.setAlignment(QtCore.Qt.AlignCenter)
        self.optionsPageTtl.setObjectName("optionsPageTtl")
        self.optionsBackButton = QtWidgets.QPushButton(self.optionsPage)
        self.optionsBackButton.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.optionsBackButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,100,0);\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(225,75,0);\n"
"    border-color: rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,50,0);\n"
"    border-color: black;\n"
"}\n"
"")
        self.optionsBackButton.setObjectName("optionsBackButton")
        self.stackedWidget.addWidget(self.optionsPage)
        self.viewBudgetPage = QtWidgets.QWidget()
        self.viewBudgetPage.setObjectName("viewBudgetPage")
        self.viewBudgetPageTtl = QtWidgets.QLabel(self.viewBudgetPage)
        self.viewBudgetPageTtl.setGeometry(QtCore.QRect(0, 0, 900, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.viewBudgetPageTtl.setFont(font)
        self.viewBudgetPageTtl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 200, 50, 255), stop:1 rgba(255, 80, 100, 255));")
        self.viewBudgetPageTtl.setAlignment(QtCore.Qt.AlignCenter)
        self.viewBudgetPageTtl.setObjectName("viewBudgetPageTtl")
        self.viewBudgetBackButton = QtWidgets.QPushButton(self.viewBudgetPage)
        self.viewBudgetBackButton.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.viewBudgetBackButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,100,0);\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(225,75,0);\n"
"    border-color: rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,50,0);\n"
"    border-color: black;\n"
"}\n"
"")
        self.viewBudgetBackButton.setObjectName("viewBudgetBackButton")
        self.stackedWidget.addWidget(self.viewBudgetPage)

        self.retranslateUi(BGBudgeter)
        QtCore.QMetaObject.connectSlotsByName(BGBudgeter)

    def retranslateUi(self, BGBudgeter):
        _translate = QtCore.QCoreApplication.translate
        BGBudgeter.setWindowTitle(_translate("BGBudgeter", "Dialog"))
        self.mainPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter"))
        self.incomePageButton.setText(_translate("BGBudgeter", "Income"))
        self.categoryPageButton.setText(_translate("BGBudgeter", "Expense Category Settings"))
        self.optionsPageButton.setText(_translate("BGBudgeter", "Extra Options"))
        self.viewBudgetPageButton.setText(_translate("BGBudgeter", "View Budget"))
        self.incomePageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Choose Your Income Sources"))
        self.incomeBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.categoryPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Choose Your Expense Categories"))
        self.categoryBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.addCategoryButton.setText(_translate("BGBudgeter", "ADD"))
        self.optionsPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Extra Options"))
        self.optionsBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.viewBudgetPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  View Your Budget"))
        self.viewBudgetBackButton.setText(_translate("BGBudgeter", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BGBudgeter = QtWidgets.QDialog()
    ui = Ui_BGBudgeter()
    ui.setupUi(BGBudgeter)
    BGBudgeter.show()
    sys.exit(app.exec_())
