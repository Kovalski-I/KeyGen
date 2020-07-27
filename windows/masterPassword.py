'''
This class implements a window which requests to fill the
password when openning the app.

'''

# 3rd party imports
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import uic

# python imports
import base64
import json
import os

# local imports
from widgets.messageBox import MessageBox
import glob

class MasterPasswordWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent = parent)

        # reading ui from ui/masterPassword.ui
        uic.loadUi(os.getcwd() + "\\ui\\masterPassword.ui", self)

        self.setWindowTitle(self.parent().windowTitle())
        self.setModal(True)

        # creating animations
        self.pushButtonAnim = QPropertyAnimation(self.pushButton, b'geometry')

        # bool of whether the entered password is correct
        self.correct_password_entered = False

        # how many times an incorrect password has been entered
        self.incorrect_times = 0

        # creating messageBox in case if entered password is incorrect
        self.messageBox = MessageBox(parent = self)
        self.messageBox.setWindowTitle(self.windowTitle())
        self.messageBox.messageText.setText('Incorrect master password')

        # assigning handlers
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButtonAnim.finished.connect(
            lambda: self.pushButton.clicked.connect(self.pushButtonClicked)
        )

    def pushButtonClicked(self):
        glob.doAnimation(self.pushButtonAnim, self.pushButton, 4)

        json_data = json.loads(open('keygen.json', 'rt').read())
        encoded_real_password = base64.b64decode(
            json_data['enterData']['masterPassword'].encode()
        )
        real_password = encoded_real_password.decode()

        if self.lineEdit.text() == real_password:
            self.correct_password_entered = True
            self.close()
        else:
            if self.incorrect_times > 2:
                self.hintLabel.setText(
                    'Hint: ' + json_data['enterData']['hint']
                )
            self.messageBox.show()
            self.incorrect_times += 1

    def closeEvent(self, ev):
        ev.accept() if self.correct_password_entered else self.parent().close()
