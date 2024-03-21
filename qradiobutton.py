from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        radio1 = QRadioButton("Label 1")
        radio2 = QRadioButton("Label 2")
        radio3 = QRadioButton("Label 3")
        self.label = QLabel("You chose: No label")
        radio1.toggled.connect(self.was_clicked)
        radio2.toggled.connect(self.was_clicked)
        radio3.toggled.connect(self.was_clicked)
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)
        layout.addWidget(self.label)

        self.show()

    def was_clicked(self, word):
        rb = self.sender()
        if rb.isChecked(): 
            self.label.setText(f"You chose: {rb.text()}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
