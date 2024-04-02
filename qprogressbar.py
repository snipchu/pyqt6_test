from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QVBoxLayout
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("")

        self.progbar = QProgressBar()
        self.progbarval = 0;
        more = QPushButton("more", clicked = self.grow)
        reset = QPushButton("reset", clicked = self.set0)

        layout = QVBoxLayout()
        layout.addWidget(self.progbar)
        layout.addWidget(more)
        layout.addWidget(reset)

        self.setLayout(layout)
        self.show()
    def grow(self): 
        if (self.progbarval < self.progbar.maximum()):
            self.progbarval += 5;
            self.progbar.setValue(self.progbarval)

    def set0(self):
        self.progbarval = 0
        self.progbar.setValue(self.progbarval)

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
