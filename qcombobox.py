from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.choicelabel = QLabel("You chose: ")
        self.indexlabel = QLabel("Index: ")

        self.combobox = QComboBox(self)
        self.combobox.addItem("Test 1")
        self.combobox.addItem("Test 3")
        self.combobox.insertItem(1,"Test 2")
        self.combobox.activated.connect(self.update)
        layout.addWidget(self.combobox)
        layout.addWidget(self.choicelabel)
        layout.addWidget(self.indexlabel)

        self.show()

    def update(self):
        self.choicelabel.setText(f"You chose: {self.combobox.currentText()}")
        self.indexlabel.setText(f"Index: {self.combobox.currentIndex()}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
