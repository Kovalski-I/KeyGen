# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serviceCardWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 157)
        Form.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.serviceLabel = QtWidgets.QLabel(Form)
        self.serviceLabel.setStyleSheet("QLabel{\n"
"    font-family: Quicksand;\n"
"    font-size:  32px;\n"
"    color: #fafafa;\n"
"}")
        self.serviceLabel.setObjectName("serviceLabel")
        self.horizontalLayout.addWidget(self.serviceLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 14)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.loginLabel = QtWidgets.QLabel(Form)
        self.loginLabel.setStyleSheet("QLabel{\n"
"    font-family: Quicksand;\n"
"    font-size:  14px;\n"
"    color: #fafafa;\n"
"}")
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout_2.addWidget(self.loginLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(22, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editToolButton = QtWidgets.QToolButton(Form)
        self.editToolButton.setStyleSheet("QToolButton{\n"
"    background-image: url(:/icons/edit_icon.png);\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}")
        self.editToolButton.setText("")
        self.editToolButton.setObjectName("editToolButton")
        self.horizontalLayout_3.addWidget(self.editToolButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.copyToolButton = QtWidgets.QToolButton(Form)
        self.copyToolButton.setStyleSheet("QToolButton{\n"
"    background-image: url(:/icons/copy_icon.png);\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}")
        self.copyToolButton.setText("")
        self.copyToolButton.setObjectName("copyToolButton")
        self.horizontalLayout_3.addWidget(self.copyToolButton)
        self.deleteToolButton = QtWidgets.QToolButton(Form)
        self.deleteToolButton.setStyleSheet("QToolButton{\n"
"    background-image: url(:/icons/delete_icon.png);\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}")
        self.deleteToolButton.setText("")
        self.deleteToolButton.setObjectName("deleteToolButton")
        self.horizontalLayout_3.addWidget(self.deleteToolButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_4.setStretch(0, 14)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.serviceLabel.setText(_translate("Form", "None"))
        self.loginLabel.setText(_translate("Form", "None"))
        self.editToolButton.setToolTip(_translate("Form", "Edit Card"))
        self.copyToolButton.setToolTip(_translate("Form", "Copy Password"))
        self.deleteToolButton.setToolTip(_translate("Form", "Delete Card"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
