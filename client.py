from PySide6.QtWidgets import QApplication
import sys
from src.client.login_window import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    app.exec()

