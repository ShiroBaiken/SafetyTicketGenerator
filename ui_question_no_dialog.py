# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question_no_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QGridLayout,
                               QLabel, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)

class Ui_Chose_question_No(object):
    def setupUi(self, Chose_question_No):
        if not Chose_question_No.objectName():
            Chose_question_No.setObjectName(u"Chose_question_No")
        Chose_question_No.resize(264, 144)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Chose_question_No.sizePolicy().hasHeightForWidth())
        Chose_question_No.setSizePolicy(sizePolicy)
        Chose_question_No.setMinimumSize(QSize(264, 144))
        Chose_question_No.setMaximumSize(QSize(264, 144))
        self.widget = QWidget(Chose_question_No)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 40, 154, 83))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Chose_question_No)

        QMetaObject.connectSlotsByName(Chose_question_No)
    # setupUi

    def retranslateUi(self, Chose_question_No):
        Chose_question_No.setWindowTitle(QCoreApplication.translate("Chose_question_No", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Chose_question_No", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Chose_question_No", u"OK", None))
    # retranslateUi

