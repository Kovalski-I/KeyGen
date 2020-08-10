'''
This class implements graphics scene of graphics view on the main window
where all colored service cards are placed in.

'''

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

        # list which all service cards on the scene are added to
        self._serviceCards = []

        self._parent = parent

        # label which is shown when there are no cards on the scene
        self.noCardsTextProxy = None

    def addItem(self, item):
        # performing animation before item is added to the scene
        item.getWidget().doOpacityAnimation()
        super().addItem(item)

    '''
    This method determines if there are cards on the scene: updates
    serviceCards list or shows no cards label.
    '''
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

    '''
    The method deletes service card with given index from the
    scene, creates remaining cards assigning them new indexes and adds
    them to the scene.
    '''
    def delete(self, index):
        serviceCards = self.parent().json()['number']

        for number, data in serviceCards.items():
            if data['index'] == index:
                serviceCards.pop(number)
                break

        self.serviceCards().clear()
        self.clear()

        counter = 0
        json_data = self.parent().json()
        for number, data in serviceCards.items():
            newCard = ServiceSticker(
                data['serviceName'], data['login'],
                color = data['color'], password = data['password'],
                index = counter, parent = self.parent(),
                number = number
            )

            json_data['number'][number] = {
                'serviceName': data['serviceName'],
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
