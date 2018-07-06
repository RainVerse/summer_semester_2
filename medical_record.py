#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QPushButton, QVBoxLayout, QLabel,
                             QHBoxLayout, QLineEdit, QGridLayout,
                             QSplitter, QFrame, QCheckBox)
from PyQt5.QtGui import QFont


class MedicalRecord(QWidget):

    def __init__(self):
        super().__init__()

        '''self.addName()
        self.addGender()
        self.addAge()
        self.addAddress()
        self.addCompany()
        self.addDate()
        self.addDepartment()
        self.addNation()'''

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(1)
        # 外层网格


        gridinformation = QGridLayout()
        gridinformation.setSpacing(10)
        # 病人基本信息网格，行距1个字距

        title = QLabel('                                    电子病历', self)
        title.setFont(QFont("Microsoft YaHei", 18, QFont.Bold))
        # title.move(235, 15)
        gridinformation.addWidget(title, 0, 0)

        string = '  姓名： '
        name = QLabel(string, self)
        name.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(name, 1, 0)

        string = '工作单位: '
        company = QLabel(string, self)
        company.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(company, 1, 1)

        string = '  性别: '
        gender = QLabel(string, self)
        gender.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(gender, 2, 0)

        string = '住       址: 深圳市猛虎区建安路55号'
        address = QLabel(string, self)
        address.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(address, 2, 1)

        string = '  年龄: '
        age = QLabel(string, self)
        age.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(age, 3, 0)

        string = '科       室: '
        department = QLabel(string, self)
        department.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(department, 3, 1)

        string = '  民族: '
        nation = QLabel(string, self)
        nation.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(nation, 4, 0, )

        string = '日       期: '
        date = QLabel(string, self)
        date.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(date, 4, 1,)

        gridinformation2 = QGridLayout()
        gridinformation2.setSpacing(1)

        string = '  症       状: 面色苍白、四肢无力、头昏眼花、有时伴有轻微呕吐感'
        symptom = QLabel(string, self)
        symptom.setWordWrap(True)
        symptom.setFont(QFont("Microsoft YaHei", 11))
        gridinformation2.addWidget(symptom, 4, 0, 4, 2)

        string = '  病情结论: 患者具有低血糖症状,并伴随轻微的发烧'
        conclusion = QLabel(string, self)
        conclusion.setWordWrap(True)
        conclusion.setFont(QFont("Microsoft YaHei", 11))
        gridinformation2.addWidget(conclusion, 5, 0, 5, 2)
        # 病人基础信息网格布局

        gridsign = QGridLayout()
        gridsign.setSpacing(1)
        # 电子签名布局
        signframe = QFrame(self)
        signframe.setFrameShape(QFrame.StyledPanel)
        signframe.move(20, 420)
        signframe.resize(575, 180)
        #分隔框

        string = '          是否电子签名，若进行电子签名，病历便不能修改'
        signprompt = QLabel(string, self)
        signprompt.setFont(QFont("Microsoft YaHei", 11))
        gridsign.addWidget(signprompt, 0, 0)

        Syes = QCheckBox('是', self)
        gridsign.addWidget(Syes, 1, 1)
        #Syes.move(200, 434)
        #cb.stateChanged.connect(self.changeTitle)复选框被选中触发事件
        Sno = QCheckBox('否', self)
        #Sno.move(20, 20)
        gridsign.addWidget(Sno, 1, 2)

        Sign = QLabel('         电子签名：', self)
        Sign.setFont(QFont("Microsoft YaHei", 14, QFont.Bold))
        gridsign.addWidget(Sign, 2, 0)

        gridbutton = QGridLayout()
        gridbutton.setSpacing(1)
        okButton = QPushButton('提交')
        okButton.setFixedSize(60,30)
        #okButton.resize(okButton.sizeHint())
        gridbutton.addWidget(okButton, 0, 2)

        # button网格布局

        grid.addLayout(gridbutton, 3, 0)
        grid.addLayout(gridinformation, 0, 0)
        grid.addLayout(gridinformation2, 1, 0)
        grid.addLayout(gridsign, 2, 0)
        self.setLayout(grid)
        # 网格布局排列结束

        self.setGeometry(0, 0, 570, 650)
        self.center()
        # 窗口居中显示
        self.setWindowTitle('电子病历')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MedicalRecord()
    sys.exit(app.exec_())
