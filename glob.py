# 3rd party imports
from PyQt5.QtCore import QRectF

# python imports
import math

tempList = [QRectF(0, 0, 816, 409)]

''' This method does animation for the object which has QPropertyAnimation '''
def doAnimation(animation, widget, square_ratio):
    end_size = []
    size = [widget.geometry().width(), widget.geometry().height()]
    for value in size:
        end_size.append(value / math.sqrt(square_ratio))

    end_x = widget.geometry().x() + ((size[0] - end_size[0]) / 2)
    end_y = widget.geometry().y() + ((size[1] - end_size[1]) / 2)

    animation.setStartValue(widget.geometry())
    animation.setEndValue(widget.geometry())
    animation.setKeyValueAt(0.5, QRectF(end_x, end_y, end_size[0], end_size[1]))
    animation.setDuration(150)
    animation.start()

    widget.clicked.disconnect()
