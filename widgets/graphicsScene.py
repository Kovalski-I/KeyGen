# 3rd party imports
from PyQt5.QtWidgets import QGraphicsScene, QLabel

class GraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.labelStyleSheet = '''QLabel{
               font-family: Quicksand;
               background-color: #212121;
               font-size: 36px;
               color: #fafafa;
           }'''

        self.serviceStickers = []

    def update(self):
        self.serviceStickers = []
        for item in self.items():
            if item.__class__.__name__ == 'ServiceSticker':
                self.serviceStickers.append(item)

        noCardsTextProxy = None
        if len(self.serviceStickers) != 0:
            self.removeItem(noCardsTextProxy)
        else:
            label = QLabel(
                'There are no cards\n' + 'Click \"+\" to add service card'
            )
            label.setStyleSheet(self.labelStyleSheet)
            noCardsTextProxy = self.addWidget(label)

        super().update()
