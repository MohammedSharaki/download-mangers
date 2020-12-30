  
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType
#import pafy
#import humanize

import os
from os import path


FROM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))
class MainApp(QMainWindow , FROM_CLASS):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
 







def main(): #to start app 
    app = QApplication(sys.argv)
    window = MainApp() 
    window.show() #to show app
    app.exec_() #infent loop  

if __name__ == '__main__':
    main()
