# 3rd party imports
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic

# python imports
import os

# local imports
import resources
import glob

class ServiceCardWidget(QWidget):
    def __init__(self, serviceName, login, color):
        super().__init__()
        uic.loadUi(os.getcwd() + '\\ui\\serviceCardWidget.ui', self)

        self.setStyleSheet(
            '''QWidget{
                background-color: ''' + '{0}'.format(color) + '''
            }'''
        )

        self.serviceLabel.setText(serviceName)
        self.loginLabel.setText(login)

        self.editToolButtonAnim = QPropertyAnimation(self.editToolButton, b'geometry')
        self.copyToolButtonAnim = QPropertyAnimation(self.copyToolButton, b'geometry')
        self.deleteToolButtonAnim = QPropertyAnimation(self.deleteToolButton, b'geometry')

        self.editToolButton.clicked.connect(self.editToolButtonClicked)
        self.copyToolButton.clicked.connect(self.copyToolButtonClicked)
        self.deleteToolButton.clicked.connect(self.deleteToolButtonClicked)

        self.editToolButtonAnim.finished.connect(
            lambda: self.editToolButton.clicked.connect(self.editToolButtonClicked)
        )
        self.copyToolButtonAnim.finished.connect(
            lambda: self.copyToolButton.clicked.connect(self.copyToolButtonClicked)
        )
        self.deleteToolButtonAnim.finished.connect(
            lambda: self.deleteToolButton.clicked.connect(self.deleteToolButtonClicked)
        )

    def editToolButtonClicked(self):
        glob.doAnimation(self.editToolButtonAnim, self.editToolButton, 4)

    def copyToolButtonClicked(self):
        glob.doAnimation(self.copyToolButtonAnim, self.copyToolButton, 4)

    def deleteToolButtonClicked(self):
        glob.doAnimation(self.deleteToolButtonAnim, self.deleteToolButton, 4)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication([])
    win = ServiceCardWidget('none', 'none')
    win.resize(240, 135)
    win.show()
    sys.exit(app.exec_())
