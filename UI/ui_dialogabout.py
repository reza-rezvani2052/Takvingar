# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogabout.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        if not DialogAbout.objectName():
            DialogAbout.setObjectName(u"DialogAbout")
        DialogAbout.resize(446, 453)
        icon = QIcon()
        icon.addFile(u":/app-icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        DialogAbout.setWindowIcon(icon)
        DialogAbout.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        DialogAbout.setModal(True)
        self.gridLayout = QGridLayout(DialogAbout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblMainContent = QLabel(DialogAbout)
        self.lblMainContent.setObjectName(u"lblMainContent")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMainContent.sizePolicy().hasHeightForWidth())
        self.lblMainContent.setSizePolicy(sizePolicy)
        self.lblMainContent.setStyleSheet(u"border: 2px solid gray;\n"
"border-radius: 7px;\n"
"background-color: #E5E5E5;")
        self.lblMainContent.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.lblMainContent, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btnOk = QPushButton(DialogAbout)
        self.btnOk.setObjectName(u"btnOk")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnOk.sizePolicy().hasHeightForWidth())
        self.btnOk.setSizePolicy(sizePolicy1)
        self.btnOk.setStyleSheet(u"QPushButton{\n"
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
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/pic/OK.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOk.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnOk)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.retranslateUi(DialogAbout)

        self.btnOk.setDefault(True)


        QMetaObject.connectSlotsByName(DialogAbout)
    # setupUi

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(QCoreApplication.translate("DialogAbout", u"\u062f\u0631\u0628\u0627\u0631\u0647 \u0628\u0631\u0646\u0627\u0645\u0647", None))
        self.lblMainContent.setText(QCoreApplication.translate("DialogAbout", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">\u0645\u062f\u06cc\u0631\u06cc\u062a \u0645\u0627\u0644\u06cc \u067e\u0631\u0648\u0698\u0647\u200c\u0647\u0627\u06cc \u0633\u0627\u062e\u062a\u0645\u0627\u0646\u06cc</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">&quot;\u062a\u06a9\u0648\u06cc\u0646\u06af\u0631&quot;</span></p><p align=\"center\">\u0646\u0633\u062e\u0647 1.0.0 </p><p align=\"center\">\u062a\u0627\u0628\u0633\u062a\u0627\u0646 \u06f1\u06f4\u06f0\u06f4<br/></p><p align=\"center\"><a href=\"http://takvingar.ir/\"><span style=\" color:#27bf73;\">\u0628\u0627\u0632\u062f\u06cc\u062f \u0627\u0632 \u0648\u0628\u0633\u0627\u06cc\u062a \u0628\u0631\u0646\u0627\u0645\u0647</span></a></p><p><br/></p><p align=\"center\"><a href=\"mailto:reza.rezvani2052@gmail.com?subject=Takvingar&amp;body=Hi\"><span style=\" text-decoration: underline; color:#0000ff;\">Reza.Rezvani2052@gmail.com</span></a><br/></p><p align"
                        "=\"center\"><br/></p></body></html>", None))
        self.btnOk.setText(QCoreApplication.translate("DialogAbout", u"\u0628\u0633\u062a\u0646", None))
    # retranslateUi

