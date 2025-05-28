# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGridLayout, QMainWindow,
    QMdiArea, QMenu, QMenuBar, QSizePolicy,
    QStackedWidget, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(926, 524)
        icon = QIcon()
        icon.addFile(u":/app-icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindow.setStyleSheet(u"QMenuBar{\n"
"     	background-color: lightgray; \n"
"       color: rgb(0, 0, 106);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"        padding: 4px 8px;\n"
"        border:1px solid transparent;\n"
"}\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"        background:  #a8a8a8; \n"
"        border:1px solid rgb(127, 127, 127);\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(190, 190, 190, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QMenuBar::item:pressed {\n"
"        border-color:rgb(127, 127, 127);\n"
"        border-style: solid;\n"
"        border-width:1px 1px 0 1px;\n"
"        /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,\n"
"                stop:0 rgba(255, 255, 255, 255),\n"
"                stop:1 rgba(190, 190, 190, 255));*/\n"
"        background-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"\n"
"/*---------------------------------*/\n"
"\n"
"QToolBar {\n"
"        border: 1px solid rgb(80,80,80);\n"
" "
                        "       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.485876 rgba(175, 175, 175, 255), stop:0.525424 rgba(140, 140, 140, 255), stop:1 rgba(150, 150, 150, 255));\n"
"        border-radius: 0px;\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    border:1px solid rgb(80,80,80);\n"
"        margin: 3px 5px 2px 5px;\n"
"        border-radius: 5px;\n"
"}\n"
"\n"
"/*---------------------------------*/\n"
"\n"
"QStatusBar {\n"
"        background-color: lightgray ;\n"
"        color: rgb(0, 0, 106);\n"
"}\n"
"\n"
"/*---------------------------------*/\n"
"")
        self.actHelp = QAction(MainWindow)
        self.actHelp.setObjectName(u"actHelp")
        self.actHelp.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/img/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actHelp.setIcon(icon1)
        self.actAbout = QAction(MainWindow)
        self.actAbout.setObjectName(u"actAbout")
        icon2 = QIcon()
        icon2.addFile(u":/img/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actAbout.setIcon(icon2)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        icon3 = QIcon()
        icon3.addFile(u":/img/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actQuit.setIcon(icon3)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.actBackup = QAction(MainWindow)
        self.actBackup.setObjectName(u"actBackup")
        icon4 = QIcon()
        icon4.addFile(u":/img/backup.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actBackup.setIcon(icon4)
        self.actRestoreBackup = QAction(MainWindow)
        self.actRestoreBackup.setObjectName(u"actRestoreBackup")
        icon5 = QIcon()
        icon5.addFile(u":/img/restore.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actRestoreBackup.setIcon(icon5)
        self.actRestartApp = QAction(MainWindow)
        self.actRestartApp.setObjectName(u"actRestartApp")
        icon6 = QIcon()
        icon6.addFile(u":/img/restart-app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actRestartApp.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetTopArea = QStackedWidget(self.centralwidget)
        self.stackedWidgetTopArea.setObjectName(u"stackedWidgetTopArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidgetTopArea.sizePolicy().hasHeightForWidth())
        self.stackedWidgetTopArea.setSizePolicy(sizePolicy)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.commandLinkButton_3 = QCommandLinkButton(self.page_2)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")
        sizePolicy.setHeightForWidth(self.commandLinkButton_3.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_3.setSizePolicy(sizePolicy)
        self.commandLinkButton_3.setIcon(icon2)

        self.gridLayout.addWidget(self.commandLinkButton_3, 0, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.page_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.commandLinkButton, 0, 2, 1, 1)

        self.commandLinkButton_2 = QCommandLinkButton(self.page_2)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        sizePolicy.setHeightForWidth(self.commandLinkButton_2.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.commandLinkButton_2, 0, 1, 1, 1)

        self.stackedWidgetTopArea.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidgetTopArea.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidgetTopArea)

        self.stackedWidgetMain = QStackedWidget(self.centralwidget)
        self.stackedWidgetMain.setObjectName(u"stackedWidgetMain")
        self.pageMdiArea = QWidget()
        self.pageMdiArea.setObjectName(u"pageMdiArea")
        self.gridLayout_2 = QGridLayout(self.pageMdiArea)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mdiArea = QMdiArea(self.pageMdiArea)
        self.mdiArea.setObjectName(u"mdiArea")

        self.gridLayout_2.addWidget(self.mdiArea, 0, 0, 1, 1)

        self.stackedWidgetMain.addWidget(self.pageMdiArea)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidgetMain.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidgetMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 30))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menulndvdj = QMenu(self.menubar)
        self.menulndvdj.setObjectName(u"menulndvdj")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menulndvdj.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actRestoreBackup)
        self.menu.addAction(self.actBackup)
        self.menu.addSeparator()
        self.menu.addAction(self.actRestartApp)
        self.menu.addAction(self.actQuit)
        self.menu.addSeparator()
        self.menu_2.addAction(self.action_4)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.actHelp)
        self.menu_3.addAction(self.actAbout)
        self.menulndvdj.addAction(self.action_5)
        self.menulndvdj.addAction(self.action_7)
        self.menulndvdj.addAction(self.action_8)
        self.toolBar.addAction(self.actBackup)
        self.toolBar.addAction(self.actRestoreBackup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actAbout)

        self.retranslateUi(MainWindow)

        self.stackedWidgetMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u062a\u06a9\u0648\u06cc\u0646\u06af\u0631", None))
        self.actHelp.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0627\u0647\u0646\u0645\u0627\u06cc \u0628\u0631\u0646\u0627\u0645\u0647", None))
#if QT_CONFIG(shortcut)
        self.actHelp.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actAbout.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628\u0627\u0631\u0647 \u0628\u0631\u0646\u0627\u0645\u0647", None))
#if QT_CONFIG(shortcut)
        self.actAbout.setShortcut(QCoreApplication.translate("MainWindow", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0633\u062a\u0646 \u0628\u0631\u0646\u0627\u0645\u0647", None))
#if QT_CONFIG(shortcut)
        self.actQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0627\u0633\u0628\u0647 \u06a9\u0627\u0631\u0645\u0632\u062f \u0628\u0627\u0646\u06a9", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06a9\u062a\u0648\u0631 \u0646\u0648\u06cc\u0633", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u0648\u0698\u0647\u200c\u0647\u0627", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u0633\u0646\u0644", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0647\u0627\u0645\u062f\u0627\u0631\u0627\u0646", None))
        self.actBackup.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0647\u06cc\u0647 \u0646\u0633\u062e\u0647 \u067e\u0634\u062a\u06cc\u0628\u0627\u0646", None))
#if QT_CONFIG(shortcut)
        self.actBackup.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+B", None))
#endif // QT_CONFIG(shortcut)
        self.actRestoreBackup.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06cc\u0627\u0628\u06cc \u0646\u0633\u062e\u0647 \u067e\u0634\u062a\u06cc\u0628\u0627\u0646", None))
#if QT_CONFIG(shortcut)
        self.actRestoreBackup.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.actRestartApp.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0627\u0647 \u0627\u0646\u062f\u0627\u0632\u06cc \u0645\u062c\u062f", None))
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06cc\u0644", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u0632\u0627\u0631\u0647\u0627", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0631\u0627\u0647\u0646\u0645\u0627", None))
        self.menulndvdj.setTitle(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634\u0627\u062a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

