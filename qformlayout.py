from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QPushButton, QLineEdit
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("qformlayout")

        form = QFormLayout()
        form.addRow("Username: ", QLineEdit())
        form.addRow("Password: ", QLineEdit(echoMode=QLineEdit.EchoMode.Password))
        form.addRow("Type password again: ", QLineEdit(echoMode=QLineEdit.EchoMode.Password))
        form.addRow("Email: ", QLineEdit())
        form.addRow("Phone number: ", QLineEdit())

        form.addRow(QPushButton("Sign up"), QPushButton("Cancel"))

        self.setLayout(form)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
