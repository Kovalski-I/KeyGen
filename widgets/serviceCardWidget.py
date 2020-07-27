'''
This class implements widget which is assigned to ServiceSticker
as a proxy widget.

'''


# 3rd party imports
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import uic

# python imports
import os

# local imports
from windows.addWindow import AddWindow
import resources
import glob

class ServiceCardWidget(QWidget):
    def __init__(self, serviceName, login, color, parent):
        super().__init__()

        uic.loadUi(os.getcwd() + '\\ui\\serviceCardWidget.ui', self)

        self.setMinimumSize(210, 135)
        self.setMaximumSize(350, 200)
        self.setStyleSheet(
            '''QWidget{
                background-color: ''' + '{0}'.format(color) + ''';
            }'''
        )
        self.setWindowOpacity(0.0)

        self._parent = parent

        self.serviceLabel.setText(serviceName)
        self.loginLabel.setText(login)

        self.opacityAnimation = QPropertyAnimation(self, b'windowOpacity')

        self.editToolButtonAnim = QPropertyAnimation(
            self.editToolButton, b'geometry'
        )
        self.copyToolButtonAnim = QPropertyAnimation(
            self.copyToolButton, b'geometry'
        )
        self.deleteToolButtonAnim = QPropertyAnimation(
            self.deleteToolButton, b'geometry'
        )

        self.editToolButton.clicked.connect(self.editToolButtonClicked)
        self.copyToolButton.clicked.connect(self.copyToolButtonClicked)
        self.deleteToolButton.clicked.connect(self.deleteToolButtonClicked)

        self.editToolButtonAnim.finished.connect(
            lambda: self.editToolButton.clicked.connect(
                self.editToolButtonClicked
            )
        )
        self.copyToolButtonAnim.finished.connect(
            lambda: self.copyToolButton.clicked.connect(
                self.copyToolButtonClicked
            )
        )
        self.deleteToolButtonAnim.finished.connect(
            lambda: self.deleteToolButton.clicked.connect(
                self.deleteToolButtonClicked
            )
        )

    '''
    Method determines whether to perform fade or appear animation.
    '''
    def doOpacityAnimation(self):
        if self.windowOpacity() == 1.0:
            startValue = 1.0
            endValue = 0.0
        else:
            startValue = 0.0
            endValue = 1.0
        self.opacityAnimation.setStartValue(startValue)
        self.opacityAnimation.setEndValue(endValue)
        self.opacityAnimation.setDuration(200)
        self.opacityAnimation.start()

    def editToolButtonClicked(self):
        glob.doAnimation(self.editToolButtonAnim, self.editToolButton, 4)

        # showing addWindow but with the contents of service card
        stickerData = self.parent().data()

        mainWindow = self.parent().parent()

        self.changeWindow = AddWindow(
            parent = mainWindow, edit = True, card = self.parent()
        )
        self.changeWindow.serviceEdit.setText(
            stickerData['serviceName']
        )
        self.changeWindow.loginEdit.setText(
            stickerData['login']
        )
        self.changeWindow.passwordEdit.setText(
            stickerData['password']
        )

        self.changeWindow.show()

    def copyToolButtonClicked(self):
        glob.doAnimation(self.copyToolButtonAnim, self.copyToolButton, 4)

        # putting password to exchange buffer
        QApplication.clipboard().setText(
            self.parent().data()['password']
        )

    def deleteToolButtonClicked(self):
        glob.doAnimation(self.deleteToolButtonAnim, self.deleteToolButton, 4)
        self.doOpacityAnimation()

        # calling delete() of GraphicsScene when animation's finished
        self.opacityAnimation.finished.connect(
            lambda: self.parent().scene().delete(
                self.parent().data()['index']
            )
        )

    def parent(self):
        return self._parent
