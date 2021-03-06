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
from globalf import Glob
import resources

# ui
from ui.serviceCardWidget import Ui_Form

class ServiceCardWidget(QWidget, Ui_Form):
    def __init__(self, serviceName, login, color, parent):
        super().__init__()

        self.setupUi(self)

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
        Glob.doAnimation(self.editToolButtonAnim, self.editToolButton, 4)

        # showing addWindow but with the contents of service card
        stickerData = self.parent().data()

        mainWindow = self.parent().mainWindow()

        self.changeWindow = AddWindow(
            parent = mainWindow, edit = True, card = self.parent()
        )
        self.changeWindow.serviceEdit.setText(
            stickerData['name']
        )
        self.changeWindow.loginEdit.setText(
            stickerData['login']
        )
        self.changeWindow.passwordEdit.setText(
            stickerData['password']
        )

        self.changeWindow.show()

    def copyToolButtonClicked(self):
        Glob.doAnimation(self.copyToolButtonAnim, self.copyToolButton, 4)

        # putting password to exchange buffer
        QApplication.clipboard().setText(
            self.parent().data()['password']
        )

    def deleteToolButtonClicked(self):
        Glob.doAnimation(self.deleteToolButtonAnim, self.deleteToolButton, 4)
        self.doOpacityAnimation()

        mainWindow = self.parent().mainWindow()
        scene = mainWindow.scene()

        item_data = self.parent().data()
        json_data = mainWindow.json()

        json_data['id'].pop(item_data['id'])

        self.opacityAnimation.finished.connect(
            lambda: scene.fill_with_cards()
        )

        mainWindow.saveData()

    def parent(self):
        return self._parent
