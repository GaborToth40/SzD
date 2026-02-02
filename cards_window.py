from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton)
from database import connection, cursor

class CardsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cards")
        self.resize(800, 800)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Select", "ID", "Question", "Answer", "Note", "Weight", "Deck"])
        layout.addWidget(self.table)

        buttons_layout = QHBoxLayout()
        layout.addLayout(buttons_layout)

        self.save_button = QPushButton("Save")
        #self.save_button.clicked.connect(self.save_clicked)
        buttons_layout.addWidget(self.save_button)

        self.delete_button = QPushButton("Delete")
        #self.delete_button.clicked.connect(self.delete_selected_rows)
        buttons_layout.addWidget(self.delete_button)

        #self.decks = self.load_decks()

        #self.load_cards()
        #self.add_empty_row