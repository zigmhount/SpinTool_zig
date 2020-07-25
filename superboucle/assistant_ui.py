# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assistant_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(774, 517)
        Dialog.setMinimumSize(QtCore.QSize(560, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 771, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelLogo = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.labelLogo.setIndent(-1)
        self.labelLogo.setObjectName("labelLogo")
        self.verticalLayout.addWidget(self.labelLogo)
        self.labelAssistant = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAssistant.sizePolicy().hasHeightForWidth())
        self.labelAssistant.setSizePolicy(sizePolicy)
        self.labelAssistant.setStyleSheet("color: rgb(160, 160, 160);\n"
"font: bold italic 18pt \"Noto Sans\";")
        self.labelAssistant.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAssistant.setObjectName("labelAssistant")
        self.verticalLayout.addWidget(self.labelAssistant)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtHelp = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtHelp.sizePolicy().hasHeightForWidth())
        self.txtHelp.setSizePolicy(sizePolicy)
        self.txtHelp.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 12pt \"Noto Sans\";\n"
"border: None;")
        self.txtHelp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtHelp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtHelp.setDocumentTitle("")
        self.txtHelp.setReadOnly(False)
        self.txtHelp.setAcceptRichText(True)
        self.txtHelp.setObjectName("txtHelp")
        self.horizontalLayout.addWidget(self.txtHelp)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SpinTool Assistant"))
        self.labelAssistant.setText(_translate("Dialog", "assistant"))
        self.txtHelp.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
import gui_rc
