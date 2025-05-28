# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogpopup.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_DialogPopup(object):
    def setupUi(self, DialogPopup):
        if not DialogPopup.objectName():
            DialogPopup.setObjectName(u"DialogPopup")
        DialogPopup.resize(302, 85)
        DialogPopup.setMinimumSize(QSize(286, 78))
        DialogPopup.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gridLayout_2 = QGridLayout(DialogPopup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(DialogPopup)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #2c3e50;\n"
"border: 2px solid #3498db;\n"
"/*border-radius: 5px;*/\n"
"color: white;\n"
"font-size: 14px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblMessage = QLabel(self.frame)
        self.lblMessage.setObjectName(u"lblMessage")
        self.lblMessage.setStyleSheet(u"border: 0px solid #3498db\n"
"\n"
"")

        self.gridLayout.addWidget(self.lblMessage, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(DialogPopup)

        QMetaObject.connectSlotsByName(DialogPopup)
    # setupUi

    def retranslateUi(self, DialogPopup):
        DialogPopup.setWindowTitle(QCoreApplication.translate("DialogPopup", u"DialogPopup", None))
        self.lblMessage.setText(QCoreApplication.translate("DialogPopup", u"Your Message Goes HERE!", None))
    # retranslateUi

