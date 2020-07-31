# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(664, 372)
        Dialog.setStyleSheet("")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.serviceEdit = QtWidgets.QLineEdit(Dialog)
        self.serviceEdit.setStyleSheet("QLineEdit {\n"
"    font-family: quicksand;\n"
"    font-size: 32px;\n"
"    border: none;\n"
"    color: #fafafa;\n"
"}")
        self.serviceEdit.setObjectName("serviceEdit")
        self.horizontalLayout_7.addWidget(self.serviceEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.brushToolButton = QtWidgets.QToolButton(Dialog)
        self.brushToolButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.brushToolButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.brushToolButton.setStyleSheet("QToolButton {\n"
"    background-image: url(:/icons/brush_icon.png);\n"
"    background-repeat: no repeat;\n"
"    border: none;\n"
"}")
        self.brushToolButton.setText("")
        self.brushToolButton.setIconSize(QtCore.QSize(20, 20))
        self.brushToolButton.setObjectName("brushToolButton")
        self.horizontalLayout_7.addWidget(self.brushToolButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginLabel = QtWidgets.QLabel(Dialog)
        self.loginLabel.setStyleSheet("QLabel {\n"
"    font-family: quicksand regular;\n"
"    font-size: 24px;\n"
"    color: #fafafa;\n"
"}")
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout_2.addWidget(self.loginLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.loginEdit = QtWidgets.QLineEdit(Dialog)
        self.loginEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    font-family: url(:/fonts/sourceSansPro.ttf);\n"
"    font-size: 20px;\n"
"}")
        self.loginEdit.setObjectName("loginEdit")
        self.verticalLayout.addWidget(self.loginEdit)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.caseToolButton = QtWidgets.QToolButton(Dialog)
        self.caseToolButton.setStyleSheet("QToolButton {\n"
"    background-image: url(:/icons/height_icon.png);\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}")
        self.caseToolButton.setText("")
        self.caseToolButton.setObjectName("caseToolButton")
        self.verticalLayout_2.addWidget(self.caseToolButton)
        self.verticalLayout_2.setStretch(0, 1222)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setStyleSheet("QLabel {\n"
"    font-family: quicksand regular;\n"
"    font-size: 24px;\n"
"    color: #fafafa;\n"
"}")
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_3.addWidget(self.passwordLabel)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.passwordEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    font-family: url(:/fonts/sourceSansPro.ttf);\n"
"    font-size: 20px;\n"
"}")
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout_3.addWidget(self.passwordEdit)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.keyToolButton = QtWidgets.QToolButton(Dialog)
        self.keyToolButton.setStyleSheet("QToolButton {\n"
"    background-image: url(:/icons/key_icon.png);\n"
"    background-repeat: no repeat;\n"
"    border: none;\n"
"}")
        self.keyToolButton.setText("")
        self.keyToolButton.setObjectName("keyToolButton")
        self.horizontalLayout_5.addWidget(self.keyToolButton)
        self.generatePasswordLabel = QtWidgets.QLabel(Dialog)
        self.generatePasswordLabel.setStyleSheet("QLabel {\n"
"    font-family: quicksand regular;\n"
"    font-size: 13px;\n"
"    color: #fafafa;\n"
"}")
        self.generatePasswordLabel.setObjectName("generatePasswordLabel")
        self.horizontalLayout_5.addWidget(self.generatePasswordLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_12.addLayout(self.verticalLayout_4)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 80)
        self.horizontalLayout_12.setStretch(2, 2)
        self.horizontalLayout_12.setStretch(3, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.numbersBox = QtWidgets.QCheckBox(Dialog)
        self.numbersBox.setStyleSheet("QCheckBox {\n"
"    font-family: source sans pro;\n"
"    font-size: 17px;\n"
"    color: #fafafa;\n"
"}\n"
"QChekcBox::indicator {\n"
"    border: none;\n"
"}")
        self.numbersBox.setChecked(True)
        self.numbersBox.setObjectName("numbersBox")
        self.horizontalLayout.addWidget(self.numbersBox)
        self.lettersBox = QtWidgets.QCheckBox(Dialog)
        self.lettersBox.setStyleSheet("QCheckBox {\n"
"    font-family: source sans pro;\n"
"    font-size: 17px;\n"
"    color: #fafafa;\n"
"}")
        self.lettersBox.setChecked(True)
        self.lettersBox.setObjectName("lettersBox")
        self.horizontalLayout.addWidget(self.lettersBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.lengthLabel = QtWidgets.QLabel(Dialog)
        self.lengthLabel.setStyleSheet("QLabel {    \n"
"    font-family: source sans pro;\n"
"    font-size: 17px;\n"
"    color: #fafafa;\n"
"}")
        self.lengthLabel.setText("")
        self.lengthLabel.setObjectName("lengthLabel")
        self.horizontalLayout_4.addWidget(self.lengthLabel)
        self.lengthSlider = QtWidgets.QSlider(Dialog)
        self.lengthSlider.setWhatsThis("")
        self.lengthSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lengthSlider.setMaximum(64)
        self.lengthSlider.setProperty("value", 8)
        self.lengthSlider.setTracking(True)
        self.lengthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lengthSlider.setInvertedAppearance(False)
        self.lengthSlider.setInvertedControls(False)
        self.lengthSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.lengthSlider.setTickInterval(10)
        self.lengthSlider.setObjectName("lengthSlider")
        self.horizontalLayout_4.addWidget(self.lengthSlider)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(3, 3)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem17)
        self.horizontalLayout_13.setStretch(0, 5)
        self.horizontalLayout_13.setStretch(1, 65)
        self.horizontalLayout_13.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem18)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout_5.setStretch(2, 2)
        self.verticalLayout_5.setStretch(3, 2)
        self.verticalLayout_5.setStretch(4, 2)
        self.verticalLayout_5.setStretch(5, 2)
        self.verticalLayout_5.setStretch(6, 2)
        self.verticalLayout_5.setStretch(7, 3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 20)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.serviceEdit.setPlaceholderText(_translate("Dialog", "Service"))
        self.brushToolButton.setToolTip(_translate("Dialog", "Change color"))
        self.loginLabel.setText(_translate("Dialog", "Login"))
        self.caseToolButton.setToolTip(_translate("Dialog", "Uppercase/Lowercase"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))
        self.generatePasswordLabel.setToolTip(_translate("Dialog", "Click on the icon to generate password"))
        self.generatePasswordLabel.setText(_translate("Dialog", "Generate Password"))
        self.numbersBox.setText(_translate("Dialog", "Numbers"))
        self.lettersBox.setText(_translate("Dialog", "Letters"))
        self.lengthSlider.setToolTip(_translate("Dialog", "set password length"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
