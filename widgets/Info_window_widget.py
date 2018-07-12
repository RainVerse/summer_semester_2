from service.RegisterService import RegisterService
from sql.sql_functions import get_department_list
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class InfoWindowWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        name = QLabel('姓名')
        gender = QLabel('性别')
        age = QLabel('年龄')
        department = QLabel('科室')

        self.nameEdit = QLineEdit(self)
        self.genderEdit = QComboBox(self)
        self.ageEdit = QLineEdit(self)
        self.departmentEdit = QComboBox(self)

        self.genderEdit.setEditable(0)
        self.departmentEdit.setEditable(0)

        self.genderEdit.addItem('男', 0)
        self.genderEdit.addItem('女', 1)

        self.departmentlist = get_department_list()
        for d in self.departmentlist:
            print(d)
            self.departmentEdit.addItem(d[0])

        form = QFormLayout()
        form.addRow(name, self.nameEdit)
        form.addRow(gender, self.genderEdit)
        form.addRow(age, self.ageEdit)
        form.addRow(department, self.departmentEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(form)
        vbox.addSpacing(10)

        self.tkonbtn = QPushButton('提交', self)
        self.tkonbtn.resize(self.tkonbtn.sizeHint())

        cancelbtn = QPushButton('退出')
        cancelbtn.resize((cancelbtn.sizeHint()))

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.tkonbtn)
        hbox.addWidget(cancelbtn)
        hbox.addStretch(1)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.resize(350, 400)
        self.center()
        self.setWindowTitle('提交信息')

        self.tkonbtn.clicked.connect(self.transInfo())
        cancelbtn.clicked.connect(QCoreApplication.instance().quit)

    
    def getUser(self, ):
        print("get user")


    def transInfo(self,username, password):
        self.username = username
        self.password = password
        print("trans info to database")
        source = self.sender()
        regService = RegisterService()

        userInfo = [self.nameEdit.text(), self.departmentlist[self.departmentEdit.currentIndex()][1],
                    self.genderEdit.currentIndex() + 1, self.ageEdit.text()]
        regService.register(self.username, self.password, userInfo)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
