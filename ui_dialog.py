# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(461, 369)
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(160, 10, 141, 16))
        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 320, 451, 21))
        self.progressBar.setValue(24)
        self.start = QPushButton(self)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(190, 280, 75, 23))
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 110, 231, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.chushibiao = QPushButton(self.layoutWidget)
        self.chushibiao.setObjectName(u"chushibiao")

        self.verticalLayout.addWidget(self.chushibiao)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 372, 12))
        self.complete = QLabel(self)
        self.complete.setObjectName(u"complete")
        self.complete.setGeometry(QRect(200, 350, 54, 12))
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 80, 301, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.grade = QComboBox(self.widget)
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.setObjectName(u"grade")

        self.horizontalLayout.addWidget(self.grade)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"\u6587\u8a00\u6587\u6ce8\u91ca\u7ffb\u8bd1\u5c0f\u7a0b\u5e8f", None))
        self.start.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb", None))
        self.chushibiao.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u5f85\u6ce8\u91ca\u53e4\u6587", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u6ce8\u91ca\u683c\u5f0f\u4e3atxt\u683c\u5f0f\uff0c\u4e00\u884c\u4e00\u6ce8\u91ca\uff0c\u5f85\u6ce8\u91ca\u8bcd\u4e0e\u6ce8\u89e3\u8bf7\u7528\u82f1\u6587:\u9694\u5f00", None))
        self.complete.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u9009\u62e9\u4f60\u7684\u5e74\u7ea7\uff1a", None))
        self.grade.setItemText(0, QCoreApplication.translate("Dialog", u"\u516d\u5e74\u7ea7", None))
        self.grade.setItemText(1, QCoreApplication.translate("Dialog", u"\u4e03\u5e74\u7ea7", None))
        self.grade.setItemText(2, QCoreApplication.translate("Dialog", u"\u516b\u5e74\u7ea7", None))
        self.grade.setItemText(3, QCoreApplication.translate("Dialog", u"\u4e5d\u5e74\u7ea7", None))

    # retranslateUi

