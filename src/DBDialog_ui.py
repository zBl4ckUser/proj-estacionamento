# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DBDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_DBDialog(object):
    def setupUi(self, DBDialog):
        if not DBDialog.objectName():
            DBDialog.setObjectName(u"DBDialog")
        DBDialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(DBDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(DBDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(32, 77, 112, 16))
        self.label_2 = QLabel(DBDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(32, 142, 40, 16))
        self.label_3 = QLabel(DBDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(32, 170, 32, 16))
        self.ed_server = QLineEdit(DBDialog)
        self.ed_server.setObjectName(u"ed_server")
        self.ed_server.setGeometry(QRect(150, 77, 161, 22))
        self.ed_server.setEchoMode(QLineEdit.Normal)
        self.ed_user = QLineEdit(DBDialog)
        self.ed_user.setObjectName(u"ed_user")
        self.ed_user.setGeometry(QRect(150, 142, 161, 22))
        self.ed_user.setEchoMode(QLineEdit.Normal)
        self.ed_pwd = QLineEdit(DBDialog)
        self.ed_pwd.setObjectName(u"ed_pwd")
        self.ed_pwd.setGeometry(QRect(150, 170, 161, 22))
        self.ed_pwd.setEchoMode(QLineEdit.Normal)
        self.label_4 = QLabel(DBDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(32, 110, 112, 16))
        self.ed_db = QLineEdit(DBDialog)
        self.ed_db.setObjectName(u"ed_db")
        self.ed_db.setGeometry(QRect(150, 110, 161, 22))
        self.ed_db.setEchoMode(QLineEdit.Normal)

        self.retranslateUi(DBDialog)
        self.buttonBox.accepted.connect(DBDialog.accept)
        self.buttonBox.rejected.connect(DBDialog.reject)

        QMetaObject.connectSlotsByName(DBDialog)
    # setupUi

    def retranslateUi(self, DBDialog):
        DBDialog.setWindowTitle(QCoreApplication.translate("DBDialog", u"Digite as informa\u00e7\u00f5es do Banco de Dados", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("DBDialog", u"Endere\u00e7o do banco de dados", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DBDialog", u"Endere\u00e7o do Servidor", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DBDialog", u"Seu usu\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DBDialog", u"Usu\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DBDialog", u"Sua senha", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("DBDialog", u"Senha", None))
        self.ed_server.setText("")
        self.ed_user.setText("")
        self.ed_pwd.setText("")
        self.ed_pwd.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("DBDialog", u"Nome do banco de dados", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("DBDialog", u"Database", None))
        self.ed_db.setText("")
    # retranslateUi

