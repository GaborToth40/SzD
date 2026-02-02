# Python 3.14.2
# PySide6 6.10.1
# SQLite

from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()
