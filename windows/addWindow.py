'''
This class implements a window, using which service cards
can be added or edited.

'''

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
from globalf import Glob
import resources

# ui
from ui.addWindow import Ui_Dialog

class AddWindow(QDialog, Ui_Dialog):
    def __init__(self, parent = None, edit = False, card = None):
        super().__init__(parent = parent)

        self.setupUi(self)

        self._edit = edit
        self._card = card
        self._colors = ['#244f26', '#875307', '#01434b', '#902c25', '#4f6670']
        self.color = random.choice(self._colors)
        self.upper = True

        if self.isEdit():
            self.setBackground(self.editedCard().data()['color'])
        else:
            self.setBackground(self.color)

        if self.isEdit():
            self.setWindowTitle('Editing Service Card')
        else:
            self.setWindowTitle('Adding Service Card')

        self.setModal(True)
        self.lengthSliderValueChanged()

        # creating animations
        self.caseToolButtonAnim = QPropertyAnimation(
            self.caseToolButton, b'geometry'
        )
        self.keyToolButtonAnim = QPropertyAnimation(
            self.keyToolButton, b'geometry'
        )
        self.brushToolButtonAnim = QPropertyAnimation(
            self.brushToolButton, b'geometry'
        )

        # assigning event handlers
        self.caseToolButton.clicked.connect(self.caseToolButtonClicked)
        self.keyToolButton.clicked.connect(self.keyToolButtonClicked)
        self.brushToolButton.clicked.connect(self.brushToolButtonClicked)
        self.lengthSlider.valueChanged.connect(self.lengthSliderValueChanged)
        self.caseToolButtonAnim.finished.connect(
            self.caseToolButtonAnimFinished
        )
        self.keyToolButtonAnim.finished.connect(
            self.keyToolButtonAnimFinished
        )
        self.brushToolButtonAnim.finished.connect(
            self.brushToolButtonAnimFinished
        )

    def caseToolButtonClicked(self):
        Glob.doAnimation(self.caseToolButtonAnim, self.caseToolButton, 4)

        text = self.passwordEdit.text()
        if self.upper:
            text = text.upper()
            self.upper = False
        else:
            text = text.lower()
            self.upper = True

        self.passwordEdit.setText(text)

    def keyToolButtonClicked(self):
        Glob.doAnimation(self.keyToolButtonAnim, self.keyToolButton, 4)

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

    '''
    This method changes background color of an add window.
    '''
    def brushToolButtonClicked(self):
        Glob.doAnimation(self.brushToolButtonAnim, self.brushToolButton, 4)

        colors = self.colors().copy()
        colors.remove(self.currentColor())

        chosen_color = random.choice(colors)
        self.setBackground(chosen_color)

        self.color = chosen_color

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

    def setBackground(self, color):
        self.setStyleSheet(
            '''QWidget{
                background-color: ''' + '{0}'.format(color) + ''';
            }'''
        )

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
            mainWindow.scene().removeItem(self.editedCard())
            self.parent().json()['id'].pop(self.editedCard().data()['id'])
        else:
            index_ = len(mainWindow.scene().serviceCards())

        mainWindow.addServiceCard(
            name = self.serviceEdit.text().strip(),
            login = self.loginEdit.text().strip(),
            index = index_,
            color = self.currentColor(),
            password = self.passwordEdit.text()
        )

        self.close()

    def isEdit(self):
        return self._edit

    def editedCard(self):
        return self._card

    def colors(self):
        return self._colors

    def currentColor(self):
        return self.color

    def caseToolButtonAnimFinished(self):
        self.caseToolButton.clicked.connect(self.caseToolButtonClicked)

    def keyToolButtonAnimFinished(self):
        self.keyToolButton.clicked.connect(self.keyToolButtonClicked)

    def brushToolButtonAnimFinished(self):
        self.brushToolButton.clicked.connect(self.brushToolButtonClicked)
