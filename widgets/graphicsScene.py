# 3rd party imports
from PyQt5.QtWidgets import QGraphicsScene, QLabel

class GraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.noCardsText = QLabel(
            'There are no cards\n' + 'Click \"+\" to add service card'
        )
        self.noCardsText.setStyleSheet(
            '''QLabel{
                   font-family: Quicksand;
                   background-color: #212121;
                   font-size: 36px;
	               color: #fafafa;
               }'''
        )

    def update(self):
        noCardsTextProxy = None

        if len(self.items()) == 0:
            noCardsTextProxy = self.addWidget(self.noCardsText)
            noCardsTextProxy.setPos(0, 0)
        else:
            self.removeItem(noCardsTextProxy)

        super().update()
