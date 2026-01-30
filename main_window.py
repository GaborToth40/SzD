from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout

from decks_window import DecksWindow
from cards_window import CardsWindow
from learning_window import LearningWindow
from statistics_window import StatisticsWindow
from about_window import AboutWindow


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        quit_action = file_menu.addAction("Exit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("copy")
        edit_menu.addAction("cut")
        edit_menu.addAction("paste")
        edit_menu.addAction("undo")
        edit_menu.addAction("redo")

        menu_bar.addAction("About").triggered.connect(self.about_open)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        #self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        central_widget.setLayout(self.main_layout)


        button_decks = QPushButton("Decks")
        self.main_layout.addWidget(button_decks)
        button_decks.clicked.connect(self.decks_open)

        button_cards = QPushButton("Cards")
        self.main_layout.addWidget(button_cards)
        button_cards.clicked.connect(self.cards_open)

        button_learning = QPushButton("Learning")
        self.main_layout.addWidget(button_learning)
        button_learning.clicked.connect(self.learning_open)

        button_statistics = QPushButton("Statistics")
        self.main_layout.addWidget(button_statistics)
        button_statistics.clicked.connect(self.learning_open)

        button_about = QPushButton("About")
        self.main_layout.addWidget(button_about)
        button_about.clicked.connect(self.statistics_open)


        self.deckswindow = DecksWindow()
        self.cardswindow = CardsWindow()
        self.learningwindow = LearningWindow()
        self.statisticswindow = StatisticsWindow()
        self.aboutwindow = AboutWindow()


    def quit_app(self):
        self.app.quit()

    def decks_open(self):
        self.deckswindow.show()

    def cards_open(self):
        self.cardswindow.show()

    def learning_open(self):
        self.learningwindow.show()

    def statistics_open(self):
        self.statisticswindow.show()

    def about_open(self):
        self.aboutwindow.show()