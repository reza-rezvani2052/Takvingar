# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialoglogin.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        if not DialogLogin.objectName():
            DialogLogin.setObjectName(u"DialogLogin")
        DialogLogin.resize(325, 442)
        icon = QIcon()
        icon.addFile(u":/app-icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        DialogLogin.setWindowIcon(icon)
        DialogLogin.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        DialogLogin.setStyleSheet(u"/* ------------------------------------- */\n"
"#frameMain{\n"
"border: 3px solid gray;\n"
"}\n"
"/* ------------------------------------- */\n"
"QLabel {\n"
"font-weight: bold;\n"
"/*font-size: 15px;*/\n"
"}\n"
"/* ------------------------------------- */\n"
"QLineEdit, QComboBox {\n"
"padding: 3px;\n"
"border: 1px solid gray;\n"
"border-radius: 2px;\n"
"font-weight: bold;\n"
"/*font-size: 15px;*/\n"
"}\n"
"/* ------------------------------------- */\n"
"QPushButton{\n"
"color: #111;\n"
"border: 2px solid #555;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"min-width: 80px;\n"
"min-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, st"
                        "op: 1 #888);\n"
"}\n"
"\n"
"/* ------------------------------------- */\n"
"\n"
"QToolButton{\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.gridLayout_5 = QGridLayout(DialogLogin)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frameMain = QFrame(DialogLogin)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameMain.setFrameShadow(QFrame.Shadow.Raised)
        self._2 = QVBoxLayout(self.frameMain)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(11, 11, -1, -1)
        self.stackedWidgetMain = QStackedWidget(self.frameMain)
        self.stackedWidgetMain.setObjectName(u"stackedWidgetMain")
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        self.gridLayout_3 = QGridLayout(self.pageLogin)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lblLogoUser = QLabel(self.pageLogin)
        self.lblLogoUser.setObjectName(u"lblLogoUser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogoUser.sizePolicy().hasHeightForWidth())
        self.lblLogoUser.setSizePolicy(sizePolicy)
        self.lblLogoUser.setPixmap(QPixmap(u":/user-login.png"))
        self.lblLogoUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogoUser.setWordWrap(True)

        self.gridLayout_3.addWidget(self.lblLogoUser, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ledPassword = QLineEdit(self.pageLogin)
        self.ledPassword.setObjectName(u"ledPassword")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ledPassword.sizePolicy().hasHeightForWidth())
        self.ledPassword.setSizePolicy(sizePolicy1)
        self.ledPassword.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.ledPassword.setAcceptDrops(False)
        self.ledPassword.setMaxLength(12)
        self.ledPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.ledPassword, 1, 1, 1, 1)

        self.ledUsername = QLineEdit(self.pageLogin)
        self.ledUsername.setObjectName(u"ledUsername")
        self.ledUsername.setMaxLength(15)

        self.gridLayout.addWidget(self.ledUsername, 0, 1, 1, 1)

        self.lblUserName = QLabel(self.pageLogin)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setMaximumSize(QSize(131, 16777215))

        self.gridLayout.addWidget(self.lblUserName, 0, 0, 1, 1)

        self.lblPassword = QLabel(self.pageLogin)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setMaximumSize(QSize(131, 16777215))

        self.gridLayout.addWidget(self.lblPassword, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.Space1 = QWidget(self.pageLogin)
        self.Space1.setObjectName(u"Space1")
        self.Space1.setMinimumSize(QSize(0, 5))

        self.gridLayout_3.addWidget(self.Space1, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnPasswordHint = QToolButton(self.pageLogin)
        self.btnPasswordHint.setObjectName(u"btnPasswordHint")
        icon1 = QIcon()
        icon1.addFile(u":/img/reset-password.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPasswordHint.setIcon(icon1)
        self.btnPasswordHint.setIconSize(QSize(30, 30))
        self.btnPasswordHint.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.btnPasswordHint)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnLogIn = QPushButton(self.pageLogin)
        self.btnLogIn.setObjectName(u"btnLogIn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnLogIn.sizePolicy().hasHeightForWidth())
        self.btnLogIn.setSizePolicy(sizePolicy2)
        self.btnLogIn.setMinimumSize(QSize(88, 38))
        self.btnLogIn.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.btnLogIn)

        self.btnClose = QPushButton(self.pageLogin)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy2.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy2)
        self.btnClose.setMinimumSize(QSize(88, 38))
        self.btnClose.setStyleSheet(u"")
        self.btnClose.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.btnClose)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.stackedWidgetMain.addWidget(self.pageLogin)
        self.pageRegistration = QWidget()
        self.pageRegistration.setObjectName(u"pageRegistration")
        self.gridLayout_2 = QGridLayout(self.pageRegistration)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblLogoUser_2 = QLabel(self.pageRegistration)
        self.lblLogoUser_2.setObjectName(u"lblLogoUser_2")
        sizePolicy.setHeightForWidth(self.lblLogoUser_2.sizePolicy().hasHeightForWidth())
        self.lblLogoUser_2.setSizePolicy(sizePolicy)
        self.lblLogoUser_2.setPixmap(QPixmap(u":/user-login.png"))
        self.lblLogoUser_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblLogoUser_2.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lblLogoUser_2, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnGoToLoginPage = QToolButton(self.pageRegistration)
        self.btnGoToLoginPage.setObjectName(u"btnGoToLoginPage")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnGoToLoginPage.sizePolicy().hasHeightForWidth())
        self.btnGoToLoginPage.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u":/user-login.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGoToLoginPage.setIcon(icon2)
        self.btnGoToLoginPage.setIconSize(QSize(25, 25))
        self.btnGoToLoginPage.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.btnGoToLoginPage)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnRegister = QPushButton(self.pageRegistration)
        self.btnRegister.setObjectName(u"btnRegister")

        self.horizontalLayout_2.addWidget(self.btnRegister)

        self.btnCancelRegistrationPage = QPushButton(self.pageRegistration)
        self.btnCancelRegistrationPage.setObjectName(u"btnCancelRegistrationPage")

        self.horizontalLayout_2.addWidget(self.btnCancelRegistrationPage)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ledUsernameRegistrationPage = QLineEdit(self.pageRegistration)
        self.ledUsernameRegistrationPage.setObjectName(u"ledUsernameRegistrationPage")
        self.ledUsernameRegistrationPage.setMaxLength(12)

        self.gridLayout_4.addWidget(self.ledUsernameRegistrationPage, 0, 1, 1, 1)

        self.label_4 = QLabel(self.pageRegistration)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.pageRegistration)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)

        self.ledPasswordAgainRegistrationPage = QLineEdit(self.pageRegistration)
        self.ledPasswordAgainRegistrationPage.setObjectName(u"ledPasswordAgainRegistrationPage")
        self.ledPasswordAgainRegistrationPage.setMaxLength(18)
        self.ledPasswordAgainRegistrationPage.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_4.addWidget(self.ledPasswordAgainRegistrationPage, 2, 1, 1, 1)

        self.ledPasswordHint = QLineEdit(self.pageRegistration)
        self.ledPasswordHint.setObjectName(u"ledPasswordHint")
        self.ledPasswordHint.setMaxLength(50)

        self.gridLayout_4.addWidget(self.ledPasswordHint, 3, 1, 1, 1)

        self.ledPasswordRegistrationPage = QLineEdit(self.pageRegistration)
        self.ledPasswordRegistrationPage.setObjectName(u"ledPasswordRegistrationPage")
        self.ledPasswordRegistrationPage.setMaxLength(18)
        self.ledPasswordRegistrationPage.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_4.addWidget(self.ledPasswordRegistrationPage, 1, 1, 1, 1)

        self.label_6 = QLabel(self.pageRegistration)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_8 = QLabel(self.pageRegistration)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.stackedWidgetMain.addWidget(self.pageRegistration)

        self._2.addWidget(self.stackedWidgetMain)


        self.gridLayout_5.addWidget(self.frameMain, 0, 0, 1, 1)

        QWidget.setTabOrder(self.ledUsername, self.ledPassword)
        QWidget.setTabOrder(self.ledPassword, self.btnLogIn)
        QWidget.setTabOrder(self.btnLogIn, self.btnClose)
        QWidget.setTabOrder(self.btnClose, self.btnPasswordHint)
        QWidget.setTabOrder(self.btnPasswordHint, self.ledUsernameRegistrationPage)
        QWidget.setTabOrder(self.ledUsernameRegistrationPage, self.ledPasswordRegistrationPage)
        QWidget.setTabOrder(self.ledPasswordRegistrationPage, self.ledPasswordAgainRegistrationPage)
        QWidget.setTabOrder(self.ledPasswordAgainRegistrationPage, self.ledPasswordHint)
        QWidget.setTabOrder(self.ledPasswordHint, self.btnRegister)
        QWidget.setTabOrder(self.btnRegister, self.btnCancelRegistrationPage)

        self.retranslateUi(DialogLogin)

        self.stackedWidgetMain.setCurrentIndex(1)
        self.btnLogIn.setDefault(True)
        self.btnRegister.setDefault(True)


        QMetaObject.connectSlotsByName(DialogLogin)
    # setupUi

    def retranslateUi(self, DialogLogin):
        DialogLogin.setWindowTitle(QCoreApplication.translate("DialogLogin", u"\u0648\u0631\u0648\u062f", None))
        self.ledPassword.setText(QCoreApplication.translate("DialogLogin", u"123456", None))
        self.ledUsername.setText(QCoreApplication.translate("DialogLogin", u"root", None))
        self.lblUserName.setText(QCoreApplication.translate("DialogLogin", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.lblPassword.setText(QCoreApplication.translate("DialogLogin", u"\u06a9\u0644\u0645\u0647 \u0639\u0628\u0648\u0631", None))
#if QT_CONFIG(tooltip)
        self.btnPasswordHint.setToolTip(QCoreApplication.translate("DialogLogin", u"\u06cc\u0627\u062f\u0622\u0648\u0631\u06cc \u06a9\u0644\u0645\u0647 \u0639\u0628\u0648\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.btnLogIn.setText(QCoreApplication.translate("DialogLogin", u"\u0648\u0631\u0648\u062f", None))
        self.btnClose.setText(QCoreApplication.translate("DialogLogin", u"\u0628\u0633\u062a\u0646", None))
#if QT_CONFIG(tooltip)
        self.btnGoToLoginPage.setToolTip(QCoreApplication.translate("DialogLogin", u"\u0631\u0641\u062a\u0646 \u0628\u0647 \u0635\u0641\u062d\u0647 \u0648\u0631\u0648\u062f", None))
#endif // QT_CONFIG(tooltip)
        self.btnGoToLoginPage.setText(QCoreApplication.translate("DialogLogin", u"...", None))
        self.btnRegister.setText(QCoreApplication.translate("DialogLogin", u"\u062b\u0628\u062a", None))
        self.btnCancelRegistrationPage.setText(QCoreApplication.translate("DialogLogin", u"\u0644\u063a\u0648", None))
        self.label_4.setText(QCoreApplication.translate("DialogLogin", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.label_7.setText(QCoreApplication.translate("DialogLogin", u"\u06cc\u0627\u062f\u0622\u0648\u0631\u06cc \u0631\u0645\u0632", None))
        self.ledPasswordHint.setPlaceholderText(QCoreApplication.translate("DialogLogin", u"\u06cc\u0627\u062f\u0622\u0648\u0631\u06cc \u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u0647\u0646\u06af\u0627\u0645 \u0641\u0631\u0627\u0645\u0648\u0634\u06cc", None))
        self.label_6.setText(QCoreApplication.translate("DialogLogin", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.label_8.setText(QCoreApplication.translate("DialogLogin", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632", None))
    # retranslateUi

