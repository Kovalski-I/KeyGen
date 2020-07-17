# 3rd party imports
from PyQt5.QtWidgets import QDialog, QGraphicsScene
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic

# python imports
import string
import random
import os

# local imports
from widgets.messageBox import MessageBox
import resources
import glob

class AddWindow(QDialog):
    def __init__(self, parent = None, edit = False, card = None):
        super().__init__(parent = parent)
        uic.loadUi(os.getcwd() + "\\ui\\addWindow.ui", self)

        self.setWindowTitle('Adding Service Card')
        self.setModal(True)
        self.lengthSliderValueChanged()

        self._edit = edit
        self._card = card
        self.upper = True

        # creating animations
        self.caseToolButtonAnim = QPropertyAnimation(
            self.caseToolButton, b'geometry'
        )
        self.keyToolButtonAnim = QPropertyAnimation(
            self.keyToolButton, b'geometry'
        )

        # assigning event handlers
        self.caseToolButton.clicked.connect(self.caseToolButtonClicked)
        self.keyToolButton.clicked.connect(self.keyToolButtonClicked)
        self.lengthSlider.valueChanged.connect(self.lengthSliderValueChanged)
        self.caseToolButtonAnim.finished.connect(
            self.caseToolButtonAnimFinished
        )
        self.keyToolButtonAnim.finished.connect(
            self.keyToolButtonAnimFinished
        )

    def caseToolButtonClicked(self):
        glob.doAnimation(self.caseToolButtonAnim, self.caseToolButton, 4)

        text = self.passwordEdit.text()
        if self.upper:
            text = text.upper()
            self.upper = False
        else:
            text = text.lower()
            self.upper = True

        self.passwordEdit.setText(text)

    def keyToolButtonClicked(self):
        glob.doAnimation(self.keyToolButtonAnim, self.keyToolButton, 4)

        convenient_symbols = ''

        if self.numbersBox.isChecked():
            for i in range(10):
                convenient_symbols += str(i)
        if self.lettersBox.isChecked():
            convenient_symbols += string.ascii_lowercase

        password = ''
        try:
            for i in range(self.lengthSlider.value()):
                password += random.choice(convenient_symbols)
        # if none of the boxes are checked
        except IndexError:
            pass

        self.passwordEdit.setText(password)

    ''' The method sets value text to the QLabel next to the slider '''
    def lengthSliderValueChanged(self):
        value = str(self.lengthSlider.value())
        if len(value) == 1:
            self.lengthLabel.setText(value + '   ') # 3 spaces
        else:
            self.lengthLabel.setText(value + ' ') # 1 space

    def keyPressEvent(self, ev):
        # Enter
        if ev.key() == 16777220:
            self.addServiceCard()

    def addServiceCard(self):
        messageBox = MessageBox(parent = self.parent())

        if self.serviceEdit.text().strip() == '':
            messageBox.messageText.setText('Should provide service name')
            messageBox.show()
            return
        if self.passwordEdit.text() == '':
            messageBox.messageText.setText('Should provide password')
            messageBox.show()
            return

        mainWindow = self.parent()

        if self.isEdit():
            index_ = self.editedCard().data()['index']
            mainWindow.scene().delete(index_)
        else:
            index_ = len(mainWindow.scene().serviceCards())

        mainWindow.addServiceCard(
            name = self.serviceEdit.text().strip(),
            login = self.loginEdit.text().strip(),
            index = index_,
            password = self.passwordEdit.text()
        )

        self.close()

    def isEdit(self):
        return self._edit

    def editedCard(self):
        return self._card

    def caseToolButtonAnimFinished(self):
        self.caseToolButton.clicked.connect(self.caseToolButtonClicked)

    def keyToolButtonAnimFinished(self):
        self.keyToolButton.clicked.connect(self.keyToolButtonClicked)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication([])
    win = AddWindow()
    win.show()
    sys.exit(app.exec_())
