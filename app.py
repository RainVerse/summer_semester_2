import sys
from PyQt5.QtWidgets import QApplication
from digital_record_system import DigitalRecordSystem

app = QApplication(sys.argv)
system = DigitalRecordSystem()
system.login_widget.show()
sys.exit(app.exec_())
