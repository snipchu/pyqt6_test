from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
import sys

class MainProgram(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        line = QLineEdit()
        label = QLabel()
        line.textChanged.connect(label.setText)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(line)
        layout.addWidget(label)

        self.setWindowTitle("hello world")
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainProgram()
    sys.exit(app.exec())

app.exec()
