from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("")

        widget1 = QWidget()
        hbox1 = QHBoxLayout()
        widget1.setLayout(hbox1)
        hbox1.addWidget(QPushButton("Hello world"))
        hbox1.addWidget(QPushButton("Hello world"))
        hbox1.addWidget(QPushButton("Hello world"))

        widget2 = QWidget()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QPushButton("Hello world2"))
        hbox2.addWidget(QPushButton("Hello world2"))
        hbox2.addWidget(QPushButton("Hello world2"))
        widget2.setLayout(hbox2)

        layout = QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)

        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
