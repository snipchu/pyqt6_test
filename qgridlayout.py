from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        userlabel = QLabel("Username:")
        userline = QLineEdit(self, clearButtonEnabled=True)
        passlabel = QLabel("Password:")
        passline = QLineEdit(self, clearButtonEnabled=True, echoMode=QLineEdit.EchoMode.Password)
        loginbutton = QPushButton("Login")
        cancelbutton = QPushButton("Cancel")
        helpbutton = QPushButton("Help")
        
        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(userlabel, 0,0,1,1, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(userline, 0,1,1,2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(passlabel, 1,0,1,1, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(passline, 1,1,1,2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(loginbutton, 2,0,1,1, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(cancelbutton, 2,1,1,1, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(helpbutton, 2,2,1,1, Qt.AlignmentFlag.AlignLeft)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
