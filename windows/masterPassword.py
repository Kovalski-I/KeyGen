# 3rd party imports
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic

# python imports
import os

# local imports
from window.mainWindow import MainWindow

class MasterPasswordWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.getcwd() + "\\ui\\masterPassword.ui", self)

        # creating animations
        self.pushButtonAnim = QPropertyAnimation(self.pushButton, b'geometry')

        # assigning handlers
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButtonAnim.finished.connect(
            lambda: self.pushButton.clicked.connect(self.pushButtonClicked)
        )

    def pushButtonClicked(self):
        MainWindow.doAnimation(self.pushButtonAnim, self.pushButton, 4)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication([])
    win = MasterPasswordWindow()
    win.show()
    sys.exit(app.exec_())
