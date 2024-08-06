from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar


class PopUpMenuBar(QMenuBar):
    def __init__(self, parent):
        self.menu_action = None
        self.options_action = None
        self._parent = parent
        super().__init__(parent)

    def setUI(self):
        menu = self.addMenu("Навигация")
        self.menu_action = QAction("Меню", parent=self._parent)
        self.options_action = QAction("Настройки", parent=self._parent)
        menu.addAction(self.menu_action)
        menu.addAction(self.options_action)
