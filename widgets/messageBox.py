# 3rd party imports
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5 import uic

# python imports
import os

# local imports
import glob

class MessageBox(QDialog):
    def __init__(self, parent, closable = True):
        super().__init__(parent = parent)
        self.setParent(parent)
        self.setModal(True)

        self.closable = closable

        # loading ui from ui/messageBox.ui
        uic.loadUi(os.getcwd() + '\\ui\\messageBox.ui', self)

        # creating button click animation
        self.anim = QPropertyAnimation(self.pushButton, b'geometry')

        # assigning event handler
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.anim.finished.connect(
            lambda: self.pushButton.clicked.connect(self.pushButtonClicked)
        )

    def pushButtonClicked(self):
        glob.doAnimation(self.anim, self.pushButton, 4)

        self.close()

    def closeEvent(self, ev):
        ev.accept() if self.closable else self.parent().close()
