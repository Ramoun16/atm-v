# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'withdraw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WithdrawForm(object):

    user_amount = 0
    
    def setupUi(self, WithdrawForm):
        WithdrawForm.setObjectName(_fromUtf8("WithdrawForm"))
        WithdrawForm.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WithdrawForm.sizePolicy().hasHeightForWidth())
        WithdrawForm.setSizePolicy(sizePolicy)
        WithdrawForm.setMinimumSize(QtCore.QSize(859, 572))
        WithdrawForm.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WithdrawForm.setWindowIcon(icon)
        self.OneThoBtn = QtGui.QPushButton(WithdrawForm)
        self.OneThoBtn.setGeometry(QtCore.QRect(0, 230, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.OneThoBtn.setFont(font)
        self.OneThoBtn.setObjectName(_fromUtf8("OneThoBtn"))
        self.twoThoBtn = QtGui.QPushButton(WithdrawForm)
        self.twoThoBtn.setGeometry(QtCore.QRect(0, 380, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.twoThoBtn.setFont(font)
        self.twoThoBtn.setObjectName(_fromUtf8("twoThoBtn"))
        self.fiveHunBtn = QtGui.QPushButton(WithdrawForm)
        self.fiveHunBtn.setGeometry(QtCore.QRect(0, 80, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.fiveHunBtn.setFont(font)
        self.fiveHunBtn.setObjectName(_fromUtf8("fiveHunBtn"))
        self.twoHunBtn = QtGui.QPushButton(WithdrawForm)
        self.twoHunBtn.setGeometry(QtCore.QRect(640, 380, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.twoHunBtn.setFont(font)
        self.twoHunBtn.setObjectName(_fromUtf8("twoHunBtn"))
        self.hunBtn = QtGui.QPushButton(WithdrawForm)
        self.hunBtn.setGeometry(QtCore.QRect(640, 230, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.hunBtn.setFont(font)
        self.hunBtn.setObjectName(_fromUtf8("hunBtn"))
        self.fiftyBtn = QtGui.QPushButton(WithdrawForm)
        self.fiftyBtn.setGeometry(QtCore.QRect(640, 80, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.fiftyBtn.setFont(font)
        self.fiftyBtn.setObjectName(_fromUtf8("fiftyBtn"))
        self.nextBtn = QtGui.QPushButton(WithdrawForm)
        self.nextBtn.setGeometry(QtCore.QRect(520, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.backBtn = QtGui.QPushButton(WithdrawForm)
        self.backBtn.setGeometry(QtCore.QRect(630, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.exitBtn = QtGui.QPushButton(WithdrawForm)
        self.exitBtn.setGeometry(QtCore.QRect(740, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.customBtn = QtGui.QPushButton(WithdrawForm)
        self.customBtn.setGeometry(QtCore.QRect(0, 490, 219, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magnum Sans Pro   20"))
        font.setPointSize(36)
        self.customBtn.setFont(font)
        self.customBtn.setStyleSheet(_fromUtf8("color:white;\n"
        "background-color:tomato;\n"
        "align:center;\n"
        "valign:center;\n"
        ""))
        self.customBtn.setObjectName(_fromUtf8("customBtn"))

        self.retranslateUi(WithdrawForm)
        QtCore.QMetaObject.connectSlotsByName(WithdrawForm)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        ################events###################3
        self.exitBtn.clicked.connect(self.exit)
        self.nextBtn.clicked.connect(self.next)
        self.backBtn.clicked.connect(self.back)
        self.fiftyBtn.clicked.connect(self.fifty)
        self.hunBtn.clicked.connect(self.hun)
        self.twoHunBtn.clicked.connect(self.twoHun)
        self.fiveHunBtn.clicked.connect(self.fiveHun)
        self.OneThoBtn.clicked.connect(self.oneTho)
        self.twoThoBtn.clicked.connect(self.twoTho)
        self.customBtn.clicked.connect(self.custom)
        ##########################################

    def retranslateUi(self, WithdrawForm):
        WithdrawForm.setWindowTitle(_translate("WithdrawForm", "VisionBank ATM", None))
        self.OneThoBtn.setText(_translate("WithdrawForm", "1000", None))
        self.twoThoBtn.setText(_translate("WithdrawForm", "2000", None))
        self.fiveHunBtn.setText(_translate("WithdrawForm", "500", None))
        self.twoHunBtn.setText(_translate("WithdrawForm", "200", None))
        self.hunBtn.setText(_translate("WithdrawForm", "100", None))
        self.fiftyBtn.setText(_translate("WithdrawForm", "50", None))
        self.nextBtn.setText(_translate("WithdrawForm", "NEXT", None))
        self.backBtn.setText(_translate("WithdrawForm", "BACK", None))
        self.exitBtn.setText(_translate("WithdrawForm", "EXIT", None))
        self.customBtn.setText(_translate("WithdrawForm", "custom", None))


    def exit(self):
        print("exit")

    def next(self):
        print("next")
        
    def back(self):
        print("back")
        
    def custom(self):
        print("custom")
        
    def fifty(self):
        user_amount = 50
        
    def hun(self):
        user_amount = 100
        
    def twoHun(self):
        user_amount = 200

    def fiveHun(self):
        user_amount = 500
        
    def oneTho(self):
        user_amount = 1000

    def twoTho(self):
        user_amount = 2000
        
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WithdrawForm = QtGui.QWidget()
    ui = Ui_WithdrawForm()
    ui.setupUi(WithdrawForm)
    WithdrawForm.show()
    sys.exit(app.exec_())

