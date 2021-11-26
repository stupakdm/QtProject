# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import numpy as np
from math import *

class UI_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setWindowIcon(QIcon('calculator.png'))
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(299, 400)
        self.stak = []
        self.page = 0
        self.operations = [['+', '-', '*', '/'],
                    ['sin','cos','tg','ctg'],
                    ['ln', 'abs', '%',  'exp']]
        self.base_operator = ''
        self.num = 1
        self.res = 0
        self.prev_oper = 0
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_curr = QLabel(self.centralwidget)
        self.label_curr.setObjectName(u"label_curr")
        self.label_curr.setGeometry(QRect(0, 0, 300, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_curr.sizePolicy().hasHeightForWidth())
        self.label_curr.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_curr.setFont(font1)
        self.label_curr.setStyleSheet(u"background-color: rgb(171, 166, 171);\n"
"color: rgb(255, 255, 255);")
        self.label_curr.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(0, 100, 75, 75))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_7.setIconSize(QSize(16, 16))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(75, 100, 75, 75))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_equal = QPushButton(self.centralwidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setGeometry(QRect(225, 100, 75, 100))
        self.pushButton_equal.setFont(font1)
        self.pushButton_equal.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(150, 100, 75, 75))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(0, 250, 75, 75))
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(75, 250, 75, 75))
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(150, 250, 75, 75))
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(0, 325, 150, 75))
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(0, 175, 75, 75))
        self.pushButton_16.setFont(font1)
        self.pushButton_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(75, 175, 75, 75))
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(150, 175, 75, 75))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_clean = QPushButton(self.centralwidget)
        self.pushButton_clean.setObjectName(u"pushButton_clean")
        self.pushButton_clean.setGeometry(QRect(225, 200, 75, 100))
        self.pushButton_clean.setFont(font1)
        self.pushButton_clean.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setGeometry(QRect(30, 50, 60, 50))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_plus.setFont(font3)
        self.pushButton_plus.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_minus = QPushButton(self.centralwidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setGeometry(QRect(90, 50, 60, 50))
        self.pushButton_minus.setFont(font3)
        self.pushButton_minus.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_div = QPushButton(self.centralwidget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.pushButton_div.setGeometry(QRect(210, 50, 60, 50))
        self.pushButton_div.setFont(font3)
        self.pushButton_div.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_mul = QPushButton(self.centralwidget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        self.pushButton_mul.setGeometry(QRect(150, 50, 60, 50))
        self.pushButton_mul.setFont(font3)
        self.pushButton_mul.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.label_prev = QLabel(self.centralwidget)
        self.label_prev.setObjectName(u"label_prev")
        self.label_prev.setGeometry(QRect(0, 0, 300, 25))
        self.label_prev.setFont(font)
        self.label_prev.setStyleSheet(u"color: rgb(34, 34, 34);")
        self.label_prev.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pushButton_period = QPushButton(self.centralwidget)
        self.pushButton_period.setObjectName(u"pushButton_period")
        self.pushButton_period.setGeometry(QRect(150, 325, 75, 75))
        self.pushButton_period.setFont(font1)
        self.pushButton_period.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setGeometry(QRect(225, 300, 75, 100))
        self.pushButton_reset.setFont(font1)
        self.pushButton_reset.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_left = QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setGeometry(QRect(0, 50, 30, 50))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_left.setFont(font4)
        self.pushButton_left.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.pushButton_left.setEnabled(False)
        self.pushButton_right = QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setEnabled(True)
        self.pushButton_right.setGeometry(QRect(270, 50, 30, 50))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_right.setFont(font5)
        self.pushButton_right.setStyleSheet(u"background-color: rgb(201, 211, 202);")
        self.label_left = QLabel(self.centralwidget)
        self.label_left.setObjectName(u"label_left")
        self.label_left.setGeometry(QRect(0, 85, 30, 15))
        font6 = QFont()
        font6.setPointSize(8)
        font6.setBold(False)
        font6.setWeight(50)
        self.label_left.setFont(font6)
        self.label_left.setAlignment(Qt.AlignCenter)
        self.label_right = QLabel(self.centralwidget)
        self.label_right.setObjectName(u"label_right")
        self.label_right.setGeometry(QRect(270, 85, 30, 15))
        self.label_right.setFont(font6)
        self.label_right.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.label_curr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_clean.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_mul.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_prev.setText("")
        self.pushButton_period.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Res", None))
        self.pushButton_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_left.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.label_right.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
    # retranslateUi



    def add_functions(self):
        self.pushButton_7.clicked.connect(lambda: self.write_number(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.write_number(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_number(self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(lambda: self.write_number(self.pushButton_10.text()))
        self.pushButton_11.clicked.connect(lambda: self.write_number(self.pushButton_11.text()))
        self.pushButton_12.clicked.connect(lambda: self.write_number(self.pushButton_12.text()))
        self.pushButton_13.clicked.connect(lambda: self.write_number(self.pushButton_13.text()))
        self.pushButton_14.clicked.connect(lambda: self.write_number(self.pushButton_14.text()))
        self.pushButton_15.clicked.connect(lambda: self.write_number(self.pushButton_15.text()))
        self.pushButton_16.clicked.connect(lambda: self.write_number(self.pushButton_16.text()))
        self.pushButton_period.clicked.connect(lambda: self.write_number(self.pushButton_period.text()))
        self.pushButton_clean.clicked.connect(lambda: self.clean())
        self.pushButton_plus.clicked.connect(lambda: self.operation(self.pushButton_plus.text()))
        self.pushButton_minus.clicked.connect(lambda: self.operation(self.pushButton_minus.text()))
        self.pushButton_mul.clicked.connect(lambda: self.operation(self.pushButton_mul.text()))
        self.pushButton_div.clicked.connect(lambda: self.operation(self.pushButton_div.text()))
        self.pushButton_equal.clicked.connect(lambda: self.result())
        self.pushButton_left.clicked.connect(lambda: self.turn_left())
        self.pushButton_right.clicked.connect(lambda: self.turn_right())
        self.pushButton_reset.clicked.connect(lambda: self.reset())


    def stack_form(self, prev, new_str):
        self.stak.append(prev)
        self.label_prev.setText(str(prev))
        self.label_curr.setText(new_str)

    def write_number(self, symb):
        if (self.res == 1):
            if (self.label_curr.text() in '+-*/'):
                if (symb == '.'):
                    self.label_curr.setText('0.')
                else:
                    self.label_curr.setText(symb)
            else:
                prev = float(self.label_curr.text())
                new_str = ''
                if (symb == '.'):
                    new_str = '0.'
                else:
                    new_str = symb
                self.stack_form(prev, new_str)
            self.res = 0
            #self.num = 1
        elif ((self.label_curr.text() =='0') or self.label_curr.text() in '*-+/'):
            if (symb == '.'):
                self.label_curr.setText('0.')
            else:
                self.label_curr.setText(symb)
        else:
            self.label_curr.setText(self.label_curr.text()+symb)

    def clean(self):
        self.label_curr.setText('0')
        self.res = 0
        self.num = 1
        self.base_operator = ''

    def basic_result(self, num1, num2, operation):
        res = 0
        if (operation =='+'):
            res = num1+num2
        elif (operation == '-'):
            res = num1-num2
        elif (operation == '*'):
            res = num1*num2
        elif (operation == '/'):
            res = num1/num2

        if ((res*10)%10 == 0):
            return int(res)
        else:
            return res

    def basic_operations(self, symb):
        if (self.label_curr.text() not in '+-*/'):
            prev = 0
            if (self.num == 1):
                prev = float(self.label_curr.text())
                self.num = 2
            else:
                res = self.basic_result(self.stak[-1], float(self.label_curr.text()), self.base_operator)
                prev= res
                self.num = 2
                self.res = 1
                self.prev_oper = 1
            self.stack_form(prev, symb)

                #self.stack_form(prev, symb)
                #self.num = 2
            #elif (self.num == 2):
                #res = self.basic_result(self.stak[-1], float(self.label_curr.text()), self.base_operator)
                #prev = res
                #self.stack_form(res, symb)
                #self.num = 1
                #self.res = 1
        else:
            self.label_curr.setText(symb)
        self.base_operator = symb

    def trigonometric(self, symb):
        prev = float(self.label_curr.text())
        res = 0
        if (symb == 'sin'):
            res = np.sin(prev)
        if (symb == 'cos'):
            res = np.cos(prev)
        if (symb == 'tg'):
            res = tan(prev)
        if (symb == 'ctg'):
            res = 1/tan(prev)
        self.stack_form(prev, str(res))
        self.num = 1
        self.res = 1

    def other_operations(self, symb): #'ln(x)', 'abs(x)', '%',  'exp(x)'
        prev = float(self.label_curr.text())
        if (symb == 'ln'):
            res = np.log(prev)
        if (symb == 'abs'):
            res = abs(prev)
        if (symb == '%'):
            res = prev/100
        if (symb == 'exp'):
            res = np.exp(prev)
        self.stack_form(prev, str(res))
        self.num = 1
        self.res = 1

    def operation(self, symb):
        if (self.page ==0):
            self.basic_operations(symb)
        if (self.page == 1):
            self.trigonometric(symb)
        if (self.page ==2):
            self.other_operations(symb)


    def result(self):
        if (self.num == 2):
            res = self.basic_result(self.stak[-1], float(self.label_curr.text()), self.base_operator)
            prev =float(self.label_curr.text())
            self.stack_form(prev, str(res))
            self.num = 1
        self.res = 1
        self.base_operator =''



    def turn_btn(self):
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", self.operations[self.page][0], None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", self.operations[self.page][1], None))
        self.pushButton_mul.setText(QCoreApplication.translate("MainWindow", self.operations[self.page][2], None))
        self.pushButton_div.setText(QCoreApplication.translate("MainWindow", self.operations[self.page][3], None))
        self.label_left.setText(QCoreApplication.translate("MainWindow", str(self.page+1)+"/3", None))
        self.label_right.setText(QCoreApplication.translate("MainWindow", str(self.page+1)+"/3", None))

    def turn_left(self):
        if (self.page==0):
            self.pushButton_left.setEnabled(False)
        else:
            if (self.page == 2):
                self.pushButton_right.setEnabled(True)
            if (self.page == 1):
                self.pushButton_left.setEnabled(False)
            self.page -=1
            self.turn_btn()

    def turn_right(self):
        if (self.page==2):
            self.pushButton_right.setEnabled(False)
        else:
            if (self.page == 0):
                self.pushButton_left.setEnabled(True)
            if (self.page == 1):
                self.pushButton_right.setEnabled(False)
            self.page +=1
            self.turn_btn()

    def reset(self):
        if (len(self.stak)==0):
            self.label_prev.setText('')
            self.label_curr.setText('0')
        else:
            if (len(self.stak)==1):
                self.label_prev.setText('')
            else:
                self.label_prev.setText(str(self.stak[-2]))
            self.label_curr.setText(str(self.stak[-1]))
            self.stak.pop()
        self.num = 1
        self.res = 1



