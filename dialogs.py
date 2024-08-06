from PySide6.QtWidgets import QDialog

from ui_add_user_dialog import Ui_Form as Ui_Add_User
from ui_alert import Ui_Dialog as Ui_Alert
from ui_position_select import Ui_Dialog
from ui_question_no_dialog import Ui_Chose_question_No


class ChoseQNo(Ui_Chose_question_No, QDialog):
    def __init__(self):
        super(ChoseQNo, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)

    def add_data(self, max):
        self.comboBox.addItems([str(x) for x in range(1, max + 1)])

    def get_q_number(self):
        return self.comboBox.currentText()


class ChosePositionNo(Ui_Dialog, QDialog):
    def __init__(self):
        super(ChosePositionNo, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)

    def get_q(self):
        return self.comboBox.currentText()


class AddUser(Ui_Add_User, QDialog):
    def __init__(self):
        super(AddUser, self).__init__()
        self.setupUi(self)
        self.buttonBox.buttons()[0].clicked.connect(self.accept)
        self.buttonBox.buttons()[1].clicked.connect(self.close)

    def return_data(self):
        return self.lineEdit.text(), self.lineEdit_2.text()


class Alert(Ui_Alert, QDialog):
    def __init__(self):
        super(Alert, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)