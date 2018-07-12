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
        self.init_connects()
        return

    def init_slots(self):
        self.register_widget.signal_user.connect(self.info_window_widget.show)
        self.register_widget.signal_user.connect(self.info_window_widget.getUser)
        self.login_widget.regbtn.clicked.connect(self.register_widget.show)
        self.login_widget.signal_login.connect(self.main_widget.set_user_id)
        self.login_widget.signal_login.connect(self.main_widget.show)
        return

    def init_connects(self):
        self.main_widget.ui.add_button.clicked.connect(self.add_medical_record_widget.show)
        self.main_widget.ui.search_button.clicked.connect(self.show_search_widget)

    def show_search_widget(self):
        name=self.main_widget.get_search_info()
        self.show_medical_record_widget.load_data(name)
        if self.show_medical_record_widget.refresh_data():
            self.show_medical_record_widget.show()
        else:
            self.main_widget.search_fail_message()
