# 3rd party imports
from PyQt5.QtWidgets import QMenu

# local imports
import glob

class ContextMenu(QMenu):
    def __init__(self):
        super().__init__()

        actions = [self.addAction('Change Master Password'),
                  self.addAction('Import KeyGen Data'),
                  self.addAction('Export KeyGen Data')]

        self.insertSeparator(actions[1])
