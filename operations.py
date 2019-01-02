# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operations.ui'
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

class Ui_servicesForm(object):
    def setupUi(self, servicesForm):
        servicesForm.setObjectName(_fromUtf8("servicesForm"))
        servicesForm.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(servicesForm.sizePolicy().hasHeightForWidth())
        servicesForm.setSizePolicy(sizePolicy)
        servicesForm.setMinimumSize(QtCore.QSize(859, 572))
        servicesForm.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        servicesForm.setWindowIcon(icon)
        self.withdrawBtn = QtGui.QPushButton(servicesForm)
        self.withdrawBtn.setGeometry(QtCore.QRect(466, 180, 141, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gadugi"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.withdrawBtn.setFont(font)
        self.withdrawBtn.setObjectName(_fromUtf8("withdrawBtn"))
        self.depositeBtn = QtGui.QPushButton(servicesForm)
        self.depositeBtn.setGeometry(QtCore.QRect(466, 260, 141, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gadugi"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.depositeBtn.setFont(font)
        self.depositeBtn.setObjectName(_fromUtf8("depositeBtn"))
        self.servicesBtn = QtGui.QPushButton(servicesForm)
        self.servicesBtn.setGeometry(QtCore.QRect(250, 180, 201, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gadugi"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.servicesBtn.setFont(font)
        self.servicesBtn.setObjectName(_fromUtf8("servicesBtn"))
        self.exitBtn = QtGui.QPushButton(servicesForm)
        self.exitBtn.setGeometry(QtCore.QRect(740, 490, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))

        self.retranslateUi(servicesForm)
        QtCore.QMetaObject.connectSlotsByName(servicesForm)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        self.exitBtn.clicked.connect(self.exit)
        self.withdrawBtn.clicked.connect(self.withdraw)
        self.depositeBtn.clicked.connect(self.deposite)
        self.servicesBtn.clicked.connect(self.services)

    def retranslateUi(self, servicesForm):
        servicesForm.setWindowTitle(_translate("servicesForm", "VisionBank ATM", None))
        self.withdrawBtn.setText(_translate("servicesForm", "Withdraw", None))
        self.depositeBtn.setText(_translate("servicesForm", "Deposite", None))
        self.servicesBtn.setText(_translate("servicesForm", "Services", None))
        self.exitBtn.setText(_translate("servicesForm", "EXIT", None))

    def exit(self):
        print("exit")

    def withdraw(self):
        print("with")

    def deposite(self):
        print("dep")
        
    def services(self):
        print("servic")
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    servicesForm = QtGui.QWidget()
    ui = Ui_servicesForm()
    ui.setupUi(servicesForm)
    servicesForm.show()
    sys.exit(app.exec_())

