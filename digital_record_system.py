from widgets.main_widget import MainWidget
from widgets.register_widget import RegisterWidget
from widgets.Info_window_widget import InfoWindowWidget
from widgets.login_widget import LoginWidget
from widgets.add_medical_record_widget import AddMedicalRecordWidget
from widgets.show_medical_record_widget import ShowMedicalRecordWidget


class DigitalRecordSystem:
    def __init__(self):
        self.main_widget = MainWidget()
        self.register_widget = RegisterWidget()
        self.info_window_widget = InfoWindowWidget()
        self.login_widget = LoginWidget()
        self.add_medical_record_widget = AddMedicalRecordWidget()
        self.show_medical_record_widget = ShowMedicalRecordWidget()
        self.init_slots()
        return

    def init_slots(self):
        self.register_widget.signal_user.connect(self.info_window_widget.show)
        self.register_widget.signal_user.connect(self.info_window_widget.getUser)
        self.login_widget.regbtn.clicked.connect(self.register_widget.show)
        self.login_widget.signal_login.connect(self.main_widget.set_user_id)
        self.login_widget.signal_login.connect(self.main_widget.show)
        return
