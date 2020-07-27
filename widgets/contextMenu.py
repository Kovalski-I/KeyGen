'''
This class implements context menu which appears when the crown button
on the main window is clicked.

'''

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
        self._importJson = self.addAction('Import json')

        self.insertSeparator(self._importJson)

        self._actions = {
            id(self._changeMasterPassword): self.changeMasterPassword,
            id(self._importJson): self.importJson,

            # do nothing if context menu is closed
            # with no action selected
            id(None): lambda: None
        }

    def executeAction(self, action):
        self.actions()[id(action)]()

    def changeMasterPassword(self):
        setPasswordWindow = SetWindow(
            parent = self.parent(), closable = True
        )
        setPasswordWindow.show()

    def importJson(self):
        file_name = QFileDialog.getOpenFileName(
            self.parent(), 'Open json', os.getcwd(), 'Json files (*.json)'
        )

        # if file dialog is closed with no file selected
        if file_name[1] == '':
            return

        try:
            self.readJson(file_name[0], self.parent())
        except:
            messageBox = MessageBox(parent = self.parent())
            messageBox.messageText.setText('Wrong json provided')
            messageBox.show()

            self.parent().scene().update()

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
            mainWindow.json_data = json_data
        except FileNotFoundError:
            pass

        # creating cards from provided .json and adding them to the scene
        for service_name, data in json_data['serviceCards'].items():
            serviceSticker = ServiceSticker(
                service_name, data['login'], index = data['index'],
                password = data['password'], color = data['color'],
                parent = mainWindow
            )
            scene.addItem(serviceSticker)

        scene.update()
