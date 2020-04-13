# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Applicazioni/SpinTool/spintool/about_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(584, 494)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.labelVersion = QtWidgets.QLabel(Dialog)
        self.labelVersion.setGeometry(QtCore.QRect(20, 110, 511, 31))
        self.labelVersion.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Noto Sans\";\n"
"text-align: center;")
        self.labelVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.labelText = QtWidgets.QLabel(Dialog)
        self.labelText.setGeometry(QtCore.QRect(20, 230, 521, 61))
        self.labelText.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Noto Sans\";\n"
"text-align: left top;")
        self.labelText.setWordWrap(True)
        self.labelText.setObjectName("labelText")
        self.labelLicense = QtWidgets.QLabel(Dialog)
        self.labelLicense.setGeometry(QtCore.QRect(20, 310, 521, 61))
        self.labelLicense.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Noto Sans\";\n"
"text-align: left top;")
        self.labelLicense.setWordWrap(True)
        self.labelLicense.setObjectName("labelLicense")
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(20, 10, 551, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
        self.labelLogo.setSizePolicy(sizePolicy)
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/icons/icons/ST_Logo_Small_Transparent.png"))
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.labelMP = QtWidgets.QLabel(Dialog)
        self.labelMP.setGeometry(QtCore.QRect(495, 400, 71, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMP.sizePolicy().hasHeightForWidth())
        self.labelMP.setSizePolicy(sizePolicy)
        self.labelMP.setText("")
        self.labelMP.setPixmap(QtGui.QPixmap(":/icons/icons/MeltinPop_Logo_100.png"))
        self.labelMP.setScaledContents(True)
        self.labelMP.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMP.setObjectName("labelMP")
        self.labelMpText = QtWidgets.QLabel(Dialog)
        self.labelMpText.setGeometry(QtCore.QRect(326, 397, 151, 91))
        self.labelMpText.setStyleSheet("color: rgb(20, 20, 20);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 11pt \"Noto Sans\";")
        self.labelMpText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMpText.setWordWrap(True)
        self.labelMpText.setObjectName("labelMpText")
        self.btnWebLink = QtWidgets.QPushButton(Dialog)
        self.btnWebLink.setGeometry(QtCore.QRect(20, 180, 521, 31))
        self.btnWebLink.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnWebLink.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: bold 10pt \"Noto Sans\";\n"
"border: None;\n"
"text-align: left;")
        self.btnWebLink.setObjectName("btnWebLink")
        self.labelSB = QtWidgets.QLabel(Dialog)
        self.labelSB.setGeometry(QtCore.QRect(8, 410, 111, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSB.sizePolicy().hasHeightForWidth())
        self.labelSB.setSizePolicy(sizePolicy)
        self.labelSB.setText("")
        self.labelSB.setPixmap(QtGui.QPixmap(":/icons/icons/logo_sb.png"))
        self.labelSB.setScaledContents(True)
        self.labelSB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSB.setObjectName("labelSB")
        self.labelSBtext = QtWidgets.QLabel(Dialog)
        self.labelSBtext.setGeometry(QtCore.QRect(130, 410, 121, 71))
        self.labelSBtext.setStyleSheet("color: rgb(20, 20, 20);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.labelSBtext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSBtext.setWordWrap(True)
        self.labelSBtext.setObjectName("labelSBtext")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "about SpinTool"))
        self.labelVersion.setText(_translate("Dialog", "version"))
        self.labelText.setText(_translate("Dialog", "text"))
        self.labelLicense.setText(_translate("Dialog", "license"))
        self.labelMpText.setText(_translate("Dialog", "Meltin\'Pop \n"
" music productions & \n"
" music stuff-ware"))
        self.btnWebLink.setText(_translate("Dialog", "PushButton"))
        self.labelSBtext.setText(_translate("Dialog", "SpinTool proudly derives from Vampouille\'s SuperBoucle"))
import gui_rc
