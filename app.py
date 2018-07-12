import sys
from PyQt5.QtWidgets import QApplication
from digital_record_system import DigitalRecordSystem

app = QApplication(sys.argv)
system = DigitalRecordSystem()
system.login_widget.show()
#system.main_widget.set_user_id(233)
#system.main_widget.show()
#system.register_widget.show()
sys.exit(app.exec_())
