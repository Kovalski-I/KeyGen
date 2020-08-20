'''
This class implements graphics scene of graphics view on the main window
where all colored service cards are placed in.

'''

# 3rd party imports
from PyQt5.QtWidgets import QGraphicsScene, QLabel

# python imports
import base64

# local imports
from widgets.serviceSticker import ServiceSticker

class GraphicsScene(QGraphicsScene):
    def __init__(self, parent):
        super().__init__()
        
        self._parent = parent

        # label which is shown when there are no cards on the scene
        self.noCardsTextProxy = None

    def addItem(self, item):
        # performing animation before item is added to the scene
        item.getWidget().doOpacityAnimation()
        super().addItem(item)

    def fill_with_cards(self):
        mainWindow = self.parent()
        scene = mainWindow.scene()
        json_data = mainWindow.json()

        scene.clear()

        counter = 0
        for id, data in reversed(json_data['id'].items()):
            card = ServiceSticker(
                id = id, pos = counter,
                name = data['name'],
                login = data['login'],
                color = data['color'],
                password = base64.b64decode(data['password'].encode()).decode(),
                mainWindow = mainWindow
            )
            scene.addItem(card)
            counter += 1

        if counter == 0:
            label = QLabel(
                'There are no cards\n' + 'Click "+" to add service card'
            )
            label.setStyleSheet(
                '''
                QLabel{
                    font-family: Quicksand;
                    background-color: #212121;
                    font-size: 36px;
                    color: #fafafa;
                }
                '''
            )
            self.noCardsTextProxy = self.addWidget(label)

        scene.update()

    def parent(self):
        return self._parent
