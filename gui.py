from PySide6.QtWidgets import QMainWindow, QTextEdit

from services import open_file, save_file, new_file

class WindowApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Блокнот")
        self.setGeometry(100, 100, 800, 600)

        # Центральное поле (чтобы окно не было пустым)
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # MenuBar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        openFile = file_menu.addAction("Open File")
        saveFile = file_menu.addAction("Save File")
        newFile = file_menu.addAction("New File")

        openFile.triggered.connect(lambda: open_file(self))
        saveFile.triggered.connect(lambda: save_file(self))
        newFile.triggered.connect(lambda: new_file(self))

