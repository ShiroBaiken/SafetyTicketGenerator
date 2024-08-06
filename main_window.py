from PySide6 import QtWidgets
from pymongo import MongoClient

from menu_bar import PopUpMenuBar
from screens import (MainMenu, LoginScreen, GenerateTicketsScreen, AddQuestionScreen, QuestionGroupSelectScreen,
                     OptionsScreen)
from test_manipulator import CollectionGetter
from ui_login import Ui_MainWindow as LoginWindow

client = MongoClient("HOST", port="PORT")


class MainWindow(LoginWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.main_menu = MainMenu()
        self.login_screen = LoginScreen(client)
        self.ticket_gen_screen = GenerateTicketsScreen(client)
        self.add_q_screen = AddQuestionScreen(client)
        self.q_group_select = QuestionGroupSelectScreen(client)
        self.options = OptionsScreen(client)
        self.menu_bar = PopUpMenuBar(self)
        self.menu_bar.setUI()
        self.menu_bar.hide()
        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.q_group_select)
        self.stacked_widget.addWidget(self.add_q_screen)
        self.stacked_widget.addWidget(self.ticket_gen_screen)
        self.stacked_widget.addWidget(self.options)
        self.stacked_widget.setCurrentIndex(0)
        self.login_screen.pushButton.clicked.connect(self.login_button_clicked)
        self.login_screen.lineEdit_2.returnPressed.connect(self.login_button_clicked)
        self.main_menu.pushButton.clicked.connect(lambda: self.nav_button_clicked_with_menu_show(4))
        self.main_menu.pushButton_3.clicked.connect(self.show_options)
        self.q_group_select.pushButton.clicked.connect(self.show_question_edit_for_selected_group)
        self.main_menu.pushButton_2.clicked.connect(lambda: self.nav_button_clicked_with_menu_show(2))
        self.menu_bar.menu_action.triggered.connect(lambda: self.button_clicked(1))
        self.menu_bar.options_action.triggered.connect(self.show_options)

    def button_clicked(self, ind):
        """switches screens in main window, resizes main window if needed"""
        self.stacked_widget.setCurrentIndex(ind)
        self.resize(self.stacked_widget.currentWidget().minimumSize())
        self.setFixedSize(self.stacked_widget.currentWidget().minimumSize())
        if not self.menu_bar.isHidden():
            self.menu_bar.hide()

    def login_button_clicked(self):
        """switches from login screen to main window"""
        success = self.stacked_widget.currentWidget().button_cliked()
        if success:
            self.button_clicked(1)

    def nav_button_clicked_with_menu_show(self, ind):
        self.button_clicked(ind)
        self.menu_bar.show()
        self.setFixedHeight(self.height() + self.menu_bar.height() + 10)

    def show_question_edit_for_selected_group(self):
        """switches to question edit screen for selected group of questions
            Shows navigation button"""
        coll_name = self.stacked_widget.currentWidget().comboBox_2.currentText()
        getter = CollectionGetter(client)
        self.button_clicked(3)
        self.stacked_widget.currentWidget().group = getter.get_collection(coll_name)
        self.stacked_widget.currentWidget().add_values()
        self.menu_bar.show()
        self.setFixedHeight(self.height() + self.menu_bar.height() + 10)

    def show_options(self):
        """shows options screen with navigation button"""
        self.button_clicked(5)
        self.stacked_widget.currentWidget().add_data()
        self.menu_bar.show()
        self.setFixedHeight(self.height() + self.menu_bar.height())
