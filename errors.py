# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errors.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from home import *

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

class Ui_errorForm(object):
    def setupUi(self, errorForm):
        errorForm.setObjectName(_fromUtf8("errorForm"))
        errorForm.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(errorForm.sizePolicy().hasHeightForWidth())
        errorForm.setSizePolicy(sizePolicy)
        errorForm.setMinimumSize(QtCore.QSize(859, 572))
        errorForm.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        errorForm.setWindowIcon(icon)
        self.errorTxt = QtGui.QLineEdit(errorForm)
        self.errorTxt.setGeometry(QtCore.QRect(200, 230, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.errorTxt.setFont(font)
        self.errorTxt.setStyleSheet(_fromUtf8("color:red;"))
        self.errorTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.errorTxt.setObjectName(_fromUtf8("errorTxt"))
        self.exitBtn = QtGui.QPushButton(errorForm)
        self.exitBtn.setGeometry(QtCore.QRect(740, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)        
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))

        self.retranslateUi(errorForm)
        QtCore.QMetaObject.connectSlotsByName(errorForm)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        self.exitBtn.clicked.connect(self.exit)

    def retranslateUi(self, errorForm):
        errorForm.setWindowTitle(_translate("errorForm", "VisionBank ATM", None))
        self.errorTxt.setText(_translate("errorForm", "ERRor,something went Wrong", None))
        self.exitBtn.setText(_translate("errorForm", "EXIT", None))

    def exit(self):
        self.homeWindow = QtGui.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.homeWindow)
        errorForm.hide()
        self.homeWindow.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    errorForm = QtGui.QWidget()
    ui = Ui_errorForm()
    ui.setupUi(errorForm)
    errorForm.show()
    sys.exit(app.exec_())

