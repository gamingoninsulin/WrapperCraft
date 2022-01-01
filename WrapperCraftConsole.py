from PyQt6 import QtCore, QtGui, QtWidgets
import WrapperCraftCreateServer

class Ui_WrapperCraft(object):
    def setupUi(self, WrapperCraft):
        WrapperCraft.setObjectName("WrapperCraft")
        WrapperCraft.resize(1000, 680)
        WrapperCraft.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(WrapperCraft)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(740, 30, 20, 541))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 30, 701, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 570, 721, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.SendBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SendBtn.setObjectName("SendBtn")
        self.horizontalLayout.addWidget(self.SendBtn)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(770, 30, 181, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.startBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startBtn.setObjectName("startBtn")

        self.verticalLayout.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stopBtn.setObjectName("stopBtn")

        self.verticalLayout.addWidget(self.stopBtn)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        self.horizontalButtonLayout = QtWidgets.QHBoxLayout()
        self.horizontalButtonLayout.setObjectName("horizontalButtonLayout")

        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalButtonLayout.addWidget(self.line)

        self.killBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.killBtn.setObjectName("killBtn")
        self.horizontalButtonLayout.addWidget(self.killBtn)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalButtonLayout.addItem(spacerItem)

        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalButtonLayout.addWidget(self.line_3)

        self.restartBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.restartBtn.setObjectName("restartBtn")
        self.horizontalButtonLayout.addWidget(self.restartBtn)

        self.verticalLayout.addLayout(self.horizontalButtonLayout)
        WrapperCraft.setCentralWidget(self.centralwidget)

        self.navbar = QtWidgets.QMenuBar(WrapperCraft)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 1000, 21))

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

        self.MenuButton_Ban_IP = QtGui.QAction(WrapperCraft)
        self.MenuButton_Ban_IP.setObjectName("MenuButton_Ban_IP")

        self.MenuButton_Ban_Players = QtGui.QAction(WrapperCraft)
        self.MenuButton_Ban_Players.setObjectName("MenuButton_Ban_Players")

        self.MenuButton_Whitelist = QtGui.QAction(WrapperCraft)
        self.MenuButton_Whitelist.setObjectName("MenuButton_Whitelist")

        self.MenuButton_OP = QtGui.QAction(WrapperCraft)
        self.MenuButton_OP.setObjectName("MenuButton_OP")
        
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

        self.SendBtn.setText(_translate("WrapperCraft", "Send"))
        self.startBtn.setText(_translate("WrapperCraft", "Start"))
        self.stopBtn.setText(_translate("WrapperCraft", "Stop"))
        self.killBtn.setText(_translate("WrapperCraft", "Kill"))
        self.restartBtn.setText(_translate("WrapperCraft", "Restart"))

        self.menuPlugins.setTitle(_translate("WrapperCraft", "Plugins"))
        self.menuServer_Options.setTitle(_translate("WrapperCraft", "Server Options"))
        self.menuServer_Moderation.setTitle(_translate("WrapperCraft", "Server Moderation"))
        self.menuConsole.setTitle(_translate("WrapperCraft", "Console"))

        self.actionStart.setText(_translate("WrapperCraft", "Start"))
        self.actionStop.setText(_translate("WrapperCraft", "Stop"))
        self.actionRestart.setText(_translate("WrapperCraft", "Restart"))
        self.actionKill.setText(_translate("WrapperCraft", "Kill"))

        self.MenuButton_OP.setText(_translate("WrapperCraft", "OP"))
        self.MenuButton_Whitelist.setText(_translate("WrapperCraft", "Whitelist"))
        self.MenuButton_Ban_Players.setText(_translate("WrapperCraft", "Ban Players"))
        self.MenuButton_Ban_IP.setText(_translate("WrapperCraft", "Ban IP"))

        self.MenuButton_Migrate_Server.setText(_translate("WrapperCraft", "Migrate Server"))
        self.MenuButton_Create_Server.setText(_translate("WrapperCraft", "Create Server"))

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
