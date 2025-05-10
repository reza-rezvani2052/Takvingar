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
        self.actHelp = QAction(MainWindow)
        self.actHelp.setObjectName(u"actHelp")
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
        self.actBckup = QAction(MainWindow)
        self.actBckup.setObjectName(u"actBckup")
        icon4 = QIcon()
        icon4.addFile(u":/img/backup.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actBckup.setIcon(icon4)
        self.actRestoreBackup = QAction(MainWindow)
        self.actRestoreBackup.setObjectName(u"actRestoreBackup")
        icon5 = QIcon()
        icon5.addFile(u":/img/restore.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actRestoreBackup.setIcon(icon5)
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
        self.menubar.setGeometry(QRect(0, 0, 926, 25))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menulndvdj = QMenu(self.menubar)
        self.menulndvdj.setObjectName(u"menulndvdj")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menulndvdj.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actRestoreBackup)
        self.menu.addAction(self.actBckup)
        self.menu.addSeparator()
        self.menu.addAction(self.actQuit)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.actHelp)
        self.menu_3.addAction(self.actAbout)
        self.menulndvdj.addAction(self.action_5)
        self.menulndvdj.addAction(self.action_7)
        self.menulndvdj.addAction(self.action_8)

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
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0633\u062a\u0646", None))
#if QT_CONFIG(shortcut)
        self.actQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0627\u0633\u0628\u0647 \u06a9\u0627\u0631\u0645\u0632\u062f", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06a9\u062a\u0648\u0631 \u0646\u0648\u06cc\u0633", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u0648\u0698\u0647\u200c\u0647\u0627", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u0633\u0646\u0644", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0647\u0627\u0645\u062f\u0627\u0631\u0627\u0646", None))
        self.actBckup.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0647\u06cc\u0647 \u0646\u0633\u062e\u0647 \u067e\u0634\u062a\u06cc\u0628\u0627\u0646", None))
#if QT_CONFIG(shortcut)
        self.actBckup.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+B", None))
#endif // QT_CONFIG(shortcut)
        self.actRestoreBackup.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06cc\u0627\u0628\u06cc \u0646\u0633\u062e\u0647 \u067e\u0634\u062a\u06cc\u0628\u0627\u0646", None))
#if QT_CONFIG(shortcut)
        self.actRestoreBackup.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06cc\u0644", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0628\u0632\u0627\u0631\u0647\u0627", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0631\u0627\u0647\u0646\u0645\u0627", None))
        self.menulndvdj.setTitle(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

