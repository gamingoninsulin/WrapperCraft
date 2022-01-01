from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WrapperCraft(object):
    def setupUi(self, WrapperCraft):
        WrapperCraft.setObjectName("WrapperCraft")
        WrapperCraft.resize(461, 371)
        WrapperCraft.setToolTip("")

        self.centralwidget = QtWidgets.QWidget(WrapperCraft)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 259, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(90, 50, 264, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ServerJar_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.label_ServerJar_4.setFont(font)
        self.label_ServerJar_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ServerJar_4.setObjectName("label_ServerJar_4")
        self.horizontalLayout_3.addWidget(self.label_ServerJar_4)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_ServerJar_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_ServerJar_3.setGeometry(QtCore.QRect(0, 0, 461, 41))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label_ServerJar_3.setFont(font)
        self.label_ServerJar_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ServerJar_3.setObjectName("label_ServerJar_3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 220, 231, 44))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_ServerJar_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.label_ServerJar_2.setFont(font)
        self.label_ServerJar_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ServerJar_2.setObjectName("label_ServerJar_2")
        self.horizontalLayout_4.addWidget(self.label_ServerJar_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 120, 343, 78))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ServerJar_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.label_ServerJar_5.setFont(font)
        self.label_ServerJar_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ServerJar_5.setObjectName("label_ServerJar_5")
        self.horizontalLayout.addWidget(self.label_ServerJar_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.ServerJar = QtWidgets.QLabel(self.horizontalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.ServerJar.setFont(font)
        self.ServerJar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ServerJar.setObjectName("ServerJar")
        self.horizontalLayout.addWidget(self.ServerJar)
        self.searchBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.searchBtn.setFont(font)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout.addWidget(self.deleteBtn)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 200, 81, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label_JVM = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.label_JVM.setFont(font)
        self.label_JVM.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_JVM.setObjectName("label_JVM")
        self.verticalLayout.addWidget(self.label_JVM)
        self.JavaARGS = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.JavaARGS.setFont(font)
        self.JavaARGS.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.JavaARGS.setObjectName("JavaARGS")
        self.verticalLayout.addWidget(self.JavaARGS)

        WrapperCraft.setCentralWidget(self.centralwidget)

        self.navbar = QtWidgets.QMenuBar(WrapperCraft)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 461, 21))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        
        self.navbar.setSizePolicy(sizePolicy)
        self.navbar.setObjectName("navbar")
        self.menuPlugins = QtWidgets.QMenu(self.navbar)
        self.menuPlugins.setObjectName("menuPlugins")
        self.menuServer_Options = QtWidgets.QMenu(self.navbar)
        self.menuServer_Options.setObjectName("menuServer_Options")
        self.menuServer_Moderation = QtWidgets.QMenu(self.navbar)
        self.menuServer_Moderation.setObjectName("menuServer_Moderation")
        self.menuConsole = QtWidgets.QMenu(self.navbar)
        self.menuConsole.setObjectName("menuConsole")

        WrapperCraft.setMenuBar(self.navbar)

        self.actionStart = QtGui.QAction(WrapperCraft)
        self.actionStart.setObjectName("actionStart")

        self.actionStop = QtGui.QAction(WrapperCraft)
        self.actionStop.setObjectName("actionStop")

        self.actionRestart = QtGui.QAction(WrapperCraft)
        self.actionRestart.setObjectName("actionRestart")

        self.actionKill = QtGui.QAction(WrapperCraft)
        self.actionKill.setObjectName("actionKill")

        self.MenuButton_Create_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Create_Server.setObjectName("MenuButton_Create_Server")

        self.MenuButton_Migrate_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Migrate_Server.setObjectName("MenuButton_Migrate_Server")

        self.MenuButton_Update_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Update_Server.setObjectName("MenuButton_Update_Server")

        self.MenuButton_Ban_IP = QtGui.QAction(WrapperCraft)
        self.MenuButton_Ban_IP.setObjectName("MenuButton_Ban_IP")

        self.MenuButton_Ban_Players = QtGui.QAction(WrapperCraft)
        self.MenuButton_Ban_Players.setObjectName("MenuButton_Ban_Players")

        self.MenuButton_Whitelist = QtGui.QAction(WrapperCraft)
        self.MenuButton_Whitelist.setObjectName("MenuButton_Whitelist")

        self.MenuButton_OP = QtGui.QAction(WrapperCraft)
        self.MenuButton_OP.setObjectName("MenuButton_OP")

        self.MenuButton_Backups = QtGui.QAction(WrapperCraft)
        self.MenuButton_Backups.setObjectName("MenuButton_Backups")

        self.MenuButton_Console = QtGui.QAction(WrapperCraft)
        self.MenuButton_Console.setObjectName("MenuButton_Console")

        self.menuServer_Options.addAction(self.MenuButton_Create_Server)
        self.menuServer_Options.addAction(self.MenuButton_Migrate_Server)
        self.menuServer_Moderation.addAction(self.MenuButton_Ban_IP)
        self.menuServer_Moderation.addAction(self.MenuButton_Ban_Players)
        self.menuServer_Moderation.addSeparator()
        self.menuServer_Moderation.addAction(self.MenuButton_Whitelist)
        self.menuServer_Moderation.addAction(self.MenuButton_OP)
        self.navbar.addAction(self.menuConsole.menuAction())
        self.navbar.addAction(self.menuPlugins.menuAction())
        self.navbar.addAction(self.menuServer_Options.menuAction())
        self.navbar.addAction(self.menuServer_Moderation.menuAction())

        self.retranslateUi(WrapperCraft)
        QtCore.QMetaObject.connectSlotsByName(WrapperCraft)

    def retranslateUi(self, WrapperCraft):
        _translate = QtCore.QCoreApplication.translate

        WrapperCraft.setWindowTitle(_translate("WrapperCraft", "Wrapper Craft"))

        self.pushButton.setText(_translate("WrapperCraft", "CREATE!"))
        self.label_ServerJar_4.setText(_translate("WrapperCraft", "Server Name:"))
        self.lineEdit.setText(_translate("WrapperCraft", "Minecraft Server"))
        self.label_ServerJar_3.setText(_translate("WrapperCraft", "Creating New Server"))
        self.label_ServerJar_2.setText(_translate("WrapperCraft", "Accept EULA:"))
        self.comboBox.setItemText(0, _translate("WrapperCraft", "True"))
        self.comboBox.setItemText(1, _translate("WrapperCraft", "False"))
        self.label_ServerJar_5.setText(_translate("WrapperCraft", "Choose Server Jar:"))
        self.ServerJar.setText(_translate("WrapperCraft", "server.jar"))
        self.searchBtn.setText(_translate("WrapperCraft", "Search"))
        self.deleteBtn.setText(_translate("WrapperCraft", "Delete"))
        self.label_JVM.setText(_translate("WrapperCraft", "RAM"))
        self.JavaARGS.setText(_translate("WrapperCraft", "1G"))

        self.menuPlugins.setTitle(_translate("WrapperCraft", "Plugins"))
        self.menuServer_Options.setTitle(_translate("WrapperCraft", "Server Options"))
        self.menuServer_Moderation.setTitle(_translate("WrapperCraft", "Server Moderation"))
        self.menuConsole.setTitle(_translate("WrapperCraft", "Console"))

        self.actionStart.setText(_translate("WrapperCraft", "Start"))
        self.actionStop.setText(_translate("WrapperCraft", "Stop"))
        self.actionRestart.setText(_translate("WrapperCraft", "Restart"))
        self.actionKill.setText(_translate("WrapperCraft", "Kill"))

        self.MenuButton_Create_Server.setText(_translate("WrapperCraft", "Create Server"))
        self.MenuButton_Migrate_Server.setText(_translate("WrapperCraft", "Migrate Server"))

        self.MenuButton_Ban_IP.setText(_translate("WrapperCraft", "Ban IP"))
        self.MenuButton_Ban_Players.setText(_translate("WrapperCraft", "Ban Players"))
        self.MenuButton_Whitelist.setText(_translate("WrapperCraft", "Whitelist"))
        self.MenuButton_OP.setText(_translate("WrapperCraft", "OP"))


    def press_btn():
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WrapperCraft = QtWidgets.QMainWindow()
    ui = Ui_WrapperCraft()
    ui.setupUi(WrapperCraft)
    WrapperCraft.show()
    sys.exit(app.exec())
