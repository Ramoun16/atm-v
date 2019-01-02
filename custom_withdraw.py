# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_withdraw.ui'
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

class Ui_cusWithForm(object):
    def setupUi(self, cusWithForm):
        cusWithForm.setObjectName(_fromUtf8("cusWithForm"))
        cusWithForm.resize(859, 572)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cusWithForm.sizePolicy().hasHeightForWidth())
        cusWithForm.setSizePolicy(sizePolicy)
        cusWithForm.setMinimumSize(QtCore.QSize(859, 572))
        cusWithForm.setMaximumSize(QtCore.QSize(859, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cusWithForm.setWindowIcon(icon)
        self.lineEdit = QtGui.QLineEdit(cusWithForm)
        self.lineEdit.setGeometry(QtCore.QRect(280, 160, 311, 41))
        self.lineEdit.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(cusWithForm)
        self.label.setGeometry(QtCore.QRect(330, 130, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.EnterBtn = QtGui.QPushButton(cusWithForm)
        self.EnterBtn.setGeometry(QtCore.QRect(370, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EnterBtn.setFont(font)
        self.EnterBtn.setFlat(False)
        self.EnterBtn.setObjectName(_fromUtf8("EnterBtn"))
        self.backBtn = QtGui.QPushButton(cusWithForm)
        self.backBtn.setGeometry(QtCore.QRect(630, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.nextBtn = QtGui.QPushButton(cusWithForm)
        self.nextBtn.setGeometry(QtCore.QRect(520, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.exitBtn = QtGui.QPushButton(cusWithForm)
        self.exitBtn.setGeometry(QtCore.QRect(740, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yoxall"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))

        self.retranslateUi(cusWithForm)
        QtCore.QMetaObject.connectSlotsByName(cusWithForm)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        self.exitBtn.clicked.connect(self.exit)
        self.nextBtn.clicked.connect(self.next)
        self.backBtn.clicked.connect(self.back)
        self.EnterBtn.clicked.connect(self.amount)

    def retranslateUi(self, cusWithForm):
        cusWithForm.setWindowTitle(_translate("cusWithForm", "VisionBank ATM", None))
        self.label.setText(_translate("cusWithForm", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Custom Amount</span></p></body></html>", None))
        self.EnterBtn.setText(_translate("cusWithForm", "Enter", None))
        self.backBtn.setText(_translate("cusWithForm", "BACK", None))
        self.nextBtn.setText(_translate("cusWithForm", "NEXT", None))
        self.exitBtn.setText(_translate("cusWithForm", "EXIT", None))

    def exit(self):
        print("exit")

    def next(self):
        print("next")
        
    def back(self):
        print("back")

    def amount(self):
        amount = self.lineEdit.text()
        print(amount)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cusWithForm = QtGui.QWidget()
    ui = Ui_cusWithForm()
    ui.setupUi(cusWithForm)
    cusWithForm.show()
    sys.exit(app.exec_())

