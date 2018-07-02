import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

w = QWidget()
w.resize(500, 600)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())
