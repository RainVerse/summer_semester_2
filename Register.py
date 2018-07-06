import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from service.RegisterService import RegisterService
from sql.sql_functions import get_department_list

class Register(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        user = QLabel('用户名')
        password = QLabel('密码')
        ackpw = QLabel('确认密码')
        name = QLabel('姓名')
        gender = QLabel('性别')
        age = QLabel('年龄')
        department = QLabel('科室')

        self.userEdit = QLineEdit(self)
        self.pwEdit = QLineEdit(self)
        self.ackpwEdit = QLineEdit(self)
        self.nameEdit = QLineEdit(self)
        self.genderEdit = QComboBox(self)
        self.ageEdit = QLineEdit(self)
        self.departmentEdit = QComboBox(self)

        # 设置为密码模式
        self.pwEdit.setEchoMode(2)
        self.ackpwEdit.setEchoMode(2)

        self.genderEdit.setEditable(0)
        self.departmentEdit.setEditable(0)

        self.genderEdit.addItem('男',0)
        self.genderEdit.addItem('女',1)

        self.departmentlist = get_department_list()
        for d in self.departmentlist:
            print(d)
            self.departmentEdit.addItem(d[0])


        form = QFormLayout()
        form.addRow(user,self.userEdit)
        form.addRow(password,self.pwEdit)
        form.addRow(ackpw,self.ackpwEdit)
        form.addRow(name,self.nameEdit)
        form.addRow(gender,self.genderEdit)
        form.addRow(age,self.ageEdit)
        form.addRow(department,self.departmentEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(form)
        vbox.addSpacing(10)
        #self.setLayout(form)





        btn = QPushButton('注册',self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.transInfo)

        cancelbtn = QPushButton('退出')
        cancelbtn.resize((cancelbtn.sizeHint()))
        cancelbtn.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(cancelbtn)
        hbox.addStretch(1)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.resize(350,400)
        self.center()
        self.setWindowTitle('注册')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def transInfo(self):
        source = self.sender()
        regService = RegisterService()

        userInfo = [self.nameEdit.text(), self.departmentlist[self.departmentEdit.currentIndex()][1], self.genderEdit.currentIndex() + 1, self.ageEdit.text()]
        regService.register(self.userEdit.text(), self.pwEdit.text(), userInfo)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    reg = Register()
    sys.exit(app.exec_())
