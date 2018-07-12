import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from service.LoginService import LoginService


class Login(QWidget):
    signal_login = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        user = QLabel('用户名')
        password = QLabel('密码')

        self.message = "输入用户名和密码"
        msgLabel = QLabel(self.message)
        self.userEdit = QLineEdit(self)
        self.pwEdit = QLineEdit(self)

        # 设置为密码模式
        self.pwEdit.setEchoMode(2)

        form = QFormLayout()
        form.addRow(user,self.userEdit)
        form.addRow(password,self.pwEdit)


        vbox = QVBoxLayout()
        vbox.addWidget(msgLabel)
        vbox.addSpacing(5)
        vbox.addLayout(form)
        vbox.addSpacing(10)

        btn = QPushButton('登录',self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.checkInfo)

        self.regbtn = QPushButton('注册',self)
        self.regbtn.resize(self.regbtn.sizeHint())
        #self.regbtn.clicked.connect(self.regist)

        cancelbtn = QPushButton('退出')
        cancelbtn.resize((cancelbtn.sizeHint()))
        cancelbtn.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(self.regbtn)
        hbox.addWidget(cancelbtn)
        hbox.addStretch(1)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.resize(350,400)
        self.center()
        self.setWindowTitle('登录')


    #放置在屏幕中心
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #def regist(self):
        #reg = Register()
        #reg.show()

    def checkInfo(self):
        ls = LoginService()
        check = ls.login(self.userEdit.text(), self.pwEdit.text())

        if(check[0]):
            print("Log in succeed")
            self.message = "登录成功"
            self.hide()
            self.signal_login.emit(self.message)
        else:
            print("Log in failed")
            self.message = check[1]
            QMessageBox.information(self, "提示", self.message)



#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    lgin = Login()
#    lgin.show()


 #   sys.exit(app.exec_())


