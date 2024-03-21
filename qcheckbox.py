from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Qcheckbox")

        vbox = QVBoxLayout()
        self.checkbox = QCheckBox("click me!", self)
        self.checkbox.setTristate(True)
        vbox.addWidget(self.checkbox)
        
        checkbutton = QPushButton("check")
        checkbutton.clicked.connect(self.check)
        uncheckbutton = QPushButton("uncheck")
        uncheckbutton.clicked.connect(self.uncheck)
        vbox.addWidget(checkbutton)
        vbox.addWidget(uncheckbutton)

        self.setLayout(vbox)
        self.show()
    def check(self):
        self.checkbox.setChecked(True)

    def uncheck(self):
        self.checkbox.setChecked(False)

if __name__ == "__main__":
    app = QApplication([])
    widnodw = MainWindow()
    sys.exit(app.exec())
