'''
This class implements service card/sticker as a graphics item,
visuals of service card are implemented in ServiceCardWidget class.

'''

# 3rd party imports
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QLabel
from PyQt5.QtCore import QRectF, QPropertyAnimation

# python imports
import random
import math

# local imports
from widgets.serviceCardWidget import ServiceCardWidget

class ServiceSticker(QGraphicsItem):
    def __init__(self, name, login, pos, color, password, mainWindow, id):
        super().__init__()

        self._width = 270.0
        self._height = 157.0

        self._color = color
        self._pos = pos
        self._name = name
        self._login = login
        self._password = password
        self._mainWindow = mainWindow
        self._id = id

        self.widget = ServiceCardWidget(
            name, login, self._color, parent = self
        )
        self.proxyWidget = QGraphicsProxyWidget(self)
        self.proxyWidget.setWidget(self.widget)

        self.anim = QPropertyAnimation(self.proxyWidget, b'geometry')

    '''
    Method returns rectangle containing a position of the card
    on graphics scene.
    '''
    def boundingRect(self):

        # getting rect of graphics view on main window
        viewRect = QRectF(self.mainWindow().graphicsView.geometry())

        min_x_padding = 20.0

        # determining how much cards can it be in a row
        items_per_line, remainder = self.remainder_div(
            viewRect.width(), self._width + min_x_padding
        )

        x_padding = remainder / (items_per_line - 1)
        y_padding = 40.0

        # number of row
        y_counter = 0

        # item's position from top top left corner to bottom right corner
        # from left to right
        line_pos = self._pos + 1

        while True:
            if items_per_line - line_pos >= 0:
                x_counter = line_pos - 1
                break
            else:
                line_pos -= items_per_line
                y_counter += 1

        return QRectF(
            x_counter * (self._width + x_padding + min_x_padding),
            y_counter * (y_padding + self._height),
            self._width, self._height
        )

    '''
    This method sets position of a proxy widget
    '''
    def paint(self, painter, option, widget):
        self.proxyWidget.setPos(
            self.boundingRect().x(), self.boundingRect().y()
        )

    def data(self):
        return {
            'name': self._name,
            'id': self._id,
            'pos': self._pos,
            'login': self._login,
            'color': self._color,
            'password': self._password
        }

    def mainWindow(self):
        return self._mainWindow

    def width(self):
        return self._width

    def getWidget(self):
        return self.widget

    @staticmethod
    def remainder_div(a, b):
        return (math.floor(a / b), a % b)
