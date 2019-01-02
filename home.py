# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
##from DB import *
##from chk import *
##from money import *
from pin import Ui_PinForm
from errors import *

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(859, 572))
        Form.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(280, 140, 311, 41))
        self.lineEdit.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 110, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.EnterBtn = QtGui.QPushButton(Form)
        self.EnterBtn.setGeometry(QtCore.QRect(370, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EnterBtn.setFont(font)
        self.EnterBtn.setFlat(False)
        self.EnterBtn.setObjectName(_fromUtf8("EnterBtn"))
        #######################Enter event############
        self.EnterBtn.clicked.connect(self.idCheck)
        ##############################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "VisionBank ATM", None))
        self.label.setText(_translate("Form", "Enter your ID", None))
        self.EnterBtn.setText(_translate("Form", "Enter", None))

    def idCheck(self):
##        Id = self.lineEdit.text()
##        id = chkinput(Id)
        if (0):
            self.welcomeWindow = QtGui.QMainWindow()
            self.ui = Ui_PinForm()
            self.ui.setupUi(self.welcomeWindow)
            Form.hide()
            self.welcomeWindow.show()
        else:
            self.errorWindow = QtGui.QMainWindow()
            self.ui = Ui_errorForm()
            self.ui.setupUi(self.errorWindow)
            Form.hide()
            self.errorWindow.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

