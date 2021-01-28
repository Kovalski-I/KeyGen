'''
This class implements a main window of the app.
The instance of this class is a parent to almost all other objects.

'''


# 3rd party imports
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPropertyAnimation, QRectF, QPoint, Qt

# python imports
import base64
import json
import re

# local imports
from widgets.contextMenu import ContextMenu
from widgets.graphicsScene import GraphicsScene
from widgets.serviceSticker import ServiceSticker
from widgets.messageBox import MessageBox
from windows.addWindow import AddWindow
from windows.setWindow import SetWindow
from windows.masterPassword import MasterPasswordWindow
from globalf import Glob

# ui
from ui.mainWindow import Ui_mainWindow

class MainWindow(QWidget, Ui_mainWindow):
    def __init__(self):
        super().__init__()

        # loading window ui
        self.setupUi(self)

        self.setMinimumSize(790, 410)

        PREFIX = '   '  # 3 SPACES

        self.searchBar.setText(PREFIX)

        # creating animations
        self.crownToolButtonAnim = QPropertyAnimation(
            self.crownToolButton, b'geometry'
        )
        self.plusToolButtonAnim = QPropertyAnimation(
            self.plusToolButton, b'geometry'
        )

        self._scene = GraphicsScene(parent=self)
        self.contextMenu = ContextMenu(parent=self)
        self.json_data = None
        self.json_is_read = False

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

        # reading json and displaying error if failed
        try:
            self.json_data = json.loads(open('keygen.json', 'rt').read())
        except:
            messageBox = MessageBox(parent=self, closable=False)
            messageBox.messageText.setText(
                'Cannot load keygen.json'
            )
            messageBox.show()

            # not trying to access json data anymore
            self.json_is_read = True

    def readJson(self):
        scene = self.scene()

        # creating cards from data of json
        scene.fill_with_cards()

        if self.json_data['firstOpen']:
            setPasswordWindow = SetWindow(parent=self)
            setPasswordWindow.show()
        else:
            masterPasswordWindow = MasterPasswordWindow(parent=self)
            masterPasswordWindow.show()

    def showEvent(self, ev):
        if not self.json_is_read:
            self.readJson()
            self.json_is_read = True
        else:
            ev.accept()

    def paintEvent(self, ev):
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
            self.scene().fill_with_cards()
            return

        counter = 0
        for unigue_id, data in reversed(self.json_data['id'].items()):
            if re.match(req, data['name'].lower()) is not None:
                newCard = ServiceSticker(
                    data['name'], data['login'],
                    color=data['color'],
                    password=base64.b64decode(
                        data['password'].encode()
                    ).decode(),
                    pos=counter, mainWindow=self,
                    id=unigue_id
                )
                scene.addItem(newCard)
                counter += 1

    def crownToolButtonClicked(self):
        Glob.doAnimation(self.crownToolButtonAnim, self.crownToolButton, 3)

        chosen_action = self.contextMenu.exec_(self.calculateCoordinates())
        self.contextMenu.executeAction(chosen_action)

    def plusToolButtonClicked(self):
        Glob.doAnimation(self.plusToolButtonAnim, self.plusToolButton, 3)

        addWindow = AddWindow(parent = self)
        addWindow.show()

    '''
    This method leaves prefix in self.searchBar QLineEdit.
    '''
    def leavePrefix(self, prefix):
        if len(self.searchBar.text()) < 3:
            self.searchBar.setText(prefix)

    '''
    This method returns a top left point of a context menu appeared
    when crown toolbutton's clicked.
    '''
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
        stream = open('keygen.json', 'wt')
        stream.write(json.dumps(self.json_data, sort_keys = False, indent = 4))
        stream.close()

    def scene(self):
        return self._scene

    def json(self):
        return self.json_data
