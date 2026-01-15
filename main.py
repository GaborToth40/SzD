# Python 3.14.2
# PySide6 6.10.1

from PySide6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()
