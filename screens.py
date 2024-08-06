from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QDialog

from dialogs import ChoseQNo, ChosePositionNo, AddUser, Alert
from password_check import LoginManipulator
from test_manipulator import ListsGetter, QestionGetter, QuestionInserter, PositionsManipulator
from test_shuffler import TestShuffler
from ticket_doc_generator import TicketDocGenerator
from ui_add_question import Ui_Form as AddQuestionForm
from ui_generate_tickets import Ui_Form as GenerateTicketsForm
from ui_login2 import Ui_Form as LoginForm
from ui_main_menu import Ui_Form as MenuWidget
from ui_options import Ui_OptionsForm
from ui_question_group_select import Ui_Form as QuestionGroupSelectForm


class MainMenu(MenuWidget, QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setupUi(self)


class LoginScreen(LoginForm, QWidget):
    def __init__(self, client):
        super(LoginScreen, self).__init__()
        self.setupUi(self)
        self.client = client
        self.alert = None

    def button_cliked(self):
        login_manager = LoginManipulator(self.client)
        login, password = self.lineEdit.text(), self.lineEdit_2.text()
        if login != '' and password != '':
            check = login_manager.pass_check(login, password)
            if check is False:
                self.alert = Alert()
                if self.alert.exec() == QDialog.Accepted:
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()
            else:
                return True


class QuestionGroupSelectScreen(QuestionGroupSelectForm, QWidget):
    def __init__(self, client):
        super(QuestionGroupSelectScreen, self).__init__()
        self.setupUi(self)
        self.client = client
        self.add_values()

    def add_values(self):
        getter = ListsGetter(self.client)
        self.comboBox.addItems(getter.get_positions())
        getter.collection = 'categorises'
        self.comboBox_2.addItems(getter.get_keys())


class AddQuestionScreen(AddQuestionForm, QWidget):
    def __init__(self, client):
        super(AddQuestionScreen, self).__init__()
        self.setupUi(self)
        self.client = client
        self.group = None
        self.question_ind = None
        self.dialog = None
        self.pushButton.clicked.connect(self.save_button_clicked)
        self.pushButton_2.clicked.connect(self.plainTextEdit.clear)
        self.pushButton_3.clicked.connect(self.show_q_number_dialog)

    def add_values(self):
        getter = QestionGetter(self.client, self.group)
        questions = getter.retrieve_all()
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(5)
        for q in questions:
            text = QLabel(text=f"{q['question_id']}) {q['question']}")
            text.setMinimumHeight(50)
            text.setWordWrap(True)
            layout.addWidget(text)
        widget.setLayout(layout)
        self.scrollArea.setWidget(widget)

    def add_new_question(self):
        text = self.plainTextEdit.toPlainText()
        if text:
            getter = QestionGetter(self.client, self.group)
            no_of_questions = getter.get_range()
            label = QLabel(text=f"{no_of_questions + 1}) {text}")
            label.setMinimumHeight(50)
            label.setWordWrap(True)
            self.scrollArea.widget().layout().addWidget(label)
            inserter = QuestionInserter(self.client, self.group)
            inserter.add_new_question(text)
            self.plainTextEdit.clear()
            bar = self.scrollArea.verticalScrollBar()
            bar.rangeChanged.connect(lambda x, y: bar.setValue(9999))

    def show_existing_question(self):
        getter = QestionGetter(self.client, self.group)
        question_to_mod = getter.retrieve_one(self.question_ind)
        self.plainTextEdit.setPlainText(question_to_mod["question"])

    def show_q_number_dialog(self):
        getter = QestionGetter(self.client, self.group)
        max_r = getter.get_range()
        self.dialog = ChoseQNo()
        self.dialog.add_data(max_r)
        if self.dialog.exec() == QDialog.Accepted:
            self.question_ind = int(self.dialog.get_q_number())
            self.show_existing_question()

    def update_existing_question(self):
        text = self.plainTextEdit.toPlainText()
        if not text:
            pass
        else:
            setter = QuestionInserter(self.client, self.group)
            setter.update_existing_question(self.question_ind, text)
            self.add_values()
            self.question_ind = None
            self.plainTextEdit.clear()

    def save_button_clicked(self):
        if self.question_ind:
            self.update_existing_question()
        else:
            self.add_new_question()


class GenerateTicketsScreen(GenerateTicketsForm, QWidget):
    def __init__(self, client):
        super(GenerateTicketsScreen, self).__init__()
        self.setupUi(self)
        self.client = client
        self.add_values()
        self.pushButton.clicked.connect(self.generate_tickets)

    def add_values(self):
        getter = ListsGetter(self.client)
        self.comboBox.addItems([str(x) for x in range(3, 31)])
        self.comboBox_2.addItems([str(x) for x in range(1, 11)])
        self.comboBox_3.addItems(getter.get_positions())

    def generate_tickets(self):
        getter = QestionGetter(self.client, 'test_questions')
        shuffler = TestShuffler(getter)
        no_of_questions = int(self.comboBox.currentText())
        no_of_tickets = int(self.comboBox_2.currentText())
        full_list = []
        for i in range(no_of_tickets):
            block = shuffler.get_block(no_of_questions)
            full_list.append(block)
        generator = TicketDocGenerator(no_of_tickets, no_of_questions, full_list)
        generator.generate()


class OptionsScreen(Ui_OptionsForm, QWidget):
    def __init__(self, client):
        super(OptionsScreen, self).__init__()
        self.question_ind = None
        self.client = client
        self.dialog = None
        self.add_user_dialog = None
        self.setupUi(self)
        self.removePosition.clicked.connect(self.remove_position)
        self.addPosition.clicked.connect(self.add_position)
        self.addUser.clicked.connect(self.add_user)
        self.removeUser.clicked.connect(self.remove_user)

    def add_data(self):
        getter = ListsGetter(self.client, 'positions')
        positions = getter.get_positions()
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(5)
        for i, position in enumerate(positions, start=1):
            text = QLabel(text=f"{i}) {position}")
            text.setMinimumHeight(20)
            text.setWordWrap(True)
            layout.addWidget(text)
        widget.setLayout(layout)
        self.scrollArea.setWidget(widget)

    def show_q_number_dialog(self, positions):
        getter = ListsGetter(self.client, 'positions')
        self.dialog = ChosePositionNo()
        self.dialog.comboBox.addItems(positions)
        if self.dialog.exec() == QDialog.Accepted:
            self.question_ind = self.dialog.get_q()

    def remove_position(self):
        setter = PositionsManipulator(self.client)
        getter = ListsGetter(self.client, 'positions')
        positions = getter.get_positions()
        self.show_q_number_dialog(positions)
        setter.delete_one(self.question_ind)
        self.add_data()

    def add_position(self):
        setter = PositionsManipulator(self.client)
        new_position = self.lineEdit.text()
        if new_position:
            i = setter.add_new_position(new_position)
            label = QLabel(text=f"{i}) {new_position}")
            label.setMinimumHeight(20)
            label.setWordWrap(True)
            self.scrollArea.widget().layout().addWidget(label)
            self.lineEdit.clear()
            bar = self.scrollArea.verticalScrollBar()
            bar.rangeChanged.connect(lambda x, y: bar.setValue(9999))

    def add_user(self):
        self.add_user_dialog = AddUser()
        creditnails_man = LoginManipulator(self.client)
        if self.add_user_dialog.exec() == QDialog.Accepted:
            user, password = self.add_user_dialog.return_data()
            creditnails_man.add_new_pair(user, password)

    def remove_user(self):
        self.add_user_dialog = AddUser()
        creditnails_man = LoginManipulator(self.client)
        if self.add_user_dialog.exec() == QDialog.Accepted:
            user, password = self.add_user_dialog.return_data()
            creditnails_man.delete_one(user, password)
