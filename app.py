import sys
from PyQt5.QtWidgets import QApplication
from digital_record_system import DigitalRecordSystem

if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = DigitalRecordSystem()
    system.login_widget.show()
    sys.exit(app.exec_())
