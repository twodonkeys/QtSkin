# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\QtSkin\UiFiles\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 605)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.centralwidget = QtWidgets.QStackedWidget(self.widget)
        self.centralwidget.setObjectName("centralwidget")
        self.widgetHome = QtWidgets.QWidget()
        self.widgetHome.setObjectName("widgetHome")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetHome)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetNavbar = QtWidgets.QWidget(self.widgetHome)
        self.widgetNavbar.setMinimumSize(QtCore.QSize(0, 40))
        self.widgetNavbar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widgetNavbar.setObjectName("widgetNavbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetNavbar)
        self.horizontalLayout_2.setContentsMargins(12, 6, 12, 6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelMyProject = QtWidgets.QLabel(self.widgetNavbar)
        self.labelMyProject.setObjectName("labelMyProject")
        self.horizontalLayout_2.addWidget(self.labelMyProject)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonAddProject = QtWidgets.QPushButton(self.widgetNavbar)
        self.buttonAddProject.setMinimumSize(QtCore.QSize(120, 28))
        self.buttonAddProject.setMaximumSize(QtCore.QSize(16777215, 28))
        self.buttonAddProject.setObjectName("buttonAddProject")
        self.horizontalLayout_2.addWidget(self.buttonAddProject)
        self.verticalLayout.addWidget(self.widgetNavbar)
        self.widgetProjectCount = QtWidgets.QWidget(self.widgetHome)
        self.widgetProjectCount.setMinimumSize(QtCore.QSize(0, 36))
        self.widgetProjectCount.setMaximumSize(QtCore.QSize(16777215, 36))
        self.widgetProjectCount.setObjectName("widgetProjectCount")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetProjectCount)
        self.horizontalLayout_3.setContentsMargins(15, 1, 15, 1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelProjectCount = QtWidgets.QLabel(self.widgetProjectCount)
        self.labelProjectCount.setObjectName("labelProjectCount")
        self.horizontalLayout_3.addWidget(self.labelProjectCount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonSortTime = QtWidgets.QPushButton(self.widgetProjectCount)
        self.buttonSortTime.setMinimumSize(QtCore.QSize(34, 34))
        self.buttonSortTime.setMaximumSize(QtCore.QSize(34, 34))
        self.buttonSortTime.setCheckable(True)
        self.buttonSortTime.setChecked(True)
        self.buttonSortTime.setObjectName("buttonSortTime")
        self.horizontalLayout_3.addWidget(self.buttonSortTime)
        self.buttonSortAz = QtWidgets.QPushButton(self.widgetProjectCount)
        self.buttonSortAz.setMinimumSize(QtCore.QSize(34, 34))
        self.buttonSortAz.setMaximumSize(QtCore.QSize(34, 34))
        self.buttonSortAz.setCheckable(True)
        self.buttonSortAz.setObjectName("buttonSortAz")
        self.horizontalLayout_3.addWidget(self.buttonSortAz)
        self.verticalLayout.addWidget(self.widgetProjectCount)
        self.widgetWorkspace = QtWidgets.QWidget(self.widgetHome)
        self.widgetWorkspace.setObjectName("widgetWorkspace")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetWorkspace)
        self.horizontalLayout.setContentsMargins(0, 15, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.listViewProjects = QtWidgets.QListView(self.widgetWorkspace)
        self.listViewProjects.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listViewProjects.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listViewProjects.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewProjects.setTabKeyNavigation(True)
        self.listViewProjects.setFlow(QtWidgets.QListView.LeftToRight)
        self.listViewProjects.setProperty("isWrapping", True)
        self.listViewProjects.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewProjects.setWordWrap(True)
        self.listViewProjects.setSelectionRectVisible(True)
        self.listViewProjects.setObjectName("listViewProjects")
        self.horizontalLayout.addWidget(self.listViewProjects)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.rightScrollBar = QtWidgets.QScrollBar(self.widgetWorkspace)
        self.rightScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.rightScrollBar.setObjectName("rightScrollBar")
        self.horizontalLayout.addWidget(self.rightScrollBar)
        self.verticalLayout.addWidget(self.widgetWorkspace)
        self.centralwidget.addWidget(self.widgetHome)
        self.verticalLayout_2.addWidget(self.centralwidget)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 2))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 2))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(0, 25))
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionWebsite = QtWidgets.QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.actionFeedback = QtWidgets.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSaveas = QtWidgets.QAction(MainWindow)
        self.actionSaveas.setObjectName("actionSaveas")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setObjectName("action_14")
        self.actionAboutQt = QtWidgets.QAction(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSaveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_14)
        self.menu_2.addAction(self.actionWebsite)
        self.menu_2.addAction(self.actionFeedback)
        self.menu_2.addAction(self.actionUpdate)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionAbout)
        self.menu_2.addAction(self.actionAboutQt)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.centralwidget.setCurrentIndex(0)
        self.actionNew.triggered.connect(self.buttonAddProject.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qt Skin Designer"))
        self.labelMyProject.setText(_translate("MainWindow", "My Project"))
        self.buttonAddProject.setText(_translate("MainWindow", " Create Project"))
        self.labelProjectCount.setText(_translate("MainWindow", "0 Project"))
        self.buttonSortTime.setText(_translate("MainWindow", ""))
        self.buttonSortAz.setText(_translate("MainWindow", ""))
        self.menu.setTitle(_translate("MainWindow", "Project"))
        self.menu_2.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New Project"))
        self.actionNew.setIconText(_translate("MainWindow", "New Project"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create New Project"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open Project"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open Exists Project"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save Project"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save Project"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionWebsite.setText(_translate("MainWindow", "Website"))
        self.actionWebsite.setStatusTip(_translate("MainWindow", "Welcome to visit http://PyQt5.com"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionUpdate.setStatusTip(_translate("MainWindow", "Check Update"))
        self.action_7.setText(_translate("MainWindow", "Faq"))
        self.action_7.setStatusTip(_translate("MainWindow", "Common problem"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionFeedback.setStatusTip(_translate("MainWindow", "ヾ(=ﾟ･ﾟ=)ﾉ♪Submit Feedback"))
        self.actionAbout.setText(_translate("MainWindow", "About Soft"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About the Software"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionSaveas.setText(_translate("MainWindow", "Save As Project"))
        self.actionSaveas.setStatusTip(_translate("MainWindow", "Save As Project"))
        self.actionSaveas.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_14.setText(_translate("MainWindow", "Exit"))
        self.action_14.setStatusTip(_translate("MainWindow", "Exit"))
        self.action_14.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAboutQt.setText(_translate("MainWindow", "About Qt"))
        self.actionAboutQt.setStatusTip(_translate("MainWindow", "About Qt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

