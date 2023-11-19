from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from src.client.register_widget import RegisterWidget
from src.client.login_widget import LoginWidget


class LoginWindow(QtWidgets.QWidget):
    register_state = 0

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setFixedSize(300, 180)

        # Init layouts

        self.main_layout = QtWidgets.QVBoxLayout()
        self.widgets_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout = QtWidgets.QHBoxLayout()

        # Init widgets

        self.login_widget = LoginWidget()
        self.register_widget = RegisterWidget()
        self.login_button = QtWidgets.QPushButton()
        self.register_button = QtWidgets.QPushButton()

        # Setting layouts

        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.widgets_layout)
        self.main_layout.addLayout(self.buttons_layout)
        self.widgets_layout.addWidget(self.login_widget)
        self.widgets_layout.addWidget(self.register_widget)
        self.buttons_layout.addWidget(self.login_button)
        self.buttons_layout.addWidget(self.register_button)
        self.widgets_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Setting widgets

        self.login_button.setText('Login')
        self.register_button.setText('Register')
        self.register_widget.hide()
        self.register_button.clicked.connect(self.change_register_state)
        self.login_button.clicked.connect(self.on_login_click)

    def on_login_click(self):
        if self.register_state > 0:
            self.register_state = 0
            self.switch_register_widget()

    def change_register_state(self):
        self.register_state = -1 if self.register_state == 1 else self.register_state
        self.register_state += 1
        self.switch_register_widget()

    def switch_register_widget(self):
        match self.register_state:
            case 0:
                self.register_widget.hide()
                self.login_widget.show()
            case 1:
                self.register_widget.show()
                self.login_widget.hide()
