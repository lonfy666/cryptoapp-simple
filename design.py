# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setMaximumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e2f;  /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #f0f0f5;  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 14px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e2f;  /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #f0f0f5;  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 14px;\n"
"}")
        self.priceoutput = QLabel(self.centralwidget)
        self.priceoutput.setObjectName(u"priceoutput")
        self.priceoutput.setGeometry(QRect(-2, 5, 301, 61))
        self.priceoutput.setStyleSheet(u"QLabel {\n"
"    color: #e0e0e0;  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 22px;\n"
"    margin: 10px;\n"
"}")
        self.priceoutput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coinselector = QComboBox(self.centralwidget)
        self.coinselector.setObjectName(u"coinselector")
        self.coinselector.setGeometry(QRect(20, 83, 261, 61))
        self.coinselector.setStyleSheet(u"QComboBox {\n"
"    background-color: #2a2a3c;  /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 2px solid #4a4a66;  /* \u041b\u0435\u0433\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    color: #ffffff;  /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #2a2a3c;  /* \u0424\u043e\u043d \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4a4a66;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    padding: 5px;\n"
"    background-color: #2a2a3c;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QComboBox::item:hover {\n"
"    background-color: #3b3b54;  /* \u0426\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.updatebutton = QPushButton(self.centralwidget)
        self.updatebutton.setObjectName(u"updatebutton")
        self.updatebutton.setGeometry(QRect(10, 440, 279, 39))
        self.updatebutton.setStyleSheet(u"QPushButton {\n"
"    background-color: #007bff;  /* \u042f\u0440\u043a\u0438\u0439 \u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #ffffff;  /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;  /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003f7f;  /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \u0432 disabled \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0438 */\n"
"QPushButton:disabled {\n"
"    background-col"
                        "or: #666666;\n"
"    color: #b3b3b3;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CryptoApp", None))
        self.priceoutput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.updatebutton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

