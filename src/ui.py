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
        self.mainPageTtl.setGeometry(QtCore.QRect(0, 0, 900, 60))
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
        self.mainPageInfoLbl.setGeometry(QtCore.QRect(25, 79, 221, 511))
        self.mainPageInfoLbl.setText("")
        self.mainPageInfoLbl.setObjectName("mainPageInfoLbl")
        self.incomePageButton = QtWidgets.QPushButton(self.mainPage)
        self.incomePageButton.setGeometry(QtCore.QRect(275, 80, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.incomePageButton.setFont(font)
        self.incomePageButton.setObjectName("incomePageButton")
        self.categoryPageButton = QtWidgets.QPushButton(self.mainPage)
        self.categoryPageButton.setGeometry(QtCore.QRect(275, 180, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.categoryPageButton.setFont(font)
        self.categoryPageButton.setObjectName("categoryPageButton")
        self.optionsPageButton = QtWidgets.QPushButton(self.mainPage)
        self.optionsPageButton.setGeometry(QtCore.QRect(275, 380, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.optionsPageButton.setFont(font)
        self.optionsPageButton.setObjectName("optionsPageButton")
        self.viewBudgetPageButton = QtWidgets.QPushButton(self.mainPage)
        self.viewBudgetPageButton.setGeometry(QtCore.QRect(275, 480, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.viewBudgetPageButton.setFont(font)
        self.viewBudgetPageButton.setObjectName("viewBudgetPageButton")
        self.oneTimeExpensesPageButton = QtWidgets.QPushButton(self.mainPage)
        self.oneTimeExpensesPageButton.setGeometry(QtCore.QRect(275, 280, 350, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.oneTimeExpensesPageButton.setFont(font)
        self.oneTimeExpensesPageButton.setObjectName("oneTimeExpensesPageButton")
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
        self.incomeSourcesScrollArea.setGeometry(QtCore.QRect(10, 100, 880, 350))
        self.incomeSourcesScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.incomeSourcesScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.incomeSourcesScrollArea.setWidgetResizable(True)
        self.incomeSourcesScrollArea.setObjectName("incomeSourcesScrollArea")
        self.incomeScrollAreaContents = QtWidgets.QWidget()
        self.incomeScrollAreaContents.setGeometry(QtCore.QRect(0, 0, 857, 348))
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
        self.addIncomeButton = QtWidgets.QPushButton(self.incomeInputPage)
        self.addIncomeButton.setGeometry(QtCore.QRect(750, 460, 140, 47))
        self.addIncomeButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0,220,100);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(30,30,30);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,200,80);\n"
"    border-color: rgb(15,15,15);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0,180,60);\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.addIncomeButton.setObjectName("addIncomeButton")
        self.updateIncomeButton = QtWidgets.QPushButton(self.incomeInputPage)
        self.updateIncomeButton.setGeometry(QtCore.QRect(375, 520, 150, 50))
        self.updateIncomeButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,180,0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(30,30,30);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,160,0);\n"
"    border-color: rgb(15,15,15);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(210,140,0);\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.updateIncomeButton.setObjectName("updateIncomeButton")
        self.incomeTipsLbl = QtWidgets.QLabel(self.incomeInputPage)
        self.incomeTipsLbl.setGeometry(QtCore.QRect(20, 460, 281, 111))
        self.incomeTipsLbl.setObjectName("incomeTipsLbl")
        self.incomeHintLbl = QtWidgets.QLabel(self.incomeInputPage)
        self.incomeHintLbl.setGeometry(QtCore.QRect(10, 60, 880, 35))
        self.incomeHintLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.incomeHintLbl.setObjectName("incomeHintLbl")
        self.studentMaintenanceDetected = QtWidgets.QLabel(self.incomeInputPage)
        self.studentMaintenanceDetected.setGeometry(QtCore.QRect(330, 460, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.studentMaintenanceDetected.setFont(font)
        self.studentMaintenanceDetected.setText("")
        self.studentMaintenanceDetected.setObjectName("studentMaintenanceDetected")
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
        self.categoryTable.setGeometry(QtCore.QRect(10, 120, 880, 400))
        self.categoryTable.setObjectName("categoryTable")
        self.categoryTable.setColumnCount(0)
        self.categoryTable.setRowCount(0)
        self.categoryNameInputLE = QtWidgets.QLineEdit(self.categoryPage)
        self.categoryNameInputLE.setGeometry(QtCore.QRect(10, 65, 180, 50))
        self.categoryNameInputLE.setObjectName("categoryNameInputLE")
        self.addCategoryButton = QtWidgets.QPushButton(self.categoryPage)
        self.addCategoryButton.setGeometry(QtCore.QRect(730, 65, 160, 40))
        self.addCategoryButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(100,200,100);\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85,185,85);\n"
"    border-color: rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60,160,60);\n"
"    border-color: black;\n"
"}\n"
"")
        self.addCategoryButton.setObjectName("addCategoryButton")
        self.categoryAmountSpinBox = QtWidgets.QDoubleSpinBox(self.categoryPage)
        self.categoryAmountSpinBox.setGeometry(QtCore.QRect(315, 65, 110, 50))
        self.categoryAmountSpinBox.setMaximum(1000000000.0)
        self.categoryAmountSpinBox.setProperty("value", 50.0)
        self.categoryAmountSpinBox.setObjectName("categoryAmountSpinBox")
        self.expenseAmountLbl = QtWidgets.QLabel(self.categoryPage)
        self.expenseAmountLbl.setGeometry(QtCore.QRect(195, 70, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.expenseAmountLbl.setFont(font)
        self.expenseAmountLbl.setObjectName("expenseAmountLbl")
        self.plus10Button = QtWidgets.QPushButton(self.categoryPage)
        self.plus10Button.setGeometry(QtCore.QRect(430, 70, 50, 20))
        self.plus10Button.setObjectName("plus10Button")
        self.minus10Button = QtWidgets.QPushButton(self.categoryPage)
        self.minus10Button.setGeometry(QtCore.QRect(430, 90, 50, 20))
        self.minus10Button.setObjectName("minus10Button")
        self.plus100Button = QtWidgets.QPushButton(self.categoryPage)
        self.plus100Button.setGeometry(QtCore.QRect(480, 70, 50, 20))
        self.plus100Button.setObjectName("plus100Button")
        self.minus100Button = QtWidgets.QPushButton(self.categoryPage)
        self.minus100Button.setGeometry(QtCore.QRect(480, 90, 50, 20))
        self.minus100Button.setObjectName("minus100Button")
        self.categoryErrLbl = QtWidgets.QLabel(self.categoryPage)
        self.categoryErrLbl.setGeometry(QtCore.QRect(360, 530, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.categoryErrLbl.setFont(font)
        self.categoryErrLbl.setStyleSheet("color: red;")
        self.categoryErrLbl.setText("")
        self.categoryErrLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryErrLbl.setObjectName("categoryErrLbl")
        self.expenseInfoLbl = QtWidgets.QLabel(self.categoryPage)
        self.expenseInfoLbl.setGeometry(QtCore.QRect(20, 530, 281, 51))
        self.expenseInfoLbl.setObjectName("expenseInfoLbl")
        self.categoryPeriodComboBox = QtWidgets.QComboBox(self.categoryPage)
        self.categoryPeriodComboBox.setGeometry(QtCore.QRect(620, 70, 91, 41))
        self.categoryPeriodComboBox.setObjectName("categoryPeriodComboBox")
        self.categoryPeriodComboBox.addItem("")
        self.categoryPeriodComboBox.addItem("")
        self.categoryPeriodComboBox.addItem("")
        self.categoryPeriodComboBox.addItem("")
        self.categoryPeriodComboBox.addItem("")
        self.categoryPeriodOptionLbl = QtWidgets.QLabel(self.categoryPage)
        self.categoryPeriodOptionLbl.setGeometry(QtCore.QRect(540, 70, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.categoryPeriodOptionLbl.setFont(font)
        self.categoryPeriodOptionLbl.setObjectName("categoryPeriodOptionLbl")
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
        self.weeklyBudgetRadioButton = QtWidgets.QRadioButton(self.optionsPage)
        self.weeklyBudgetRadioButton.setGeometry(QtCore.QRect(290, 230, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.weeklyBudgetRadioButton.setFont(font)
        self.weeklyBudgetRadioButton.setObjectName("weeklyBudgetRadioButton")
        self.fortnightlyBudgetRadioButton = QtWidgets.QRadioButton(self.optionsPage)
        self.fortnightlyBudgetRadioButton.setGeometry(QtCore.QRect(290, 255, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.fortnightlyBudgetRadioButton.setFont(font)
        self.fortnightlyBudgetRadioButton.setObjectName("fortnightlyBudgetRadioButton")
        self.timePeriodOptionLbl = QtWidgets.QLabel(self.optionsPage)
        self.timePeriodOptionLbl.setGeometry(QtCore.QRect(265, 200, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.timePeriodOptionLbl.setFont(font)
        self.timePeriodOptionLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.timePeriodOptionLbl.setObjectName("timePeriodOptionLbl")
        self.monthlyBudgetRadioButton = QtWidgets.QRadioButton(self.optionsPage)
        self.monthlyBudgetRadioButton.setGeometry(QtCore.QRect(290, 280, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.monthlyBudgetRadioButton.setFont(font)
        self.monthlyBudgetRadioButton.setObjectName("monthlyBudgetRadioButton")
        self.updateOptionsButton = QtWidgets.QPushButton(self.optionsPage)
        self.updateOptionsButton.setGeometry(QtCore.QRect(375, 450, 150, 50))
        self.updateOptionsButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,180,0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(30,30,30);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,160,0);\n"
"    border-color: rgb(15,15,15);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(210,140,0);\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.updateOptionsButton.setObjectName("updateOptionsButton")
        self.budgetPeriodOccurencesSpinBox = QtWidgets.QSpinBox(self.optionsPage)
        self.budgetPeriodOccurencesSpinBox.setGeometry(QtCore.QRect(515, 250, 150, 41))
        self.budgetPeriodOccurencesSpinBox.setMaximum(52)
        self.budgetPeriodOccurencesSpinBox.setObjectName("budgetPeriodOccurencesSpinBox")
        self.budgetOccurencesLbl = QtWidgets.QLabel(self.optionsPage)
        self.budgetOccurencesLbl.setGeometry(QtCore.QRect(500, 190, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.budgetOccurencesLbl.setFont(font)
        self.budgetOccurencesLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.budgetOccurencesLbl.setObjectName("budgetOccurencesLbl")
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
        self.budgetTable = QtWidgets.QTableWidget(self.viewBudgetPage)
        self.budgetTable.setGeometry(QtCore.QRect(10, 70, 880, 450))
        self.budgetTable.setObjectName("budgetTable")
        self.budgetTable.setColumnCount(0)
        self.budgetTable.setRowCount(0)
        self.stackedWidget.addWidget(self.viewBudgetPage)
        self.oneTimeExpensesPage = QtWidgets.QWidget()
        self.oneTimeExpensesPage.setObjectName("oneTimeExpensesPage")
        self.otPlus100Button = QtWidgets.QPushButton(self.oneTimeExpensesPage)
        self.otPlus100Button.setGeometry(QtCore.QRect(580, 70, 50, 20))
        self.otPlus100Button.setObjectName("otPlus100Button")
        self.addOTExpenseButton = QtWidgets.QPushButton(self.oneTimeExpensesPage)
        self.addOTExpenseButton.setGeometry(QtCore.QRect(730, 65, 160, 40))
        self.addOTExpenseButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(100,200,100);\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85,185,85);\n"
"    border-color: rgb(25,25,25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(60,160,60);\n"
"    border-color: black;\n"
"}\n"
"")
        self.addOTExpenseButton.setObjectName("addOTExpenseButton")
        self.otExpenseErrLbl = QtWidgets.QLabel(self.oneTimeExpensesPage)
        self.otExpenseErrLbl.setGeometry(QtCore.QRect(350, 530, 530, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.otExpenseErrLbl.setFont(font)
        self.otExpenseErrLbl.setStyleSheet("color: red;")
        self.otExpenseErrLbl.setText("")
        self.otExpenseErrLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.otExpenseErrLbl.setObjectName("otExpenseErrLbl")
        self.otExpenseBackButton = QtWidgets.QPushButton(self.oneTimeExpensesPage)
        self.otExpenseBackButton.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.otExpenseBackButton.setStyleSheet("QPushButton {\n"
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
        self.otExpenseBackButton.setObjectName("otExpenseBackButton")
        self.otExpenseAmountLbl = QtWidgets.QLabel(self.oneTimeExpensesPage)
        self.otExpenseAmountLbl.setGeometry(QtCore.QRect(295, 70, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.otExpenseAmountLbl.setFont(font)
        self.otExpenseAmountLbl.setObjectName("otExpenseAmountLbl")
        self.otMinus100Button = QtWidgets.QPushButton(self.oneTimeExpensesPage)
        self.otMinus100Button.setGeometry(QtCore.QRect(580, 90, 50, 20))
        self.otMinus100Button.setObjectName("otMinus100Button")
        self.oneTimeExpensePageTtl = QtWidgets.QLabel(self.oneTimeExpensesPage)
        self.oneTimeExpensePageTtl.setGeometry(QtCore.QRect(0, 0, 900, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.oneTimeExpensePageTtl.setFont(font)
        self.oneTimeExpensePageTtl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 200, 50, 255), stop:1 rgba(255, 80, 100, 255));")
        self.oneTimeExpensePageTtl.setAlignment(QtCore.Qt.AlignCenter)
        self.oneTimeExpensePageTtl.setObjectName("oneTimeExpensePageTtl")
        self.otExpenseNameInputLE = QtWidgets.QLineEdit(self.oneTimeExpensesPage)
        self.otExpenseNameInputLE.setGeometry(QtCore.QRect(10, 65, 281, 50))
        self.otExpenseNameInputLE.setObjectName("otExpenseNameInputLE")
        self.otMinus10Button = QtWidgets.QPushButton(self.oneTimeExpensesPage)
        self.otMinus10Button.setGeometry(QtCore.QRect(530, 90, 50, 20))
        self.otMinus10Button.setObjectName("otMinus10Button")
        self.otPlus10Button = QtWidgets.QPushButton(self.oneTimeExpensesPage)
        self.otPlus10Button.setGeometry(QtCore.QRect(530, 70, 50, 20))
        self.otPlus10Button.setObjectName("otPlus10Button")
        self.otExpenseSpinBox = QtWidgets.QDoubleSpinBox(self.oneTimeExpensesPage)
        self.otExpenseSpinBox.setGeometry(QtCore.QRect(415, 65, 110, 50))
        self.otExpenseSpinBox.setMaximum(1000000000.0)
        self.otExpenseSpinBox.setProperty("value", 50.0)
        self.otExpenseSpinBox.setObjectName("otExpenseSpinBox")
        self.otExpenseInfoLbl = QtWidgets.QLabel(self.oneTimeExpensesPage)
        self.otExpenseInfoLbl.setGeometry(QtCore.QRect(20, 530, 291, 61))
        self.otExpenseInfoLbl.setObjectName("otExpenseInfoLbl")
        self.otExpenseTable = QtWidgets.QTableWidget(self.oneTimeExpensesPage)
        self.otExpenseTable.setGeometry(QtCore.QRect(10, 120, 880, 400))
        self.otExpenseTable.setObjectName("otExpenseTable")
        self.otExpenseTable.setColumnCount(0)
        self.otExpenseTable.setRowCount(0)
        self.otPlus100Button.raise_()
        self.addOTExpenseButton.raise_()
        self.otExpenseErrLbl.raise_()
        self.otExpenseAmountLbl.raise_()
        self.otMinus100Button.raise_()
        self.oneTimeExpensePageTtl.raise_()
        self.otExpenseNameInputLE.raise_()
        self.otMinus10Button.raise_()
        self.otPlus10Button.raise_()
        self.otExpenseSpinBox.raise_()
        self.otExpenseInfoLbl.raise_()
        self.otExpenseTable.raise_()
        self.otExpenseBackButton.raise_()
        self.stackedWidget.addWidget(self.oneTimeExpensesPage)

        self.retranslateUi(BGBudgeter)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BGBudgeter)

    def retranslateUi(self, BGBudgeter):
        _translate = QtCore.QCoreApplication.translate
        BGBudgeter.setWindowTitle(_translate("BGBudgeter", "BG-Budgeter"))
        self.mainPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter"))
        self.incomePageButton.setText(_translate("BGBudgeter", "Income"))
        self.categoryPageButton.setText(_translate("BGBudgeter", "Regular Expense Category Settings"))
        self.optionsPageButton.setText(_translate("BGBudgeter", "Extra Options"))
        self.viewBudgetPageButton.setText(_translate("BGBudgeter", "View Budget"))
        self.oneTimeExpensesPageButton.setText(_translate("BGBudgeter", "One-Time Expenses"))
        self.incomePageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Choose Your Income Sources"))
        self.incomeBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.addIncomeButton.setText(_translate("BGBudgeter", "Add Income Source"))
        self.updateIncomeButton.setText(_translate("BGBudgeter", "UPDATE"))
        self.incomeTipsLbl.setText(_translate("BGBudgeter", "Tips:\n"
"- You can manually enter an amount into the\n"
"  income amount option box\n"
"- The occurences option details how many\n"
"  times per year you are paid. For example,\n"
"  200 a week 50 times a year is a yearly\n"
"  income total of 10000"))
        self.incomeHintLbl.setText(_translate("BGBudgeter", "Hint: If you choose the student maintenance option in the income period drop down box, the number of\n"
"occurences you put does not matter, you can ignore it."))
        self.categoryPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Choose Your Expense Categories"))
        self.categoryBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.categoryNameInputLE.setPlaceholderText(_translate("BGBudgeter", "Expense Name"))
        self.addCategoryButton.setText(_translate("BGBudgeter", "ADD"))
        self.expenseAmountLbl.setText(_translate("BGBudgeter", "Expense Amount:"))
        self.plus10Button.setText(_translate("BGBudgeter", "+10"))
        self.minus10Button.setText(_translate("BGBudgeter", "-10"))
        self.plus100Button.setText(_translate("BGBudgeter", "+100"))
        self.minus100Button.setText(_translate("BGBudgeter", "-100"))
        self.expenseInfoLbl.setText(_translate("BGBudgeter", "The expense amount is how much you expect\n"
"to pay during each budget period"))
        self.categoryPeriodComboBox.setItemText(0, _translate("BGBudgeter", "Weekly"))
        self.categoryPeriodComboBox.setItemText(1, _translate("BGBudgeter", "Monthly"))
        self.categoryPeriodComboBox.setItemText(2, _translate("BGBudgeter", "Every 3 Months"))
        self.categoryPeriodComboBox.setItemText(3, _translate("BGBudgeter", "Every 6 Months"))
        self.categoryPeriodComboBox.setItemText(4, _translate("BGBudgeter", "Annually"))
        self.categoryPeriodOptionLbl.setText(_translate("BGBudgeter", "How often\n"
"you pay:"))
        self.optionsPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Extra Options"))
        self.optionsBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.weeklyBudgetRadioButton.setText(_translate("BGBudgeter", "Weekly"))
        self.fortnightlyBudgetRadioButton.setText(_translate("BGBudgeter", "Fortnightly"))
        self.timePeriodOptionLbl.setText(_translate("BGBudgeter", "Budget Time Period"))
        self.monthlyBudgetRadioButton.setText(_translate("BGBudgeter", "Monthly"))
        self.updateOptionsButton.setText(_translate("BGBudgeter", "UPDATE"))
        self.budgetOccurencesLbl.setText(_translate("BGBudgeter", "How many weeks\n"
"the budget will cover"))
        self.viewBudgetPageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  View Your Budget"))
        self.viewBudgetBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.otPlus100Button.setText(_translate("BGBudgeter", "+100"))
        self.addOTExpenseButton.setText(_translate("BGBudgeter", "ADD"))
        self.otExpenseBackButton.setText(_translate("BGBudgeter", "BACK"))
        self.otExpenseAmountLbl.setText(_translate("BGBudgeter", "Expense Amount:"))
        self.otMinus100Button.setText(_translate("BGBudgeter", "-100"))
        self.oneTimeExpensePageTtl.setText(_translate("BGBudgeter", "BG-Budgeter  -  Specify Your One Time Expenses"))
        self.otExpenseNameInputLE.setPlaceholderText(_translate("BGBudgeter", "Expense Name"))
        self.otMinus10Button.setText(_translate("BGBudgeter", "-10"))
        self.otPlus10Button.setText(_translate("BGBudgeter", "+10"))
        self.otExpenseInfoLbl.setText(_translate("BGBudgeter", "For example, £600 on a new laptop. This will be\n"
"deducted from your calculated annual income \n"
"(which is used to calculate your budget)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BGBudgeter = QtWidgets.QDialog()
    ui = Ui_BGBudgeter()
    ui.setupUi(BGBudgeter)
    BGBudgeter.show()
    sys.exit(app.exec_())
