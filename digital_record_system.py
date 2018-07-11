from widgets.main_widget import MainWidget
from widgets.Register import Register
from widgets.InfoWindow import InfoWindow
from widgets.Login import Login


class DigitalRecordSystem:
    def __init__(self):
        self.main_window = MainWidget()
        self.reg = Register()
        self.iw = InfoWindow()
        self.lgin = Login()
        return

    def init_slots(self):
        self.reg.signal_user.connect(self.iw.show)
        self.reg.signal_user.connect(self.iw.getUser())
        self.lgin.regbtn.connect(self.reg.show)
        return
