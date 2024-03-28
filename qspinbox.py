from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSpinbox")

        self.label = QLabel("You chose: ")
        
        spinbox = QSpinBox(prefix="#", value=40, minimum=20, maximum=60, singleStep=2, wrapping=True)
        spinbox.valueChanged.connect(self.val_changed)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(spinbox)
        layout.addWidget(self.label)

        self.show()

    def val_changed(self, msg):
        self.label.setText(f"You chose #{msg}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
