import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("./ui/mainwindow.ui", self)
        
        # Setup the widgets
        self.calculateCostWidget = uic.loadUi("./ui/calculator.ui")
        self.searchEntriesWidget = uic.loadUi("./ui/search.ui")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()