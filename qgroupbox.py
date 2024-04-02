from PyQt6.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QVBoxLayout
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("")

        groupbox = QGroupBox("lalalaAAAAAAAAA")
        boxlayout = QVBoxLayout()
        groupbox.setLayout(boxlayout)
        boxlayout.addWidget(QPushButton("hello world"))
        boxlayout.addWidget(QPushButton("hello world"))

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(groupbox)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
