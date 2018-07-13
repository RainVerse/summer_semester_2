from PyQt5.QtWidgets import (QTextEdit, QWidget, QDesktopWidget, QPushButton, QLabel, QGridLayout,QMessageBox)
from PyQt5.QtGui import QFont
from service.RecordService import RecordService


class UpdateMedicalRecordWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.record_id = None
        self.user_id = None
        self.data = None
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        # 外层网格

        self.gridinformation = QGridLayout()
        self.gridinformation.setSpacing(20)
        # 病人基本信息网格，行距1个字距

        self.title = QLabel('电子病历', self)
        self.title.setFont(QFont("Microsoft YaHei", 18, QFont.Bold))
        self.gridinformation.addWidget(self.title, 0, 0)

        string = '姓       名: '
        self.name = QLabel(string, self)
        self.name.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.name, 1, 0)

        string = '工作单位: '
        self.company = QLabel(string, self)
        self.company.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.company, 1, 1)

        string = '性       别: '
        self.gender = QLabel(string, self)
        self.gender.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.gender, 2, 0)

        string = '住       址: '
        self.address = QLabel(string, self)
        self.address.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.address, 2, 1)

        string = '年       龄: '
        self.age = QLabel(string, self)
        self.age.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.age, 3, 0)

        string = '科       室: '
        self.department = QLabel(string, self)
        self.department.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.department, 3, 1)

        string = '民       族: '
        self.nation = QLabel(string, self)
        self.nation.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.nation, 4, 0)

        string = '日       期: '
        self.date = QLabel(string, self)
        self.date.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.date, 4, 1)

        self.gridinformation2 = QGridLayout()
        self.gridinformation2.setSpacing(15)

        string = '症       状：'
        self.symptom = QLabel(string, self)
        self.symptom.setWordWrap(True)
        self.symptom.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation2.addWidget(self.symptom, 0, 0)
        self.symptomEdit = QTextEdit()
        self.gridinformation2.addWidget(self.symptomEdit, 0, 1, 2, 1)

        string = '病情结论：'
        self.conclusion = QLabel(string, self)
        self.conclusion.setWordWrap(True)
        self.conclusion.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation2.addWidget(self.conclusion, 2, 0)
        # 病人基础信息网格布局
        self.conclusionEdit = QTextEdit()
        self.gridinformation2.addWidget(self.conclusionEdit, 2, 1, 2, 1)

        self.gridsign = QGridLayout()
        self.gridsign.setSpacing(1)

        self.Sign = QLabel('', self)
        self.Sign.setFont(QFont("Microsoft YaHei", 14, QFont.Bold))
        self.gridsign.addWidget(self.Sign, 0, 0)

        self.gridbutton = QGridLayout()
        self.gridbutton.setSpacing(1)
        self.updateButton = QPushButton('修改')
        self.updateButton.clicked.connect(self.on_commit_button_clicked)
        self.updateButton.setFixedSize(60, 30)
        self.gridbutton.addWidget(self.updateButton, 0, 2)

        self.grid.addLayout(self.gridbutton, 3, 0)
        self.grid.addLayout(self.gridinformation, 0, 0)
        self.grid.addLayout(self.gridinformation2, 1, 0)
        self.grid.addLayout(self.gridsign, 2, 0)
        self.setLayout(self.grid)

        self.setGeometry(0, 0, 570, 650)
        self.setFixedSize(610, 650)
        self.center()
        self.setWindowTitle('电子病历')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_data(self, name):
        self.data = RecordService().get_record_data(name)

    def refresh_data(self, user_id):
        if self.data is None:
            return False
        self.record_id = self.data.get('id')
        self.user_id = user_id
        self.name.setText('  姓名: ' + self.data.get('name'))
        self.company.setText('工作单位: ' + self.data.get('company'))
        self.gender.setText('  性别: ' + self.data.get('gender'))
        self.age.setText('  年龄: ' + self.data.get('age'))
        self.address.setText('住       址: ' + self.data.get('address'))
        self.department.setText('科       室: ' + self.data.get('department'))
        self.nation.setText('  民族: ' + self.data.get('nation'))
        self.date.setText('日       期: ' + self.data.get('date'))
        self.symptomEdit.setText(self.data.get('symptom'))
        self.conclusionEdit.setText(self.data.get('conclusion'))
        self.Sign.setText('电子签名：' + self.data.get('sign') if self.data.get('sign') is not None else '无')
        return True

    def on_commit_button_clicked(self):
        updated_data = {'symptom': self.symptomEdit.toPlainText(), 'conclusion': self.conclusionEdit.toPlainText()}
        ret, message = RecordService().update_record_data(self.user_id, self.record_id, updated_data)
        QMessageBox.information(self, "警告", message, QMessageBox.Yes)
        if ret:
            self.hide()
