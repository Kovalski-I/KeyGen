'''
This class implements message box which can be used in different cases.
Text of the message box is set after creating an instance.

'''

# 3rd party imports
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5 import uic

# python imports
import os

# local imports
from globalf import Glob

# ui
from ui.messageBox import Ui_Dialog

class MessageBox(QDialog, Ui_Dialog):
    def __init__(self, parent, closable = True):
        super().__init__(parent = parent)
        self.setParent(parent)

        self.setupUi(self)
        self.setModal(True)

        self.closable = closable

        # creating button click animation
        self.anim = QPropertyAnimation(self.pushButton, b'geometry')

        # assigning event handler
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.anim.finished.connect(
            lambda: self.pushButton.clicked.connect(self.pushButtonClicked)
        )

    def pushButtonClicked(self):
        Glob.doAnimation(self.anim, self.pushButton, 4)

        self.close()

    def closeEvent(self, ev):
        ev.accept() if self.closable else self.parent().close()
