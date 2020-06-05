# 3rd party imports
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QLabel
from PyQt5.QtCore import QRectF, QPropertyAnimation

# python imports
import random

# local imports
from widgets.serviceCardWidget import ServiceCardWidget
import glob

class ServiceSticker(QGraphicsItem):
    def __init__(self, serviceName, login, index = 0):
        super().__init__()

        self._width = 270.0
        self._height = 157.0
        self._color = random.choice(['#244f26', '#875307', '#01434b'])
        self._index = index

        self.widget = ServiceCardWidget(serviceName, login, self._color)
        self.proxyWidget = QGraphicsProxyWidget(self)
        self.anim = QPropertyAnimation(self.proxyWidget, b'geometry')
        self.proxyWidget.setWidget(self.widget)

    def boundingRect(self):
        viewRect = glob.tempList[0]
        min_x_padding = 20

        items_per_line, remainder = self.remainder_div(viewRect.width(), self._width)
        try:
            x_padding = remainder / (items_per_line - 1) + min_x_padding
        except ZeroDivisionError:
            x_padding = 0
        y_padding = 40

        line_pos = self._index + 1
        y_counter = 0
        while True:
            if items_per_line - line_pos >= 0:
                x_counter = line_pos - 1
                break
            else:
                line_pos -= items_per_line
                y_counter += 1

        return QRectF(
                   x_counter * (self._width + x_padding),
                   y_counter * (y_padding + self._height),
                   self._width, self._height
               )

    @staticmethod
    def remainder_div(a, b):
        return (int(a / b), a % b)

    def paint(self, painter, option, widget):
        self.proxyWidget.setPos(
            self.boundingRect().x(), self.boundingRect().y()
        )
