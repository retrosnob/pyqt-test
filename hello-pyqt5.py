from PyQt5.QtWidgets import QApplication, QLabel

print("Hello pyqt-test!")
app = QApplication([])
label = QLabel("Hello Label!")
label.show()
app.exec_()