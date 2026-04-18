from PySide6.QtWidgets import QFileDialog, QMessageBox

def open_file(self):
    file_name, filter = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")

    if file_name:
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                self.text_edit.setText(content)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Не удалось открыть файл: {e}")

def save_file(self):
    file_name, filter = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")

    if file_name:
        try:
            with open(file_name, 'w') as file:
                content = self.text_edit.toPlainText()
                file.write(content)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Не удалось сохранить файл: {e}")

def new_file(self):
    if self.text_edit.toPlainText():
        reply = QMessageBox.question(
            self,
            "Новый файл",
            "Вы сохранили текущий файл?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

    self.text_edit.clear()