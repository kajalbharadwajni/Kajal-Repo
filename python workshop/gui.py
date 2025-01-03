import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
class NormalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setGeometry(100,100,300,200)


        self.layout = QVBoxLayout(self)
        title_label = QLabel("hello world")
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label) 

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NormalWindow()
    window.show()
    sys.exit(app.exec_())


