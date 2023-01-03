from abc import ABC, abstractmethod

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Mock observers
        self.angel_listener = AngelListener()
        self.devil_listener = DevilListener()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        button = QPushButton("Press Me!")
        # Attaching observers to observable button
        button.clicked.connect(self.devil_listener.action_performed)
        button.clicked.connect(self.angel_listener.action_performed)

        self.setCentralWidget(button)

    def button_clicked(self):
        print('clicked')


class ActionListener(ABC):
    @abstractmethod
    def action_performed(self, e):
        ...


class AngelListener(ActionListener):
    def action_performed(self, e):
        print('Dont do it, you might regret it!')


class DevilListener(ActionListener):
    def action_performed(self, e):
        print('Come on, do it!')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
