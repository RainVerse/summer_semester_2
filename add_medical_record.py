import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QLineEdit, QGridLayout,
                             QTextEdit, QComboBox)
from PyQt5.QtGui import QFont
from sql.sql_functions import get_department_list
from service.RecordService import RecordService


class AddMedicalRecord(QWidget):

    def __init__(self):
        super().__init__()
        self.departmentlist = get_department_list()
        self.initUI()
        self.data = {}

    def initUI(self):
        self.gridinformation = QGridLayout()
        self.gridinformation.setSpacing(10)
        # 病人基本信息网格，行距1个字距

        self.title = QLabel('电子病历', self)
        self.title.setFont(QFont("Microsoft YaHei", 18, QFont.Bold))
        self.gridinformation.addWidget(self.title, 0, 0)

        string = '姓       名：'
        self.name = QLabel(string, self)
        self.name.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.name, 2, 0)
        self.nameEdit = QLineEdit()
        self.gridinformation.addWidget(self.nameEdit, 2, 1)

        string = '性       别：'
        self.gender = QLabel(string, self)
        self.gender.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.gender, 3, 0)
        self.namecombo = QComboBox(self)
        self.namecombo.addItem('男')
        self.namecombo.addItem('女')
        self.gridinformation.addWidget(self.namecombo, 3, 1)

        string = '年       龄：'
        self.age = QLabel(string, self)
        self.age.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.age, 4, 0)
        self.ageEdit = QLineEdit()
        self.gridinformation.addWidget(self.ageEdit, 4, 1)

        string = '民       族：'
        self.nation = QLabel(string, self)
        self.nation.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.nation, 5, 0, )
        self.nationEdit = QLineEdit()
        self.gridinformation.addWidget(self.nationEdit, 5, 1)

        string = '工作单位：'
        self.company = QLabel(string, self)
        self.company.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.company, 6, 0)
        self.companyEdit = QLineEdit()
        self.gridinformation.addWidget(self.companyEdit, 6, 1)

        string = '住       址：'
        self.address = QLabel(string, self)
        self.address.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.address, 7, 0)
        self.addressEdit = QLineEdit()
        self.gridinformation.addWidget(self.addressEdit, 7, 1)

        string = '科       室：'
        self.department = QLabel(string, self)
        self.department.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.department, 8, 0)
        self.gendercombo = QComboBox(self)
        for d in self.departmentlist:
            self.gendercombo.addItem(d[0])
        self.gridinformation.addWidget(self.gendercombo, 8, 1)

        string = '症       状：'
        self.symptom = QLabel(string, self)
        self.symptom.setWordWrap(True)
        self.symptom.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.symptom, 10, 0)
        self.symptomEdit = QTextEdit()
        self.gridinformation.addWidget(self.symptomEdit, 10, 1, 2, 1)

        string = '病情结论：'
        self.conclusion = QLabel(string, self)
        self.conclusion.setWordWrap(True)
        self.conclusion.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.conclusion, 13, 0)
        # 病人基础信息网格布局
        self.conclusionEdit = QTextEdit()
        self.gridinformation.addWidget(self.conclusionEdit, 14, 1, 2, 1)

        self.addButton = QPushButton('添加', self)
        self.addButton.setFixedSize(60, 30)
        self.addButton.clicked.connect(self.commit)
        self.gridinformation.addWidget(self.addButton, 16, 1)

        self.setLayout(self.gridinformation)
        # 网格布局排列结束

        self.setGeometry(0, 0, 500, 650)
        self.setFixedSize(500, 650)
        self.center()
        # 窗口居中显示
        self.setWindowTitle('添加电子病历')

    def commit(self):
        self.data['name'] = self.nameEdit.text()
        self.data['company'] = self.companyEdit.text()
        self.data['gender'] = self.gendercombo.currentIndex() + 1
        self.data['address'] = self.addressEdit.text()
        age = self.ageEdit.text()
        if age.isdigit():
            self.data['age'] = int(age)
        else:
            print('input digit')
            return
        self.data['department_id'] = self.departmentlist[self.gendercombo.currentIndex()][1]
        self.data['nation'] = self.nationEdit.text()
        self.data['symptom'] = self.symptomEdit.toPlainText()
        self.data['conclusion'] = self.conclusionEdit.toPlainText()
        print(self.data)
        print(RecordService().add_record(self.data))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
