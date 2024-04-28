### CODE IN THIS DOCUMENT IS MOSTLY COPY-PASTED FROM ui.py

from PyQt5 import QtCore, QtGui, QtWidgets

class IncomeSourceTile:
    def __init__(self, parent : QtWidgets.QWidget, verticalLayout : QtWidgets.QVBoxLayout):
        ''' parent is incomeScrollAreaContents, vertical layout is verticalLayout_3'''
        self.parent = parent



        self.incomeSourceParentWidget = QtWidgets.QWidget(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incomeSourceParentWidget.sizePolicy().hasHeightForWidth())
        self.incomeSourceParentWidget.setSizePolicy(sizePolicy)
        self.incomeSourceParentWidget.setMinimumSize(QtCore.QSize(835, 100))
        self.incomeSourceParentWidget.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.incomeSourceParentWidget.setObjectName("incomeSourceParentWidget")
        self.incomeAmountSpinBox = QtWidgets.QDoubleSpinBox(self.incomeSourceParentWidget)
        self.incomeAmountSpinBox.setGeometry(QtCore.QRect(5, 35, 140, 50))
        self.incomeAmountSpinBox.setStyleSheet("border-style: solid;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"background-color: rgb(250,250,250);\n"
"")
        self.incomeAmountSpinBox.setMaximum(1000000.0)
        self.incomeAmountSpinBox.setProperty("value", 30000.0)
        self.incomeAmountSpinBox.setObjectName("incomeAmountSpinBox")
        self.incomeAmountLbl = QtWidgets.QLabel(self.incomeSourceParentWidget)
        self.incomeAmountLbl.setGeometry(QtCore.QRect(10, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        self.incomeAmountLbl.setFont(font)
        self.incomeAmountLbl.setObjectName("incomeAmountLbl")
        self.incomePeriodComboBox = QtWidgets.QComboBox(self.incomeSourceParentWidget)
        self.incomePeriodComboBox.setGeometry(QtCore.QRect(280, 35, 151, 50))
        self.incomePeriodComboBox.setStyleSheet("border-style: solid;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"background-color: white;\n"
"")
        self.incomePeriodComboBox.setObjectName("incomePeriodComboBox")
        self.incomePeriodComboBox.addItem("")
        self.incomePeriodComboBox.addItem("")
        self.incomePeriodComboBox.addItem("")
        self.incomePeriodComboBox.addItem("")
        self.incomePeriodComboBox.addItem("")
        self.incomeAdd100Button = QtWidgets.QPushButton(self.incomeSourceParentWidget)
        self.incomeAdd100Button.setGeometry(QtCore.QRect(160, 35, 50, 25))
        self.incomeAdd100Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(75,175,0);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35,155,0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(15,135,0);\n"
"\n"
"}")
        self.incomeAdd100Button.setObjectName("incomeAdd100Button")
        self.incomeMinus100Button = QtWidgets.QPushButton(self.incomeSourceParentWidget)
        self.incomeMinus100Button.setGeometry(QtCore.QRect(160, 60, 50, 25))
        self.incomeMinus100Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,175,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,155,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(210,135,0);\n"
"\n"
"}")
        self.incomeMinus100Button.setObjectName("incomeMinus100Button")
        self.incomeAdd1000Button = QtWidgets.QPushButton(self.incomeSourceParentWidget)
        self.incomeAdd1000Button.setGeometry(QtCore.QRect(210, 35, 50, 25))
        self.incomeAdd1000Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(125,225,0);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(105,205,0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85,185,0);\n"
"\n"
"}")
        self.incomeAdd1000Button.setObjectName("incomeAdd1000Button")
        self.incomeMinus1000Button = QtWidgets.QPushButton(self.incomeSourceParentWidget)
        self.incomeMinus1000Button.setGeometry(QtCore.QRect(210, 60, 50, 25))
        self.incomeMinus1000Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250,100,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,80,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(210,60,0);\n"
"\n"
"}")
        self.incomeMinus1000Button.setObjectName("incomeMinus1000Button")
        self.incomePeriodLbl = QtWidgets.QLabel(self.incomeSourceParentWidget)
        self.incomePeriodLbl.setGeometry(QtCore.QRect(280, 10, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        self.incomePeriodLbl.setFont(font)
        self.incomePeriodLbl.setObjectName("incomePeriodLbl")
        self.incomeOccurencesSpinBox = QtWidgets.QSpinBox(self.incomeSourceParentWidget)
        self.incomeOccurencesSpinBox.setGeometry(QtCore.QRect(470, 40, 111, 41))
        self.incomeOccurencesSpinBox.setStyleSheet("border-style: solid;\n"
"border-color: black;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"background-color: rgb(250,250,250);\n"
"")
        self.incomeOccurencesSpinBox.setProperty("value", 50)
        self.incomeOccurencesSpinBox.setObjectName("incomeOccurencesSpinBox")
        self.incomeOccurencesLbl = QtWidgets.QLabel(self.incomeSourceParentWidget)
        self.incomeOccurencesLbl.setGeometry(QtCore.QRect(470, 10, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        self.incomeOccurencesLbl.setFont(font)
        self.incomeOccurencesLbl.setObjectName("incomeOccurencesLbl")
        self.removeIncomeButton = QtWidgets.QPushButton(self.incomeSourceParentWidget)
        self.removeIncomeButton.setGeometry(QtCore.QRect(740, 10, 80, 80))
        self.removeIncomeButton.setStyleSheet("QPushButton {\n"
"    background-color: red;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(30,30,30);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(210,0,0);\n"
"    border-color: rgb(15,15,15);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170,0,0);\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        


        ### initialise values and text
        _translate = QtCore.QCoreApplication.translate
        self.incomeAmountLbl.setText(_translate("BGBudgeter", "Income Amount:"))
        self.incomePeriodComboBox.setItemText(0, _translate("BGBudgeter", "Weekly"))
        self.incomePeriodComboBox.setItemText(1, _translate("BGBudgeter", "Fortnightly"))
        self.incomePeriodComboBox.setItemText(2, _translate("BGBudgeter", "Monthly"))
        self.incomePeriodComboBox.setItemText(3, _translate("BGBudgeter", "Annually"))
        self.incomePeriodComboBox.setItemText(4, _translate("BGBudgeter", "Student Maintenance Loan (UK)"))
        self.incomeAdd100Button.setText(_translate("BGBudgeter", "+100"))
        self.incomeMinus100Button.setText(_translate("BGBudgeter", "-100"))
        self.incomeAdd1000Button.setText(_translate("BGBudgeter", "+1000"))
        self.incomeMinus1000Button.setText(_translate("BGBudgeter", "-1000"))
        self.incomePeriodLbl.setText(_translate("BGBudgeter", "Pay Period/Cycle Length:"))
        self.incomeOccurencesLbl.setText(_translate("BGBudgeter", "How Many Times Per Year Are You Paid?"))
        self.removeIncomeButton.setText(_translate("BGBudgeter", "REMOVE"))





        self.removeIncomeButton.setObjectName("removeIncomeButton")
        verticalLayout.addWidget(self.incomeSourceParentWidget)