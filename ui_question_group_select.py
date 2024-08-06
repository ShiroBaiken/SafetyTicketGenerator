# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question_group_select.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout,
                               QLabel, QPushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QSize(400, 300))
        Form.setBaseSize(QSize(400, 300))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(31)
        self.formLayout.setContentsMargins(-1, 10, -1, 7)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 0))
        self.comboBox.setMaximumSize(QSize(360, 16777215))
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.comboBox.setFont(font)
        self.comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.comboBox)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(300, 0))
        self.comboBox_2.setMaximumSize(QSize(360, 16777215))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.comboBox_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.pushButton)


        self.horizontalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

