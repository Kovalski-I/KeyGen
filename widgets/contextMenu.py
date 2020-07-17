# 3rd party imports
from PyQt5.QtWidgets import QMenu, QFileDialog

# pyton imports
import json
import os

# local imports
from windows.setWindow import SetWindow
from widgets.messageBox import MessageBox
from widgets.serviceSticker import ServiceSticker
import glob

class ContextMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self._changeMasterPassword = self.addAction(
            'Change master password'
        )
        # self._changeServiceCardsSize = self.addAction(
        #     'Change service cards\' size'
        # )
        self._importJson = self.addAction('Import json')

        self.insertSeparator(self._importJson)

        self._actions = {
            id(self._changeMasterPassword): self.changeMasterPassword,
            # id(self._changeServiceCardsSize): self.changeServiceCardsSize,
            id(self._importJson): self.importJson,
            id(None): lambda: None
        }

        self.chosenSize = None

    def executeAction(self, action):
        self.actions()[id(action)]()

    def changeMasterPassword(self):
        setPasswordWindow = SetWindow(
            parent = self.parent(), closable = True
        )
        setPasswordWindow.show()

    # def changeServiceCardsSize(self):
    #     serviceCardWidget = ServiceCardWidget(
    #         'Editing Size', 'Close this window if ready', color = 'gray',
    #         parent = self
    #     )
    #     serviceCardWidget.show()
    #
    #     chosenSize = self.chosenSize
    #     print(chosenSize)
    #     mainWindow = self.parent()

    def importJson(self):
        file_name = QFileDialog.getOpenFileName(
            self.parent(), 'Open json', os.getcwd(), 'Json files (*.json)'
        )

        self.readJson(file_name[0], self.parent())
        # try:
        #     self.readJson(file_name[0], self.parent())
        # except:
        #     messageBox = MessageBox(parent = self.parent())
        #     messageBox.messageText.setText('Wrong json provided')
        #     messageBox.show()
        #
        #     self.parent().scene().update()

    def actions(self):
        return self._actions

    @staticmethod
    def readJson(filename, mainWindow):
        scene = mainWindow.scene()

        scene.clear()

        json_data = {}
        json_data['serviceCards'] = {}
        try:
            json_data = json.loads(open(filename, 'rt').read())
        except FileNotFoundError:
            pass

        for service_name, data in json_data['serviceCards'].items():
            serviceSticker = ServiceSticker(
                service_name, data['login'], index = data['index']
            )
            scene.addItem(serviceSticker)

        scene.update()
