# 3rd party imports
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import uic

# python imports
import base64
import json
import os

# local imports
from widgets.messageBox import MessageBox
import glob

class SetWindow(QDialog):
    def __init__(self, parent, closable = False):
        super().__init__(parent = parent)

        # loading ui from ui\greetWindow.ui
        uic.loadUi(os.getcwd() + "\\ui\\setWindow.ui", self)

        self.setWindowTitle('Set Master Password')
        self.setModal(True)

        # bool of whether the entered passswords are correct
        self.requirements_passed = closable

        # creating messageBox
        self.messageBox = MessageBox(parent = self)
        self.messageBox.setWindowTitle(self.windowTitle())

        # creating animation
        self.buttonAnim = QPropertyAnimation(self.pushButton, b'geometry')

        # assigning event handlers
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.buttonAnim.finished.connect(self.buttonAnimFinished)

    def pushButtonClicked(self):
        glob.doAnimation(self.buttonAnim, self.pushButton, 4)

        masterPasswordText = self.masterPasswordEdit.text()
        confirmMasterPasswordText = self.confirmMasterPasswordEdit.text()
        messageText = None

        if masterPasswordText != confirmMasterPasswordText:
            messageText = "Passwords don't match each other"
        else:
            if masterPasswordText == '':
                messageText = 'Password is empty'
            else:
                if self.hintEdit.text().strip() == '':
                    messageText = 'Must provide a hint'
                else:
                    if len(masterPasswordText) <= 4:
                        messageText = 'Password is too short\n(should be more than 4 symbols)'
                    else:
                        messageText = 'Master password has been\nsuccessfully set'
                        self.requirements_passed = True
                        # writing hint and encoded password to your_keygen.json
                        self.dumpToJson()
                        self.close()

        self.messageBox.messageText.setText(messageText)
        self.messageBox.show()

    def dumpToJson(self):
        json_data = self.parent().json()
        encoded_password =  base64.b64encode(
            self.masterPasswordEdit.text().encode()
        )

        json_data['enterData']['hint'] = self.hintEdit.text().strip()
        json_data['enterData']['masterPassword'] = encoded_password.decode()
        json_data['firstOpen'] = False

        buffer = open('keygen.json', 'wt')
        buffer.write(json.dumps(json_data, sort_keys = False, indent = 4))
        buffer.close()

    def buttonAnimFinished(self):
        self.pushButton.clicked.connect(self.pushButtonClicked)

    def closeEvent(self, ev):
        ev.accept() if self.requirements_passed else self.parent().close()
