# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_question.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractScrollArea, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(732, 581)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(732, 581))
        Form.setBaseSize(QSize(732, 581))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 18, -1, -1)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(91, 23))
        self.groupBox.setBaseSize(QSize(91, 23))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setFamilies([u"C059"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"color: rgb(0, 0, 0);\n"
"font: 13pt \"C059\";\n"
"")
        self.plainTextEdit.setBackgroundVisible(False)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(91, 31))

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(91, 31))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(91, 31))

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(287, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.verticalSpacer = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(352, 538))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 336, 536))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \n"
"\u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432", None))
    # retranslateUi

