# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Sviluppo/SpinTool/superboucle/export_samples_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(680, 338)
        Dialog.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 300, 661, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.cBoxNormalize = QtWidgets.QCheckBox(Dialog)
        self.cBoxNormalize.setGeometry(QtCore.QRect(10, 110, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cBoxNormalize.setFont(font)
        self.cBoxNormalize.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.cBoxNormalize.setObjectName("cBoxNormalize")
        self.labelChoosePath = QtWidgets.QLabel(Dialog)
        self.labelChoosePath.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.labelChoosePath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.labelChoosePath.setObjectName("labelChoosePath")
        self.btnPath = QtWidgets.QPushButton(Dialog)
        self.btnPath.setGeometry(QtCore.QRect(10, 50, 51, 41))
        self.btnPath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.btnPath.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPath.setIcon(icon)
        self.btnPath.setIconSize(QtCore.QSize(27, 27))
        self.btnPath.setObjectName("btnPath")
        self.labelPath = QtWidgets.QLabel(Dialog)
        self.labelPath.setGeometry(QtCore.QRect(70, 50, 591, 41))
        self.labelPath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.labelPath.setObjectName("labelPath")
        self.labelX = QtWidgets.QLabel(Dialog)
        self.labelX.setGeometry(QtCore.QRect(20, 180, 101, 18))
        self.labelX.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.labelX.setObjectName("labelX")
        self.lineX = QtWidgets.QLineEdit(Dialog)
        self.lineX.setGeometry(QtCore.QRect(130, 170, 101, 41))
        self.lineX.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.lineX.setAlignment(QtCore.Qt.AlignCenter)
        self.lineX.setObjectName("lineX")
        self.labelY = QtWidgets.QLabel(Dialog)
        self.labelY.setGeometry(QtCore.QRect(20, 240, 101, 18))
        self.labelY.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.labelY.setObjectName("labelY")
        self.lineY = QtWidgets.QLineEdit(Dialog)
        self.lineY.setGeometry(QtCore.QRect(130, 230, 101, 41))
        self.lineY.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.lineY.setAlignment(QtCore.Qt.AlignCenter)
        self.lineY.setObjectName("lineY")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Export all samples"))
        self.cBoxNormalize.setText(_translate("Dialog", "Normalize samples when exporting"))
        self.labelChoosePath.setText(_translate("Dialog", "Export all clip samples to:"))
        self.labelPath.setText(_translate("Dialog", "(select a directory for exporting)"))
        self.labelX.setText(_translate("Dialog", "Column prefix:"))
        self.lineX.setText(_translate("Dialog", "X"))
        self.lineX.setPlaceholderText(_translate("Dialog", "X"))
        self.labelY.setText(_translate("Dialog", "Row prefix:"))
        self.lineY.setText(_translate("Dialog", "Y"))
        self.lineY.setPlaceholderText(_translate("Dialog", "Y"))
import gui_rc
