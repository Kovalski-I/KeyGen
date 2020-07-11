# 3rd party imports
from PyQt5.QtWidgets import QGraphicsScene

class GraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.positioning = dict()

    def update(self):
        super().update()

        # for i in range(1, len(self.items()), 2):
        #     currentItem = self.items()[i]
        #     currentItem.setIndex(
        #         self.module(currentItem.index() - len(self.items()))
        #     )
