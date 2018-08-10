# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\QtSkin\UiFiles\LoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(320, 410)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LoginDialog)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialogWidgetBg = QtWidgets.QWidget(LoginDialog)
        self.dialogWidgetBg.setMinimumSize(QtCore.QSize(310, 400))
        self.dialogWidgetBg.setMaximumSize(QtCore.QSize(310, 400))
        self.dialogWidgetBg.setProperty("active", True)
        self.dialogWidgetBg.setObjectName("dialogWidgetBg")
        self.gridLayout = QtWidgets.QGridLayout(self.dialogWidgetBg)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(93, 101, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(160, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(160, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        self.labelHead = QtWidgets.QLabel(self.dialogWidgetBg)
        self.labelHead.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHead.setObjectName("labelHead")
        self.gridLayout.addWidget(self.labelHead, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(92, 101, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.loginWidgetEdit = QtWidgets.QWidget(self.dialogWidgetBg)
        self.loginWidgetEdit.setObjectName("loginWidgetEdit")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.loginWidgetEdit)
        self.verticalLayout.setContentsMargins(25, 0, 25, 0)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editUsername = QtWidgets.QLineEdit(self.loginWidgetEdit)
        self.editUsername.setMinimumSize(QtCore.QSize(0, 30))
        self.editUsername.setMaximumSize(QtCore.QSize(16777215, 30))
        self.editUsername.setClearButtonEnabled(True)
        self.editUsername.setObjectName("editUsername")
        self.verticalLayout.addWidget(self.editUsername)
        self.editPassword = QtWidgets.QLineEdit(self.loginWidgetEdit)
        self.editPassword.setMinimumSize(QtCore.QSize(0, 30))
        self.editPassword.setMaximumSize(QtCore.QSize(16777215, 30))
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.verticalLayout.addWidget(self.editPassword)
        self.labelNotice = QtWidgets.QLabel(self.loginWidgetEdit)
        self.labelNotice.setText("")
        self.labelNotice.setObjectName("labelNotice")
        self.verticalLayout.addWidget(self.labelNotice)
        self.buttonLogin = QtWidgets.QPushButton(self.loginWidgetEdit)
        self.buttonLogin.setMinimumSize(QtCore.QSize(0, 36))
        self.buttonLogin.setMaximumSize(QtCore.QSize(16777215, 36))
        self.buttonLogin.setObjectName("buttonLogin")
        self.verticalLayout.addWidget(self.buttonLogin)
        self.gridLayout.addWidget(self.loginWidgetEdit, 4, 0, 1, 3)
        self.widgetTitle = BaseTitleWidget(self.dialogWidgetBg)
        self.widgetTitle.setMinimumSize(QtCore.QSize(0, 28))
        self.widgetTitle.setMaximumSize(QtCore.QSize(16777215, 28))
        self.widgetTitle.setObjectName("widgetTitle")
        self.gridLayout.addWidget(self.widgetTitle, 0, 0, 1, 3)
        self.loginWidgetBottom = QtWidgets.QWidget(self.dialogWidgetBg)
        self.loginWidgetBottom.setMinimumSize(QtCore.QSize(0, 54))
        self.loginWidgetBottom.setObjectName("loginWidgetBottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loginWidgetBottom)
        self.horizontalLayout_2.setContentsMargins(28, 0, 28, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelRegister = QtWidgets.QLabel(self.loginWidgetBottom)
        self.labelRegister.setOpenExternalLinks(True)
        self.labelRegister.setObjectName("labelRegister")
        self.horizontalLayout_2.addWidget(self.labelRegister)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.labelForgot = QtWidgets.QLabel(self.loginWidgetBottom)
        self.labelForgot.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelForgot.setOpenExternalLinks(True)
        self.labelForgot.setObjectName("labelForgot")
        self.horizontalLayout_2.addWidget(self.labelForgot)
        self.gridLayout.addWidget(self.loginWidgetBottom, 6, 0, 1, 3)
        self.horizontalLayout.addWidget(self.dialogWidgetBg)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.labelHead.setText(_translate("LoginDialog", ""))
        self.editUsername.setPlaceholderText(_translate("LoginDialog", "Github账号"))
        self.editPassword.setPlaceholderText(_translate("LoginDialog", "密码"))
        self.buttonLogin.setText(_translate("LoginDialog", "登录"))
        self.labelRegister.setText(_translate("LoginDialog", "<html><head/><body><p><a href=\"https://github.com/join?source=login\"><span style=\" text-decoration: none; color:#24afff;\">立即注册</span></a></p></body></html>"))
        self.labelForgot.setText(_translate("LoginDialog", "<html><head/><body><p><a href=\"https://github.com/password_reset\"><span style=\" text-decoration: none; color:#787878;\">忘记密码?</span></a></p></body></html>"))

from Widgets.BaseTitleWidget import BaseTitleWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())

