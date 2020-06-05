# 3rd party imports
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic

# ptyhon imports
import os

# local imports
from windows.mainWindow import MainWindow

class GreetWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.getcwd() + "\\ui\\greetWindow.ui", self)
        self.setWindowTitle('Create Master Password')

        # creating animation
        self.buttonAnim = QPropertyAnimation(self.pushButton, b'geometry')

        # assigning event handlers
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.buttonAnim.finished.connect(self.buttonAnimFinished)

    def pushButtonClicked(self):
        MainWindow.doAnimation(self.buttonAnim, self.pushButton, 4)

    def buttonAnimFinished(self):
        self.pushButton.clicked.connect(self.pushButtonClicked)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication([])
    win = GreetWindow()
    win.show()
    sys.exit(app.exec_())
