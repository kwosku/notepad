from PySide6.QtWidgets import (QMainWindow, QTextEdit)

class window_app(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Блокнот")
        self.setGeometry(100, 100, 800, 600)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)


class header(QMainWindow):
    ...
