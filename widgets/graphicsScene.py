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

        self._serviceCards = []
        self.noCardsTextProxy = None

    def update(self):
        self._serviceCards = []
        for item in self.items():
            if item.__class__.__name__ == 'ServiceSticker':
                self._serviceCards.append(item)

        if len(self.serviceCards()) != 0:
            self.removeItem(self.noCardsTextProxy)
        else:
            label = QLabel(
                'There are no cards\n' + 'Click "+" to add service card'
            )
            label.setStyleSheet(self.labelStyleSheet)
            self.noCardsTextProxy = self.addWidget(label)

        super().update()

    def delete(self, index):
        for card in self.serviceCards():
            if card.data()['index'] == index:
                self.removeItem(card)

    def serviceCards(self):
        return self._serviceCards
