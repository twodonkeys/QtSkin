# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\QtSkin\UiFiles\DesignerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DesignerWidget(object):
    def setupUi(self, DesignerWidget):
        DesignerWidget.setObjectName("DesignerWidget")
        DesignerWidget.resize(766, 617)
        self.verticalLayout = QtWidgets.QVBoxLayout(DesignerWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetNavbar = QtWidgets.QWidget(DesignerWidget)
        self.widgetNavbar.setMinimumSize(QtCore.QSize(0, 40))
        self.widgetNavbar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widgetNavbar.setObjectName("widgetNavbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetNavbar)
        self.horizontalLayout_2.setContentsMargins(12, 6, 12, 6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonMyProject = QtWidgets.QPushButton(self.widgetNavbar)
        self.buttonMyProject.setMinimumSize(QtCore.QSize(0, 28))
        self.buttonMyProject.setMaximumSize(QtCore.QSize(16777215, 28))
        self.buttonMyProject.setObjectName("buttonMyProject")
        self.horizontalLayout_2.addWidget(self.buttonMyProject)
        self.buttonCurrentProject = QtWidgets.QPushButton(self.widgetNavbar)
        self.buttonCurrentProject.setMinimumSize(QtCore.QSize(0, 28))
        self.buttonCurrentProject.setMaximumSize(QtCore.QSize(16777215, 28))
        self.buttonCurrentProject.setObjectName("buttonCurrentProject")
        self.horizontalLayout_2.addWidget(self.buttonCurrentProject)
        self.vLine = QtWidgets.QFrame(self.widgetNavbar)
        self.vLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.vLine.setObjectName("vLine")
        self.horizontalLayout_2.addWidget(self.vLine)
        self.labelCurrentProject = QtWidgets.QLabel(self.widgetNavbar)
        self.labelCurrentProject.setText("")
        self.labelCurrentProject.setObjectName("labelCurrentProject")
        self.horizontalLayout_2.addWidget(self.labelCurrentProject)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonAddFile = QtWidgets.QPushButton(self.widgetNavbar)
        self.buttonAddFile.setMinimumSize(QtCore.QSize(70, 28))
        self.buttonAddFile.setMaximumSize(QtCore.QSize(16777215, 28))
        self.buttonAddFile.setObjectName("buttonAddFile")
        self.horizontalLayout_2.addWidget(self.buttonAddFile)
        self.verticalLayout.addWidget(self.widgetNavbar)
        self.splitter = QtWidgets.QSplitter(DesignerWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widgetWorkspace = QtWidgets.QWidget(self.splitter)
        self.widgetWorkspace.setObjectName("widgetWorkspace")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetWorkspace)
        self.horizontalLayout.setContentsMargins(0, 15, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.listViewFiles = QtWidgets.QListView(self.widgetWorkspace)
        self.listViewFiles.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listViewFiles.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listViewFiles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewFiles.setTabKeyNavigation(True)
        self.listViewFiles.setFlow(QtWidgets.QListView.LeftToRight)
        self.listViewFiles.setProperty("isWrapping", True)
        self.listViewFiles.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewFiles.setWordWrap(True)
        self.listViewFiles.setSelectionRectVisible(True)
        self.listViewFiles.setObjectName("listViewFiles")
        self.horizontalLayout.addWidget(self.listViewFiles)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.rightScrollBar = QtWidgets.QScrollBar(self.widgetWorkspace)
        self.rightScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.rightScrollBar.setObjectName("rightScrollBar")
        self.horizontalLayout.addWidget(self.rightScrollBar)
        self.toolWidget = QtWidgets.QStackedWidget(self.splitter)
        self.toolWidget.setMinimumSize(QtCore.QSize(160, 0))
        self.toolWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.toolWidget.setObjectName("toolWidget")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(DesignerWidget)
        QtCore.QMetaObject.connectSlotsByName(DesignerWidget)

    def retranslateUi(self, DesignerWidget):
        _translate = QtCore.QCoreApplication.translate
        DesignerWidget.setWindowTitle(_translate("DesignerWidget", "Designer Widget"))
        self.buttonMyProject.setText(_translate("DesignerWidget", " My Project"))
        self.buttonCurrentProject.setText(_translate("DesignerWidget", ""))
        self.buttonAddFile.setText(_translate("DesignerWidget", " Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DesignerWidget = QtWidgets.QWidget()
    ui = Ui_DesignerWidget()
    ui.setupUi(DesignerWidget)
    DesignerWidget.show()
    sys.exit(app.exec_())

