# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deposite.ui'
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

class Ui_depositeForm(object):
    def setupUi(self, depositeForm):
        depositeForm.setObjectName(_fromUtf8("depositeForm"))
        depositeForm.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(depositeForm.sizePolicy().hasHeightForWidth())
        depositeForm.setSizePolicy(sizePolicy)
        depositeForm.setMinimumSize(QtCore.QSize(859, 572))
        depositeForm.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        depositeForm.setWindowIcon(icon)
        self.lineEdit = QtGui.QLineEdit(depositeForm)
        self.lineEdit.setGeometry(QtCore.QRect(590, 140, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color:rgb(0,0,0);"))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(depositeForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 140, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:black;\n"
"color:white\n"
""))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(depositeForm)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 140, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(_fromUtf8("background-color:black;\n"
"color:white\n"
""))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.twoHunTxt = QtGui.QLineEdit(depositeForm)
        self.twoHunTxt.setGeometry(QtCore.QRect(110, 300, 161, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(36)
        self.twoHunTxt.setFont(font)
        self.twoHunTxt.setMaxLength(2)
        self.twoHunTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.twoHunTxt.setObjectName(_fromUtf8("twoHunTxt"))
        self.hunTxt = QtGui.QLineEdit(depositeForm)
        self.hunTxt.setGeometry(QtCore.QRect(350, 300, 161, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(36)
        self.hunTxt.setFont(font)
        self.hunTxt.setMaxLength(2)
        self.hunTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.hunTxt.setObjectName(_fromUtf8("hunTxt"))
        self.fiftyTxt = QtGui.QLineEdit(depositeForm)
        self.fiftyTxt.setGeometry(QtCore.QRect(590, 300, 161, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(36)
        self.fiftyTxt.setFont(font)
        self.fiftyTxt.setMaxLength(2)
        self.fiftyTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.fiftyTxt.setObjectName(_fromUtf8("fiftyTxt"))
        self.exitBtn = QtGui.QPushButton(depositeForm)
        self.exitBtn.setGeometry(QtCore.QRect(740, 490, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.backBtn = QtGui.QPushButton(depositeForm)
        self.backBtn.setGeometry(QtCore.QRect(630, 490, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.nextBtn = QtGui.QPushButton(depositeForm)
        self.nextBtn.setGeometry(QtCore.QRect(520, 490, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))

        self.retranslateUi(depositeForm)
        QtCore.QMetaObject.connectSlotsByName(depositeForm)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        self.exitBtn.clicked.connect(self.exit)
        self.nextBtn.clicked.connect(self.next)
        self.backBtn.clicked.connect(self.back)

    def retranslateUi(self, depositeForm):
        depositeForm.setWindowTitle(_translate("depositeForm", "VisionBank ATM", None))
        self.lineEdit.setText(_translate("depositeForm", "50", None))
        self.lineEdit_2.setText(_translate("depositeForm", "100", None))
        self.lineEdit_3.setText(_translate("depositeForm", "200", None))
        self.twoHunTxt.setText(_translate("depositeForm", "30", None))
        self.hunTxt.setText(_translate("depositeForm", "30", None))
        self.fiftyTxt.setText(_translate("depositeForm", "30", None))
        self.exitBtn.setText(_translate("depositeForm", "EXIT", None))
        self.backBtn.setText(_translate("depositeForm", "BACK", None))
        self.nextBtn.setText(_translate("depositeForm", "NEXT", None))

    def exit(self):
        print("exit")

    def next(self):
        print("next")
        
    def back(self):
        print("back")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    depositeForm = QtGui.QWidget()
    ui = Ui_depositeForm()
    ui.setupUi(depositeForm)
    depositeForm.show()
    sys.exit(app.exec_())

