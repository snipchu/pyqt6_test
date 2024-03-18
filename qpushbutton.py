from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        button = QPushButton("Click me!!!")
        button.setCheckable(True)
        button.setIcon(QIcon('trash.png'))
        button.setFixedSize(QSize(150,50))

        button.clicked.connect(self.on_toggle)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def on_toggle(self, checked):
        print(checked)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    sys.exit(app.exec())
