# 3rd party imports
from PyQt5.QtWidgets import QGraphicsScene, QLabel

# local imports
from widgets.serviceSticker import ServiceSticker

class GraphicsScene(QGraphicsScene):
    def __init__(self, parent):
        super().__init__()

        self.labelStyleSheet = '''QLabel{
               font-family: Quicksand;
               background-color: #212121;
               font-size: 36px;
               color: #fafafa;
           }'''

        self._serviceCards = []
        self._parent = parent
        self.noCardsTextProxy = None

    def addItem(self, item):
        item.getWidget().doOpacityAnimation()
        super().addItem(item)

    def update(self):
        self._serviceCards = []
        for item in self.items():
            if item.__class__.__name__ == 'ServiceSticker':
                self.serviceCards().append(item)

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
        serviceCards = self.parent().json()['serviceCards']

        for name, data in serviceCards.items():
            if data['index'] == index:
                serviceCards.pop(name)
                break

        self.serviceCards().clear()
        self.clear()

        counter = 0
        json_data = self.parent().json()
        for name, data in serviceCards.items():
            newCard = ServiceSticker(
                name, data['login'],
                color = data['color'], password = data['password'],
                index = counter, parent = self.parent()
            )

            json_data['serviceCards'][name] = {
                'index': counter,
                'login': data['login'],
                'color': data['color'],
                'password': data['password']
            }
            self.addItem(newCard)

            counter += 1

        self.parent().saveData()
        self.update()

    def serviceCards(self):
        return self._serviceCards

    def parent(self):
        return self._parent
