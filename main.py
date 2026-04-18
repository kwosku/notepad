import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtGui import QAction


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

        # Подменю
        submenu = file_menu.addMenu("Submenu")

        # Action
        option_action = QAction("Option 1", self)
        submenu.addAction(option_action)

app = QApplication(sys.argv)
window = WindowApp()
window.show()
sys.exit(app.exec())