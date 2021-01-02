from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import urllib.request
import os 
from os import path
import sys
FROM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))

class mainapp(QMainWindow,FROM_CLASS):
    def __init__(self,parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui()
        self.Download()
        self.handel_button()
    
    
    
    
    
    def handel_ui(self):
        self.setWindowTitle("PyDownload")
        self.setFixedSize(684,299)
    def handel_button(self):
        self.pushButton.clicked.connect(self.download)

    def handel_browse(self):
        pass

    def Handel_Progress(self, blocknum, blocksize,totalsize):
        pass


    def Download(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()

        try:
            urllib.request.urlretrieve(url,save_location,self.Handel_Progress)
        except Exception:
            QMessageBox.warning(self, "Download Error", "Download Failed")
            return

        QMessageBox.information(self,"Download Completed","Download Finished")

        self.progressBar.setValue(0)
        self.self.lineEdit.setText("")
        self.self.lineEdit_2.setText("")

def main(): 
    app=QApplication(sys.argv)
    window=mainapp()
    window.show()
    app.exec_()

if __name__=="__main__":
    main()
