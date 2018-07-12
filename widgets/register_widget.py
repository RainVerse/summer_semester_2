from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore


class RegisterWidget(QWidget):
    signal_user = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        user = QLabel('用户名')
        password = QLabel('密码')
        ackpw = QLabel('确认密码')

        self.userEdit = QLineEdit(self)
        self.pwEdit = QLineEdit(self)
        self.ackpwEdit = QLineEdit(self)

        # 设置为密码模式
        self.pwEdit.setEchoMode(2)
        self.ackpwEdit.setEchoMode(2)

        form = QFormLayout()
        form.addRow(user, self.userEdit)
        form.addRow(password, self.pwEdit)
        form.addRow(ackpw, self.ackpwEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(form)
        vbox.addSpacing(10)

        self.btn = QPushButton('注册', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.checkInfo)

        cancelbtn = QPushButton('退出')
        cancelbtn.resize((cancelbtn.sizeHint()))
        cancelbtn.clicked.connect(self.hide)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn)
        hbox.addWidget(cancelbtn)
        hbox.addStretch(1)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.resize(350, 400)
        self.center()
        self.setWindowTitle('注册')

    # 放置在屏幕中心
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def infoWindow(self):
    # IW = InfoWindow()
    # IW.transInfo(self.userEdit.text(),self.pwEdit.text())
    def transInfo(self):
        self.signal_user.emit(self.userEdit.text(), self.pwEdit.text())
        print("transInfo from reg")
        self.hide()

    def checkInfo(self):
        print("check info")
        if (self.pwEdit.text() == self.ackpwEdit.text()):
            print("correct")
            self.transInfo()
        else:
            print("incorrect")
            QMessageBox.information(self, "提示", "两次输入的密码不相同")

# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    reg = Register()
#    reg.show()
#    iw = InfoWindow()
#    reg.signal_user.connect(iw.show)
#    reg.signal_user.connect(iw.getUser)
#    iw.tkonbtn.clicked.connect(iw.transInfo)


#    sys.exit(app.exec_())
