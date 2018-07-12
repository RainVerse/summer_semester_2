from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QPushButton, QLabel, QGridLayout, QFrame, QRadioButton)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from service.RecordService import RecordService


class ShowMedicalRecordWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(1)
        # 外层网格

        self.gridinformation = QGridLayout()
        self.gridinformation.setSpacing(10)
        # 病人基本信息网格，行距1个字距

        self.title = QLabel('                                电子病历', self)
        self.title.setFont(QFont("Microsoft YaHei", 18, QFont.Bold))
        # title.move(235, 15)
        self.gridinformation.addWidget(self.title, 0, 0)

        string = '  姓名: '
        self.name = QLabel(string, self)
        self.name.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.name, 1, 0)

        string = '工作单位: '
        self.company = QLabel(string, self)
        self.company.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.company, 1, 1)

        string = '  性别: '
        self.gender = QLabel(string, self)
        self.gender.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.gender, 2, 0)

        string = '住       址: '
        self.address = QLabel(string, self)
        self.address.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.address, 2, 1)

        string = '  年龄: '
        self.age = QLabel(string, self)
        self.age.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.age, 3, 0)

        string = '科       室: '
        self.department = QLabel(string, self)
        self.department.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.department, 3, 1)

        string = '  民族: '
        self.nation = QLabel(string, self)
        self.nation.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.nation, 4, 0, )

        string = '日       期: '
        self.date = QLabel(string, self)
        self.date.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation.addWidget(self.date, 4, 1, )

        self.gridinformation2 = QGridLayout()
        self.gridinformation2.setSpacing(1)

        string = '症       状: '
        self.symptom = QLabel(string, self)
        self.symptom.setWordWrap(True)
        self.symptom.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation2.addWidget(self.symptom, 4, 0, 4, 2)

        string = '病情结论: '
        self.conclusion = QLabel(string, self)
        self.conclusion.setWordWrap(True)
        self.conclusion.setFont(QFont("Microsoft YaHei", 11))
        self.gridinformation2.addWidget(self.conclusion, 5, 0, 5, 2)
        # 病人基础信息网格布局

        self.setGeometry(0, 0, 570, 650)
        self.setFixedSize(610, 650)
        self.center()
        self.setWindowTitle('电子病历')
        self.gridsign = QGridLayout()
        self.gridsign.setSpacing(1)
        self.signframe = QFrame(self)
        self.signframe.setFrameShape(QFrame.StyledPanel)
        self.signframe.move(20, 420)
        self.signframe.resize(575, 190)

    def load_ui_not_signed(self):

        string = '          是否电子签名，若进行电子签名，病历便不能修改'
        self.signprompt = QLabel(string, self)
        self.signprompt.setFont(QFont("Microsoft YaHei", 11))
        self.gridsign.addWidget(self.signprompt, 0, 0)

        self.yes = QRadioButton('是', self)
        self.yes.setFocusPolicy(Qt.NoFocus)
        self.yes.toggle()

        self.no = QRadioButton('否', self)
        self.no.setFocusPolicy(Qt.NoFocus)
        self.no.toggle()
        self.gridsign.addWidget(self.yes, 1, 1)
        self.gridsign.addWidget(self.no, 1, 2)

        self.gridbutton = QGridLayout()
        self.gridbutton.setSpacing(1)
        self.okButton = QPushButton('提交')
        self.okButton.setFixedSize(60, 30)
        self.gridbutton.addWidget(self.okButton, 0, 2)

        self.grid.addLayout(self.gridbutton, 3, 0)
        self.grid.addLayout(self.gridinformation, 0, 0)
        self.grid.addLayout(self.gridinformation2, 1, 0)
        self.grid.addLayout(self.gridsign, 2, 0)
        self.setLayout(self.grid)
        if hasattr(self,'Sign'):
            self.Sign.hide()


    def load_ui_signed(self, name):

        self.Sign = QLabel('         电子签名：' + name, self)
        self.Sign.setFont(QFont("Microsoft YaHei", 14, QFont.Bold))
        self.gridsign.addWidget(self.Sign, 2, 0)

        self.grid.addLayout(self.gridinformation, 0, 0)
        self.grid.addLayout(self.gridinformation2, 1, 0)
        self.grid.addLayout(self.gridsign, 2, 0)
        self.setLayout(self.grid)

        if hasattr(self,'signprompt'):
            self.signprompt.hide()
            self.yes.hide()
            self.no.hide()
            self.okButton.hide()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_data(self, name):
        self.data = RecordService().get_record_data(name)

    def refresh_data(self):
        if self.data is None:
            return False
        self.name.setText('  姓名: ' + self.data.get('name'))
        self.company.setText('工作单位: ' + self.data.get('company'))
        self.gender.setText('  性别: ' + self.data.get('gender'))
        self.age.setText('  年龄: ' + self.data.get('age'))
        self.address.setText('住       址: ' + self.data.get('address'))
        self.department.setText('科       室: ' + self.data.get('department'))
        self.nation.setText('  民族: ' + self.data.get('nation'))
        self.date.setText('日       期: ' + self.data.get('date'))
        self.symptom.setText('症       状: ' + self.data.get('symptom'))
        self.conclusion.setText('病情结论: ' + self.data.get('conclusion'))
        if self.data.get('sign') is None:
            self.load_ui_not_signed()
        else:
            self.load_ui_signed(self.data.get('sign'))
        return True
