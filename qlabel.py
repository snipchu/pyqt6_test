from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QMovie
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("qlabel hell")

        label = QLabel("qlabel jumpscare! :ghost:")

        yippeelabel = QLabel()
        yippeelabel.setPixmap(QPixmap("yippee.png"))

        bunnyguy = QMovie("bunnyguy.gif")
        bunnyguylabel = QLabel()
        bunnyguylabel.setMovie(bunnyguy)
        bunnyguy.start()
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(yippeelabel)
        layout.addWidget(bunnyguylabel)

        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
