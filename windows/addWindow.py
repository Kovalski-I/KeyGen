# 3rd party imports
from PyQt5.QtWidgets import QDialog, QGraphicsScene
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import uic

# python imports
import os

# local imports
import resources
import glob

class AddWindow(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        uic.loadUi(os.getcwd() + "\\ui\\addWindow.ui", self)

        self.setWindowTitle('Adding Service Card')
        self.setModal(True)
        self.lengthSliderValueChanged()

        # creating animations
        self.caseToolButtonAnim = QPropertyAnimation(self.caseToolButton, b'geometry')
        self.keyToolButtonAnim = QPropertyAnimation(self.keyToolButton, b'geometry')

        # assigning event handlers
        self.caseToolButton.clicked.connect(self.caseToolButtonClicked)
        self.keyToolButton.clicked.connect(self.keyToolButtonClicked)
        self.lengthSlider.valueChanged.connect(self.lengthSliderValueChanged)
        self.caseToolButtonAnim.finished.connect(self.caseToolButtonAnimFinished)
        self.keyToolButtonAnim.finished.connect(self.keyToolButtonAnimFinished)

    def caseToolButtonClicked(self):
        glob.doAnimation(self.caseToolButtonAnim, self.caseToolButton, 4)

    def keyToolButtonClicked(self):
        glob.doAnimation(self.keyToolButtonAnim, self.keyToolButton, 4)

    ''' The method sets value text to the QLabel next the slider '''
    def lengthSliderValueChanged(self):
        value = str(self.lengthSlider.value())
        if len(value) == 1:
            self.lengthLabel.setText(value + '   ') # 3 spaces
        else:
            self.lengthLabel.setText(value + ' ') # 1 space

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
