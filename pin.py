# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
##from DB import *
##from chk import *
##from money import *


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

class Ui_PinForm(object):
    def setupUi(self, PinForm):
        PinForm.setObjectName(_fromUtf8("PinForm"))
        PinForm.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PinForm.sizePolicy().hasHeightForWidth())
        PinForm.setSizePolicy(sizePolicy)
        PinForm.setMinimumSize(QtCore.QSize(859, 572))
        PinForm.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PinForm.setWindowIcon(icon)
        self.pin_txt = QtGui.QLineEdit(PinForm)
        self.pin_txt.setGeometry(QtCore.QRect(280, 170, 311, 41))
        self.pin_txt.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pin_txt.setFont(font)
        self.pin_txt.setInputMask(_fromUtf8(""))
        self.pin_txt.setMaxLength(4)
        self.pin_txt.setFrame(True)
        self.pin_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.pin_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.pin_txt.setObjectName(_fromUtf8("pin_txt"))
        self.label = QtGui.QLabel(PinForm)
        self.label.setGeometry(QtCore.QRect(370, 140, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.EnterBtn = QtGui.QPushButton(PinForm)
        self.EnterBtn.setGeometry(QtCore.QRect(370, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EnterBtn.setFont(font)
        self.EnterBtn.setFlat(False)
        self.EnterBtn.setObjectName(_fromUtf8("EnterBtn"))
        ##########enter btn event########
        self.EnterBtn.clicked.connect(self.checkPin)
        ###############################
        self.pushButton = QtGui.QPushButton(PinForm)
        self.pushButton.setGeometry(QtCore.QRect(740, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ###############event of exit######################
        self.pushButton.clicked.connect(self.exit)
        ##################################################

        self.retranslateUi(PinForm)
        QtCore.QMetaObject.connectSlotsByName(PinForm)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

    def retranslateUi(self, PinForm):
        PinForm.setWindowTitle(_translate("PinForm", "VisionBank ATM", None))
        self.label.setText(_translate("PinForm", "Enter your PIN", None))
        self.EnterBtn.setText(_translate("PinForm", "Enter", None))
        self.pushButton.setText(_translate("PinForm", "EXIT", None))

    def checkPin(self):
        pin = self.pin_txt.text()
        pinchk = chkinput(id.id,pin)
        pinchk.chkpin()

    def exit(self):
        pass###return back to home screen


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PinForm = QtGui.QWidget()
    ui = Ui_PinForm()
    ui.setupUi(PinForm)
    PinForm.show()
    sys.exit(app.exec_())

