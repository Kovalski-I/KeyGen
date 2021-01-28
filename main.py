'''
Main file of the application.

'''

# python imports
import sys

# 3rd party imports
from PyQt5.QtWidgets import QApplication

# local imports
from windows.mainWindow import MainWindow

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())