from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QLabel, QVBoxLayout
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("")

        tab = QTabWidget(
            movable=True,
            tabPosition=QTabWidget.TabPosition.South
            #tabsClosable=True
            #tabShape=QTabWidget.TabShape.Triangular
        )

        tab1 = QWidget(tab)
        pagelayout1 = QVBoxLayout()
        pagelayout1.addWidget(QLabel("Hello world"))
        pagelayout1.addWidget(QPushButton("Hello world"))
        pagelayout1.addWidget(QLabel("Hello world"))
        pagelayout1.addWidget(QPushButton("Hello world"))
        tab1.setLayout(pagelayout1)
        tab.addTab(tab1, "tab 1")
        
        tab2 = QWidget(tab)
        pagelayout2 = QVBoxLayout()
        pagelayout2.addWidget(QPushButton("Hello world"))
        pagelayout2.addWidget(QLabel("Hello world"))
        pagelayout2.addWidget(QPushButton("Hello world"))
        pagelayout2.addWidget(QLabel("Hello world"))
        tab2.setLayout(pagelayout2)
        tab.addTab(tab2, "tab 2")


        layout = QVBoxLayout()
        layout.addWidget(tab)

        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
