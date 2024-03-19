from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QCompleter, QVBoxLayout
import sys
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("qlineedit")
        
        word_list = {
            "art", "apple", "aardvark",
            "beetle", "bottle", "bear",
            "cattle", "course", "camp",
            "dog", "damp", "destroy"
        }

        completer=QCompleter(word_list)

        line_edit =QLineEdit(
            "default value",
            self,
            clearButtonEnabled=True,
            #echoMode=QLineEdit.EchoMode.Password
        )
        line_edit.setCompleter(completer)

        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        self.setLayout(layout)

        self.show()

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    sys.exit(app.exec())
