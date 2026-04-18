import sys
from PySide6.QtWidgets import QApplication

from gui import WindowApp

app = QApplication(sys.argv)
window = WindowApp()
window.show()
sys.exit(app.exec())