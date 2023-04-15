# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linkaccountui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_linkAnAccountDialog(object):
    def setupUi(self, linkAnAccountDialog):
        if not linkAnAccountDialog.objectName():
            linkAnAccountDialog.setObjectName(u"linkAnAccountDialog")
        linkAnAccountDialog.resize(400, 300)
        linkAnAccountDialog.setMinimumSize(QSize(400, 300))
        self.verticalLayout = QVBoxLayout(linkAnAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameLabel = QLabel(linkAnAccountDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.verticalLayout.addWidget(self.nameLabel)

        self.nameText = QTextEdit(linkAnAccountDialog)
        self.nameText.setObjectName(u"nameText")

        self.verticalLayout.addWidget(self.nameText)

        self.curlLabel = QLabel(linkAnAccountDialog)
        self.curlLabel.setObjectName(u"curlLabel")

        self.verticalLayout.addWidget(self.curlLabel)

        self.curlText = QTextEdit(linkAnAccountDialog)
        self.curlText.setObjectName(u"curlText")

        self.verticalLayout.addWidget(self.curlText)

        self.buttonBox = QDialogButtonBox(linkAnAccountDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(linkAnAccountDialog)
        self.buttonBox.accepted.connect(linkAnAccountDialog.accept)
        self.buttonBox.rejected.connect(linkAnAccountDialog.reject)

        QMetaObject.connectSlotsByName(linkAnAccountDialog)
    # setupUi

    def retranslateUi(self, linkAnAccountDialog):
        linkAnAccountDialog.setWindowTitle(QCoreApplication.translate("linkAnAccountDialog", u"Link an account", None))
        self.nameLabel.setText(QCoreApplication.translate("linkAnAccountDialog", u"Enter name for your account", None))
        self.curlLabel.setText(QCoreApplication.translate("linkAnAccountDialog", u"Paste your CreateTweet request here in cURL", None))
    # retranslateUi

