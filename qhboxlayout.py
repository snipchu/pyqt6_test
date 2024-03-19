from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("qhboxlayout")

        buttons = QHBoxLayout();
        titles=["Yes", "No", "Cancel", "Help"]
        buttonlist=[QPushButton(title) for title in titles]
        buttons.addWidget(buttonlist[0])
        buttons.addWidget(buttonlist[1])
        buttons.addStretch()
        buttons.addWidget(buttonlist[2])
        buttons.addWidget(buttonlist[3])
        buttons.setSpacing(20)
        buttons.setContentsMargins(0,20,0,0)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello world"))
        layout.addWidget(QLineEdit("Your answer here", clearButtonEnabled=True))
        layout.addLayout(buttons)
        
        self.setLayout(layout);
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
