# 3rd party imports
from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtCore import QPropertyAnimation, QRectF, QPointF, QPoint, Qt
from PyQt5.QtGui import QPainter
from PyQt5 import uic

# python imports
import base64
import json
import re
import os

# local imports
from widgets.contextMenu import ContextMenu
from widgets.graphicsScene import GraphicsScene
from widgets.serviceSticker import ServiceSticker
from widgets.messageBox import MessageBox
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

        self._scene = GraphicsScene(parent = self)
        self.contextMenu = ContextMenu(parent = self)
        self.json_data = None
        self.session_approved = False

        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setScene(self._scene)
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

        try:
            self.json_data = json.loads(open('keygen.json', 'rt').read())
            self.readJson()
        except:
            messageBox = MessageBox(parent = self, closable = False)
            messageBox.messageText.setText(
                'Cannot load keygen.json\nbecause it is corrupted'
            )
            messageBox.show()
            self.scene().update()

    def readJson(self):
        for service_name, data in self.json_data['serviceCards'].items():
            serviceSticker = ServiceSticker(
                service_name, data['login'], index = data['index'],
                password = base64.b64decode(
                    data['password'].encode()
                ).decode(),
                color = data['color'],
                parent = self
            )
            self.scene().addItem(serviceSticker)

        if self.json_data['firstOpen']:
            setPasswordWindow = SetWindow(parent = self)
            setPasswordWindow.show()
        else:
            if not self.session_approved:
                masterPasswordWindow = MasterPasswordWindow(parent = self)
                masterPasswordWindow.show()
                self.session_approved = True

        # updating keygen.json
        buffer = open('keygen.json', 'wt')
        buffer.write(json.dumps(self.json_data, sort_keys = False, indent = 4))
        buffer.close()

        self.scene().update()

    def addServiceCard(self, name, login, index, color, password):
        scene = self.scene()
        serviceCard = ServiceSticker(
            name, login,
            index = index,
            password = password,
            color = color,
            parent = self
        )
        scene.addItem(serviceCard)
        self.json_data['serviceCards'][name] = {
            'index': index,
            'login': login,
            'color': color,
            'password': base64.b64encode(password.encode()).decode()
        }

        scene.update()

    def paintEvent(self, ev):
        self.writeToGlobal(QRectF(self.graphicsView.geometry()))
        self.setSceneRectangle()

    def setSceneRectangle(self):
        viewWidth = self.graphicsView.width()
        viewHeight = self.graphicsView.height()
        boundingRectHeight = self.scene().itemsBoundingRect().height()
        sceneWidth = viewWidth

        if boundingRectHeight > viewHeight:
            sceneHeight = boundingRectHeight
        else:
            sceneHeight = viewHeight

        self.scene().setSceneRect(
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

        req = self.searchBar.text().strip().lower()
        scene = self.scene()

        self.scene().clear()

        if req == '':
            self.readJson()
            return

        counter = 0
        for card in scene.serviceCards():
            data = card.data()

            if re.match(req, data['serviceName'].lower()) is not None:
                newCard = ServiceSticker(
                    data['serviceName'], data['login'],
                    color = data['color'], password = data['password'],
                    index = counter, parent = self
                )
                scene.addItem(newCard)
                scene.update()
                counter += 1

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

    def saveData(self):
        self.json_data = json.loads(open('keygen.json', 'rt').read())
        self.json_data['serviceCards'] = {}

        for card in reversed(self.scene().serviceCards()):
            cardData = card.data()

            serviceName = cardData['serviceName']
            index = cardData['index']
            login = cardData['login']
            color = cardData['color']
            password = cardData['password']

            self.json_data['serviceCards'][serviceName] = {
                'index': index,
                'login': login,
                'color': color,
                'password': base64.b64encode(password.encode()).decode()
            }

        stream = open('keygen.json', 'wt')
        stream.write(json.dumps(self.json_data, sort_keys = False, indent = 4))
        stream.close()

    def closeEvent(self, ev):
        self.saveData()

    def scene(self):
        return self._scene

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
