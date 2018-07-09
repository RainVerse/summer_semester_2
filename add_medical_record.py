#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QPushButton, QVBoxLayout, QLabel,
                             QLineEdit, QGridLayout,QSplitter,
                             QFrame, QTextEdit,QComboBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class AddMedicalRecord(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

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
        nameEdit = QLineEdit()
        gridinformation.addWidget(nameEdit, 2, 1)
        str = nameEdit.text()

        string = '性       别：'
        gender = QLabel(string, self)
        gender.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(gender, 3, 0)
        namecombo = QComboBox(self)
        namecombo.addItem('男')
        namecombo.addItem('女')
        gridinformation.addWidget(namecombo, 3, 1)

        string = '年       龄：'
        age = QLabel(string, self)
        age.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(age, 4, 0)
        ageEdit = QLineEdit()
        gridinformation.addWidget(ageEdit, 4, 1)

        string = '民       族：'
        nation = QLabel(string, self)
        nation.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(nation, 5, 0, )
        nationEdit = QLineEdit()
        gridinformation.addWidget(nationEdit, 5, 1)

        string = '工作单位：'
        company = QLabel(string, self)
        company.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(company, 6, 0)
        companyEdit = QLineEdit()
        gridinformation.addWidget(companyEdit, 6, 1)

        string = '住       址：'
        address = QLabel(string, self)
        address.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(address, 7, 0)
        addressEdit = QLineEdit()
        gridinformation.addWidget(addressEdit, 7, 1)

        string = '科       室：'
        department = QLabel(string, self)
        department.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(department,8, 0)
        gendercombo = QComboBox(self)
        gendercombo.addItem('内科')
        gendercombo.addItem('外科')
        gendercombo.addItem('急诊科')
        gridinformation.addWidget(gendercombo, 8, 1)


        string = '日       期：'
        date = QLabel(string, self)
        date.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(date, 9, 0)
        dateEdit = QLineEdit()
        gridinformation.addWidget(dateEdit, 9, 1)


        string = '症       状：'
        symptom = QLabel(string, self)
        symptom.setWordWrap(True)
        symptom.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(symptom, 10, 0)
        symptomEdit = QTextEdit()
        gridinformation.addWidget(symptomEdit, 10, 1, 2, 1)

        string = '病情结论：'
        conclusion = QLabel(string, self)
        conclusion.setWordWrap(True)
        conclusion.setFont(QFont("Microsoft YaHei", 11))
        gridinformation.addWidget(conclusion, 13, 0)
        # 病人基础信息网格布局
        conclusionEdit = QTextEdit()
        gridinformation.addWidget(conclusionEdit, 14, 1, 2, 1)


        addButton = QPushButton('添加',self)
        addButton.setFixedSize(60,30)
        addButton.clicked.connect(self.printstr)
        gridinformation.addWidget(addButton, 16, 1)

        self.setLayout(gridinformation)
        # 网格布局排列结束

        self.setGeometry(0, 0, 500, 650)
        self.setFixedSize(500,650)
        self.center()
        # 窗口居中显示
        self.setWindowTitle('添加电子病历')
        self.show()

    def printstr(self):
        print("button")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    AMR = AddMedicalRecord()
    sys.exit(app.exec_())
