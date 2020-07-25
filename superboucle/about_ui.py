# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(700, 460)
        Dialog.setMinimumSize(QtCore.QSize(700, 460))
        Dialog.setMaximumSize(QtCore.QSize(700, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelLogo = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
        self.labelLogo.setSizePolicy(sizePolicy)
        self.labelLogo.setMinimumSize(QtCore.QSize(0, 0))
        self.labelLogo.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/icons/icons/ST_Logo_Small_Transparent.png"))
        self.labelLogo.setScaledContents(False)
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.verticalLayout_2.addWidget(self.labelLogo)
        self.labelVersion = QtWidgets.QLabel(Dialog)
        self.labelVersion.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Noto Sans\";\n"
"text-align: center;")
        self.labelVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.verticalLayout_2.addWidget(self.labelVersion)
        self.btnWebLink = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWebLink.sizePolicy().hasHeightForWidth())
        self.btnWebLink.setSizePolicy(sizePolicy)
        self.btnWebLink.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnWebLink.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnWebLink.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: bold 10pt \"Noto Sans\";\n"
"border: None;\n"
"text-align: left;")
        self.btnWebLink.setObjectName("btnWebLink")
        self.verticalLayout_2.addWidget(self.btnWebLink)
        self.labelText = QtWidgets.QLabel(Dialog)
        self.labelText.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Noto Sans\";\n"
"text-align: left top;")
        self.labelText.setWordWrap(True)
        self.labelText.setObjectName("labelText")
        self.verticalLayout_2.addWidget(self.labelText)
        self.labelLicense = QtWidgets.QLabel(Dialog)
        self.labelLicense.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Noto Sans\";\n"
"text-align: left top;")
        self.labelLicense.setWordWrap(True)
        self.labelLicense.setObjectName("labelLicense")
        self.verticalLayout_2.addWidget(self.labelLicense)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSB = QtWidgets.QLabel(Dialog)
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
        self.horizontalLayout.addWidget(self.labelSB)
        self.labelSBtext = QtWidgets.QLabel(Dialog)
        self.labelSBtext.setStyleSheet("color: rgb(20, 20, 20);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 11pt \"Noto Sans\";")
        self.labelSBtext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSBtext.setWordWrap(True)
        self.labelSBtext.setObjectName("labelSBtext")
        self.horizontalLayout.addWidget(self.labelSBtext)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelMP_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMP_2.sizePolicy().hasHeightForWidth())
        self.labelMP_2.setSizePolicy(sizePolicy)
        self.labelMP_2.setMinimumSize(QtCore.QSize(80, 80))
        self.labelMP_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelMP_2.setMidLineWidth(0)
        self.labelMP_2.setText("")
        self.labelMP_2.setPixmap(QtGui.QPixmap(":/icons/icons/Superdirt_Logo_80.png"))
        self.labelMP_2.setScaledContents(False)
        self.labelMP_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMP_2.setIndent(-1)
        self.labelMP_2.setObjectName("labelMP_2")
        self.verticalLayout.addWidget(self.labelMP_2)
        self.labelMpText_2 = QtWidgets.QLabel(Dialog)
        self.labelMpText_2.setStyleSheet("color: rgb(20, 20, 20);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 11pt \"Noto Sans\";")
        self.labelMpText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMpText_2.setWordWrap(True)
        self.labelMpText_2.setObjectName("labelMpText_2")
        self.verticalLayout.addWidget(self.labelMpText_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelMpText = QtWidgets.QLabel(Dialog)
        self.labelMpText.setStyleSheet("color: rgb(20, 20, 20);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 11pt \"Noto Sans\";")
        self.labelMpText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMpText.setWordWrap(True)
        self.labelMpText.setObjectName("labelMpText")
        self.horizontalLayout_2.addWidget(self.labelMpText)
        self.labelMP = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMP.sizePolicy().hasHeightForWidth())
        self.labelMP.setSizePolicy(sizePolicy)
        self.labelMP.setMinimumSize(QtCore.QSize(80, 100))
        self.labelMP.setMaximumSize(QtCore.QSize(80, 100))
        self.labelMP.setText("")
        self.labelMP.setPixmap(QtGui.QPixmap(":/icons/icons/MeltinPop_Logo_100.png"))
        self.labelMP.setScaledContents(True)
        self.labelMP.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMP.setObjectName("labelMP")
        self.horizontalLayout_2.addWidget(self.labelMP)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "about SpinTool"))
        self.labelVersion.setText(_translate("Dialog", "version"))
        self.btnWebLink.setText(_translate("Dialog", "PushButton"))
        self.labelText.setText(_translate("Dialog", "text"))
        self.labelLicense.setText(_translate("Dialog", "license"))
        self.labelSBtext.setText(_translate("Dialog", "SpinTool proudly \n"
"derives from \n"
"SuperBoucle"))
        self.labelMpText_2.setText(_translate("Dialog", "Superdirt³ / Sonejo.net"))
        self.labelMpText.setText(_translate("Dialog", "Meltin\'Pop \n"
" music productions & \n"
" music stuff-ware"))
import gui_rc
