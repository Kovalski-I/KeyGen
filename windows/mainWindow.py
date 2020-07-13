# 3rd party imports
from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtCore import QPropertyAnimation, QRectF, QPointF, QPoint, Qt
from PyQt5.QtGui import QPainter
from PyQt5 import uic

# python imports
import json
import os

# local imports
from widgets.contextMenu import ContextMenu
from widgets.graphicsScene import GraphicsScene
from widgets.serviceSticker import ServiceSticker
from windows.addWindow import AddWindow
from windows.setWindow import SetWindow
from windows.masterPassword import MasterPasswordWindow
import resources
import glob

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # loading window ui
        uic.loadUi(os.getcwd() + "\\ui\\mainWindow.ui", self)

        PREFIX = '   ' # 3 SPACES

        self.searchBar.setText(PREFIX)

        # creating animations
        self.crownToolButtonAnim = QPropertyAnimation(
            self.crownToolButton, b'geometry'
        )
        self.plusToolButtonAnim = QPropertyAnimation(
            self.plusToolButton, b'geometry'
        )

        self.scene = GraphicsScene()
        self.contextMenu = ContextMenu(parent = self)

        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.centerOn(0, 0)

        # assigning events handlers
        self.searchBar.textChanged.connect(
            lambda: self.searchBarTextChanged(PREFIX)
        )
        self.crownToolButton.clicked.connect(self.crownToolButtonClicked)
        self.plusToolButton.clicked.connect(self.plusToolButtonClicked)
        self.crownToolButtonAnim.finished.connect(
            lambda: self.crownToolButton.clicked.connect(
                self.crownToolButtonClicked
            )
        )
        self.plusToolButtonAnim.finished.connect(
            lambda: self.plusToolButton.clicked.connect(
                self.plusToolButtonClicked
            )
        )

        self.readJson()

    def readJson(self):
        json_data = json.loads(open('keygen.json', 'rt').read())

        for service_name, data in json_data['serviceCards'].items():
            serviceSticker = ServiceSticker(
                service_name, data['login'], index = data['index']
            )
            self.scene.addItem(serviceSticker)

        if json_data['firstOpen']:
            setPasswordWindow = SetWindow(parent = self)
            setPasswordWindow.show()

            json_data['firstOpen'] = False
        else:
            masterPasswordWindow = MasterPasswordWindow(parent = self)
            masterPasswordWindow.show()

        # updating keygen.json
        buffer = open('keygen.json', 'wt')
        buffer.write(json.dumps(json_data, sort_keys = False, indent = 2))
        buffer.close()

        self.scene.update()

    def paintEvent(self, ev):
        self.writeToGlobal(QRectF(self.graphicsView.geometry()))
        self.setSceneRectangle()

    def setSceneRectangle(self):
        viewWidth = self.graphicsView.width()
        viewHeight = self.graphicsView.height()
        boundingRectHeight = self.scene.itemsBoundingRect().height()
        sceneWidth = viewWidth

        if boundingRectHeight > viewHeight:
            sceneHeight = boundingRectHeight
        else:
            sceneHeight = viewHeight

        self.scene.setSceneRect(
            QRectF(
                QPoint(),
                QPoint(
                    sceneWidth,
                    sceneHeight
                )
            )
        )

    def searchBarTextChanged(self, prefix):
        self.leavePrefix(prefix)

    def crownToolButtonClicked(self):
        glob.doAnimation(self.crownToolButtonAnim, self.crownToolButton, 3)

        chosen_action = self.contextMenu.exec_(self.calculateCoordinates())
        self.contextMenu.executeAction(chosen_action)

    def plusToolButtonClicked(self):
        glob.doAnimation(self.plusToolButtonAnim, self.plusToolButton, 3)

        addWindow = AddWindow(parent = self)
        addWindow.show()

    ''' This method leaves prefix in self.searchBar QLineEdit '''
    def leavePrefix(self, prefix):
        if len(self.searchBar.text()) < 3:
            self.searchBar.setText(prefix)

    def calculateCoordinates(self):
        coordinates = [
            self.mapToGlobal(self.crownToolButton.pos()).x(),
            self.mapToGlobal(self.crownToolButton.pos()).y()
        ]
        final_coordinates = []
        for coordinate in coordinates:
            final_coordinates.append(coordinate + 25)

        return QPoint(
            final_coordinates[0], final_coordinates[1]
        )

    @staticmethod
    def writeToGlobal(data):
        glob.tempList[0] = data

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
