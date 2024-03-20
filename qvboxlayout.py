from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("qvboxlayout")

        vlay = QVBoxLayout()
        self.setLayout(vlay)
        
        yesbutton = QPushButton("Yes")
        yesbutton.setStyleSheet("QPushButton{background-color: green;}")
        nobutton = QPushButton("No")
        nobutton.setStyleSheet("QPushButton{background-color: red;}")
        cancellabel = QLabel("Cancel")
        cancellabel.setStyleSheet("QLabel{background-color: blue;}")
        helplabel = QLabel("Help")
        helplabel.setStyleSheet("QLabel{background-color: gray;}")

        vlay.addWidget(yesbutton)
        vlay.addWidget(nobutton)
        vlay.addWidget(cancellabel)
        vlay.addWidget(helplabel)

        vlay.setStretchFactor(cancellabel, 2)
        vlay.setStretchFactor(helplabel, 1)

        vlay.setContentsMargins(20,20,20,20)
        vlay.setSpacing(10)

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
