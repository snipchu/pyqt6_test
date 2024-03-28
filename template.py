from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("")

        layout = QVBoxLayout()

        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
