from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateEdit
import sys
from datetime import date

class window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDateEdit")
        self.setMinimumWidth(150)

        self.label = QLabel("You picked:")
        self.date = QDateEdit()
        self.date.editingFinished.connect(self.was_changed)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.label)
        layout.addWidget(self.date)

        self.show()

    def was_changed(self):
        self.foo = self.date.date()
        self.label.setText(f"You picked: {self.foo.toPyDate()}")

if __name__ == "__main__":
    app = QApplication([])
    win = window()
    sys.exit(app.exec())
