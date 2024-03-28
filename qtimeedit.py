from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTimeEdit, QLabel
import sys

class win(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("qtimeedit")

        self.qline = QLabel()
        self.qtime = QTimeEdit()
        self.qtime.editingFinished.connect(self.finish_edit)

        layout = QVBoxLayout()
        layout.addWidget(self.qline)
        layout.addWidget(self.qtime)

        self.setLayout(layout)
        self.show()

    def finish_edit(self):
        self.foo = self.qtime.time().toPyTime()
        self.qline.setText(str(self.foo))

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    sys.exit(app.exec())
