# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statusui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_statusDialog(object):
    def setupUi(self, statusDialog):
        if not statusDialog.objectName():
            statusDialog.setObjectName(u"statusDialog")
        statusDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(statusDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.statusLabel = QLabel(statusDialog)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout.addWidget(self.statusLabel)

        self.buttonBox = QDialogButtonBox(statusDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(statusDialog)
        self.buttonBox.accepted.connect(statusDialog.accept)
        self.buttonBox.rejected.connect(statusDialog.reject)

        QMetaObject.connectSlotsByName(statusDialog)
    # setupUi

    def retranslateUi(self, statusDialog):
        statusDialog.setWindowTitle(QCoreApplication.translate("statusDialog", u"Status", None))
        self.statusLabel.setText(QCoreApplication.translate("statusDialog", u"Status", None))
    # retranslateUi

