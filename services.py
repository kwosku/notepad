from PySide6.QtWidgets import QFileDialog


def open_file(self):
    path, _ = QFileDialog.getOpenFileName(self, "Open file")

    if path:
        with open(path, 'r', encoding='utf-8') as f:
            self.text_edit.setText(f.read())


def save_file(self):
    path, _ = QFileDialog.getSaveFileName(self, "Save file")

    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.text_edit.toPlainText())