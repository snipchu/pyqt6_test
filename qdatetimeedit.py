from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateTimeEdit
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("qtimedatedit")

        self.qdateline = QLabel()
        self.qtimeline = QLabel()
        self.tedit = QDateTimeEdit(calendarPopup=True)
        self.tedit.dateTimeChanged.connect(self.editdone)

        layout = QVBoxLayout()
        layout.addWidget(self.qdateline)
        layout.addWidget(self.qtimeline)
        layout.addWidget(self.tedit)

        self.setLayout(layout)
        self.show()

    def editdone(self):
        self.qdateline.setText(f"Date: {str(self.tedit.date().toPyDate())}")
        self.qtimeline.setText(f"Time: {str(self.tedit.time().toPyTime())}")

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
