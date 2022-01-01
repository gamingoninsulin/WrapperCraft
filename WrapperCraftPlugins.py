from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WrapperCraft(object):
    def setupUi(self, WrapperCraft):
        WrapperCraft.setObjectName("WrapperCraft")
        WrapperCraft.resize(400, 600)
        WrapperCraft.setToolTip("")

        self.centralwidget = QtWidgets.QWidget(WrapperCraft)
        self.centralwidget.setObjectName("centralwidget")
        self.PluginView = QtWidgets.QTableView(self.centralwidget)
        self.PluginView.setGeometry(QtCore.QRect(60, 20, 261, 511))
        self.PluginView.setObjectName("PluginView")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(320, 20, 20, 511))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 530, 160, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout.addWidget(self.deleteBtn)

        WrapperCraft.setCentralWidget(self.centralwidget)

        self.navbar = QtWidgets.QMenuBar(WrapperCraft)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 396, 21))

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

        self.MenuButton_AddPlugin = QtGui.QAction(WrapperCraft)
        self.MenuButton_AddPlugin.setObjectName("MenuButton_AddPlugin")
        self.MenuButton_Remove_Plugin = QtGui.QAction(WrapperCraft)
        self.MenuButton_Remove_Plugin.setObjectName("MenuButton_Remove_Plugin")
        self.MenuButton_Config_Editor = QtGui.QAction(WrapperCraft)
        self.MenuButton_Config_Editor.setObjectName("MenuButton_Config_Editor")
        self.MenuButton_Log_Reader = QtGui.QAction(WrapperCraft)
        self.MenuButton_Log_Reader.setObjectName("MenuButton_Log_Reader")
        self.MenuButton_Purge_Logs = QtGui.QAction(WrapperCraft)
        self.MenuButton_Purge_Logs.setObjectName("MenuButton_Purge_Logs")
        self.MenuButton_Create_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Create_Server.setObjectName("MenuButton_Create_Server")
        self.MenuButton_Migrate_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Migrate_Server.setObjectName("MenuButton_Migrate_Server")
        self.MenuButton_Update_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Update_Server.setObjectName("MenuButton_Update_Server")
        self.MenuButton_Clone_Server = QtGui.QAction(WrapperCraft)
        self.MenuButton_Clone_Server.setObjectName("MenuButton_Clone_Server")
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

        self.searchBtn.setText(_translate("WrapperCraft", "Search"))
        self.deleteBtn.setText(_translate("WrapperCraft", "Delete"))
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
        self.MenuButton_Console.setText(_translate("WrapperCraft", "Console"))


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
