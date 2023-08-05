# create a Qt5 window and display a text in it

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, Qt

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('PyQt5 App')
# window.setGeometry(100, 100, 280, 80)
# window.move(60, 15)
label = QLabel('Hello \nWorld!', parent=window)
window.setCentralWidget(label)


window.show()
app.processEvents()
app.exec_()