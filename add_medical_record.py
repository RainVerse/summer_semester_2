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
        gridinformation = QGridLayout()
        gridinformation.setSpacing(10)
        # 病人基本信息网格，行距1个字距

        title = QLabel('电子病历', self)
        title.setFont(QFont("Microsoft YaHei", 18, QFont.Bold))
        gridinformation.addWidget(title, 0, 0)

        string = '姓       名：'
        name = QLabel(string, self)
        name.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(name, 2, 0)
        self.nameEdit = QLineEdit()
        gridinformation.addWidget(self.nameEdit, 2, 1)

        string = '性       别：'
        gender = QLabel(string, self)
        gender.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(gender, 3, 0)
        self.namecombo = QComboBox(self)
        self.namecombo.addItem('男')
        self.namecombo.addItem('女')
        gridinformation.addWidget(self.namecombo, 3, 1)

        string = '年       龄：'
        age = QLabel(string, self)
        age.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(age, 4, 0)
        self.ageEdit = QLineEdit()
        gridinformation.addWidget(self.ageEdit, 4, 1)

        string = '民       族：'
        nation = QLabel(string, self)
        nation.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(nation, 5, 0, )
        self.nationEdit = QLineEdit()
        gridinformation.addWidget(self.nationEdit, 5, 1)

        string = '工作单位：'
        company = QLabel(string, self)
        company.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(company, 6, 0)
        self.companyEdit = QLineEdit()
        gridinformation.addWidget(self.companyEdit, 6, 1)

        string = '住       址：'
        address = QLabel(string, self)
        address.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(address, 7, 0)
        self.addressEdit = QLineEdit()
        gridinformation.addWidget(self.addressEdit, 7, 1)

        string = '科       室：'
        department = QLabel(string, self)
        department.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(department, 8, 0)
        self.gendercombo = QComboBox(self)
        for d in self.departmentlist:
            self.gendercombo.addItem(d[0])
        gridinformation.addWidget(self.gendercombo, 8, 1)

        string = '症       状：'
        symptom = QLabel(string, self)
        symptom.setWordWrap(True)
        symptom.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(symptom, 10, 0)
        self.symptomEdit = QTextEdit()
        gridinformation.addWidget(self.symptomEdit, 10, 1, 2, 1)

        string = '病情结论：'
        conclusion = QLabel(string, self)
        conclusion.setWordWrap(True)
        conclusion.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(conclusion, 13, 0)
        # 病人基础信息网格布局
        self.conclusionEdit = QTextEdit()
        gridinformation.addWidget(self.conclusionEdit, 14, 1, 2, 1)

        addButton = QPushButton('添加', self)
        addButton.setFixedSize(60, 30)
        addButton.clicked.connect(self.commit)
        gridinformation.addWidget(addButton, 16, 1)

        self.setLayout(gridinformation)
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
        age=self.ageEdit.text()
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    AMR = AddMedicalRecord()
    sys.exit(app.exec_())
