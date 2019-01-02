import sys
from PyQt4 import QtGui, QtCore

class Window (QtGui.QMainWindow):


    #always there whatever what
    def __init__ (self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Vision Bank ATM")
        self.setWindowIcon(QtGui.QIcon("python.png"))
        self.home()

    #changes based on each page
    def home(self):
        #exit button
        btn = QtGui.QPushButton("EXIT", self)
        btn.clicked.connect(self.close_app)
        #btn.resize(100,50)        
        btn.move(100,100)

        #checkbox
        chkbox = QtGui.QCheckBox('Enlarge!', self)
        chkbox.stateChanged.connect(self.enlarge_window)

        #file picker
        openFile = QtGui.QPushButton("pick", self)
        openFile.clicked.connect(self.file_open)
        
        #combo
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Enter your ID:", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("cde")
        comboBox.addItem("Windows")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("Plastique")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)


        #editor
        openEditor = QtGui.QPushButton("open Editor", self)        
        openEditor.setStatusTip("Open Editor")
        openEditor.clicked.connect(self.show_editor)
        openEditor.move(200,200)
        
        self.show()


    #choosing style
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    #file open
    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')

            
    #enlarge window
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 900)
        else:
            self.setGeometry(50, 50, 500, 500)

    #editor
    def show_editor(self) :
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

        openEditor = QtGui.QPushButton("save file", self)                
        openEditor.clicked.connect(self.save_file)
        openEditor.move(300,300)

    #save file
    def save_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        

    #exit method
    def close_app(self):
        msgbox = QtGui.QMessageBox.question(self, "Exit?",
                                            "Are you sure you wanna Exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if msgbox == QtGui.QMessageBox.Yes:        
            print("App Shutdown")
            sys.exit()
        else:
            pass

        

#main driver
def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


#call the driver to get your hands dirty
main()    


        
        
