# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtWidgets import (QGridLayout, QLineEdit, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QWidget)

class Ui_OptionsForm(object):
    def setupUi(self, OptionsForm):
        if not OptionsForm.objectName():
            OptionsForm.setObjectName(u"OptionsForm")
        OptionsForm.resize(400, 320)
        OptionsForm.setMinimumSize(QSize(400, 320))
        self.gridLayout_2 = QGridLayout(OptionsForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(OptionsForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 222, 269))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(OptionsForm)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.removeUser = QPushButton(OptionsForm)
        self.removeUser.setObjectName(u"removeUser")

        self.gridLayout.addWidget(self.removeUser, 5, 0, 1, 1)

        self.addUser = QPushButton(OptionsForm)
        self.addUser.setObjectName(u"addUser")

        self.gridLayout.addWidget(self.addUser, 4, 0, 1, 1)

        self.addPosition = QPushButton(OptionsForm)
        self.addPosition.setObjectName(u"addPosition")

        self.gridLayout.addWidget(self.addPosition, 0, 0, 1, 1)

        self.removePosition = QPushButton(OptionsForm)
        self.removePosition.setObjectName(u"removePosition")

        self.gridLayout.addWidget(self.removePosition, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)


        self.retranslateUi(OptionsForm)

        QMetaObject.connectSlotsByName(OptionsForm)
    # setupUi

    def retranslateUi(self, OptionsForm):
        OptionsForm.setWindowTitle(QCoreApplication.translate("OptionsForm", u"Form", None))
        self.removeUser.setText(QCoreApplication.translate("OptionsForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.addUser.setText(QCoreApplication.translate("OptionsForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.addPosition.setText(QCoreApplication.translate("OptionsForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.removePosition.setText(QCoreApplication.translate("OptionsForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

