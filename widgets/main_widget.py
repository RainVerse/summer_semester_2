from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication
from sql.sql_functions import get_user_name_by_id


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        self.exit_button = QtWidgets.QPushButton(main_window)
        self.exit_button.setGeometry(QtCore.QRect(360, 310, 101, 31))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(QCoreApplication.instance().quit)
        self.welcome_label = QtWidgets.QLabel(main_window)
        self.welcome_label.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.welcome_label.setTextFormat(QtCore.Qt.RichText)
        self.welcome_label.setObjectName("welcome_label")
        self.tabWidget = QtWidgets.QTabWidget(main_window)
        self.tabWidget.setGeometry(QtCore.QRect(40, 70, 381, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.add_record = QtWidgets.QWidget()
        self.add_record.setObjectName("add_record")
        self.add_button = QtWidgets.QPushButton(self.add_record)
        self.add_button.setGeometry(QtCore.QRect(70, 60, 241, 41))
        self.add_button.setObjectName("add_button")
        self.tabWidget.addTab(self.add_record, "")
        self.search_record = QtWidgets.QWidget()
        self.search_record.setObjectName("search_record")
        self.name_input_edit = QtWidgets.QLineEdit(self.search_record)
        self.name_input_edit.setGeometry(QtCore.QRect(50, 40, 271, 41))
        self.name_input_edit.setClearButtonEnabled(False)
        self.name_input_edit.setObjectName("name_input_edit")
        self.search_button = QtWidgets.QPushButton(self.search_record)
        self.search_button.setGeometry(QtCore.QRect(70, 100, 241, 41))
        self.search_button.setObjectName("search_button")
        self.tabWidget.addTab(self.search_record, "")

        self.retranslateUi(main_window)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "电子病历防篡改存档演示"))
        self.exit_button.setText(_translate("main_window", "退出系统"))
        self.welcome_label.setText(_translate("main_window", "欢迎您，"))
        self.add_button.setText(_translate("main_window", "添加一份新的病历"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_record), _translate("main_window", "添加病历"))
        self.name_input_edit.setPlaceholderText(_translate("main_window", "输入病人名字"))
        self.search_button.setText(_translate("main_window", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_record), _translate("main_window", "查找病历"))


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.resize(480, 400)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

    def get_search_info(self):
        return self.ui.name_input_edit.text()

    def search_fail_message(self):
        QtWidgets.QMessageBox.information(self, "警告", "没有找到对应病人信息",QtWidgets.QMessageBox.Yes)

    def set_user_id(self, user_id):
        self.user_id = user_id
        self.ui.welcome_label.setText(self.ui.welcome_label.text() + get_user_name_by_id(self.user_id))
