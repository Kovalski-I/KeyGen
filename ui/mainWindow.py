# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1138, 672)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("QWidget#mainWindow{\n"
"    background-color: #212121;\n"
"}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(mainWindow)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.plusToolButton = QtWidgets.QToolButton(mainWindow)
        self.plusToolButton.setStyleSheet("QToolButton {\n"
"    background-image: url(:/icons/plus_icon.png);\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}\n"
"")
        self.plusToolButton.setText("")
        self.plusToolButton.setIconSize(QtCore.QSize(32, 32))
        self.plusToolButton.setCheckable(False)
        self.plusToolButton.setChecked(False)
        self.plusToolButton.setObjectName("plusToolButton")
        self.verticalLayout_5.addWidget(self.plusToolButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.crownToolButton = QtWidgets.QToolButton(mainWindow)
        self.crownToolButton.setStyleSheet("QToolButton {\n"
"    background-image: url(:/icons/settings_icon.png);\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}")
        self.crownToolButton.setText("")
        self.crownToolButton.setIconSize(QtCore.QSize(32, 32))
        self.crownToolButton.setObjectName("crownToolButton")
        self.verticalLayout_5.addWidget(self.crownToolButton)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_5.setStretch(0, 75)
        self.verticalLayout_5.setStretch(2, 10)
        self.verticalLayout_5.setStretch(5, 100)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keygenLabel = QtWidgets.QLabel(mainWindow)
        self.keygenLabel.setStyleSheet("QLabel {\n"
"    font-family: quicksand;\n"
"    font-size: 49pt;\n"
"    color: #fafafa;\n"
"}")
        self.keygenLabel.setObjectName("keygenLabel")
        self.horizontalLayout.addWidget(self.keygenLabel)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.searchBar = QtWidgets.QLineEdit(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 12px;\n"
"    font-size: 26px;\n"
"    font-family: SegoeUI;\n"
"    padding: 4px 4px 4px 10px;\n"
"    background-image: url(:/icons/search_icon.ico);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    background-origin: content;\n"
"}")
        self.searchBar.setInputMask("")
        self.searchBar.setText("")
        self.searchBar.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.searchBar.setCursorPosition(0)
        self.searchBar.setPlaceholderText("")
        self.searchBar.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.searchBar.setClearButtonEnabled(False)
        self.searchBar.setObjectName("searchBar")
        self.verticalLayout_3.addWidget(self.searchBar)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.graphicsView = QtWidgets.QGraphicsView(mainWindow)
        self.graphicsView.setStyleSheet("QGraphicsView {\n"
"    background-color: #212121;\n"
"    border: none;    \n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 27)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 30)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 70)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "KeyGen"))
        self.plusToolButton.setToolTip(_translate("mainWindow", "Add new service card"))
        self.plusToolButton.setWhatsThis(_translate("mainWindow", "Add new service"))
        self.crownToolButton.setToolTip(_translate("mainWindow", "Settings"))
        self.crownToolButton.setWhatsThis(_translate("mainWindow", "Settings"))
        self.keygenLabel.setText(_translate("mainWindow", "KeyGen"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
