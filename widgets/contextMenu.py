# 3rd party imports
from PyQt5.QtWidgets import QMenu

# local imports
import glob

class ContextMenu(QMenu):
    def __init__(self):
        super().__init__()

        self.actions = [
            self.addAction('Change master password'),
            self.addAction('Change service cards\' size'),
            self.addAction('Import json')
        ]

        self.insertSeparator(self.actions[2])
