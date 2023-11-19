from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class LoginWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Init layouts

        self.main_layout = QtWidgets.QVBoxLayout()
        self.line_edit_label_layout = QtWidgets.QHBoxLayout()
        self.line_edit_layout = QtWidgets.QVBoxLayout()
        self.label_layout = QtWidgets.QVBoxLayout()

        # Init elements

        self.login_label = QtWidgets.QLabel(self)
        self.password_label = QtWidgets.QLabel(self)
        self.login_line_edit = QtWidgets.QLineEdit(self)
        self.password_line_edit = QtWidgets.QLineEdit(self)

        # Setting layouts

        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.line_edit_label_layout)
        self.line_edit_label_layout.addLayout(self.label_layout)
        self.line_edit_label_layout.addLayout(self.line_edit_layout)
        self.label_layout.addWidget(self.login_label)
        self.label_layout.addWidget(self.password_label)
        self.line_edit_layout.addWidget(self.login_line_edit)
        self.line_edit_layout.addWidget(self.password_line_edit)
        self.line_edit_label_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        # Setting elements

        self.login_label.setText('Login')
        self.password_label.setText('Password')
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
