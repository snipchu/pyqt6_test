from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt6.QtCore import Qt
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("")

        self.label = QLabel("You chose: 25")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setValue(25)
        self.slider.setRange(0,50)
        self.slider.setSingleStep(2)
        self.slider.setPageStep(5)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.valueChanged.connect(self.waschanged)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        self.setLayout(layout)
        self.show()
    def waschanged(self):
        self.label.setText(f"You chose: {str(self.slider.value())}")

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
