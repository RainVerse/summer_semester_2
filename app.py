import sys
from PyQt5.QtWidgets import QApplication
from digital_record_system import DigitalRecordSystem

app = QApplication(sys.argv)
system = DigitalRecordSystem()
system.main_window.set_user_id(233)
system.main_window.show()
sys.exit(app.exec_())
