# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Sviluppo/SpinTool/superboucle/add_clip_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 263)
        Dialog.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 220, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.emptyButton = QtWidgets.QRadioButton(Dialog)
        self.emptyButton.setGeometry(QtCore.QRect(40, 100, 99, 21))
        self.emptyButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.emptyButton.setObjectName("emptyButton")
        self.newButton = QtWidgets.QRadioButton(Dialog)
        self.newButton.setGeometry(QtCore.QRect(40, 20, 141, 21))
        self.newButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.newButton.setObjectName("newButton")
        self.useButton = QtWidgets.QRadioButton(Dialog)
        self.useButton.setGeometry(QtCore.QRect(40, 60, 81, 21))
        self.useButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.useButton.setObjectName("useButton")
        self.fileList = QtWidgets.QComboBox(Dialog)
        self.fileList.setGeometry(QtCore.QRect(140, 60, 251, 23))
        self.fileList.setStyleSheet("color: rgb(0, 0, 0);")
        self.fileList.setObjectName("fileList")
        self.groupBoxClip = QtWidgets.QGroupBox(Dialog)
        self.groupBoxClip.setGeometry(QtCore.QRect(40, 144, 341, 61))
        self.groupBoxClip.setStyleSheet("font: italic 9pt \"Noto Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border: 1;")
        self.groupBoxClip.setFlat(False)
        self.groupBoxClip.setObjectName("groupBoxClip")
        self.cBoxLockRec = QtWidgets.QCheckBox(self.groupBoxClip)
        self.cBoxLockRec.setGeometry(QtCore.QRect(140, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cBoxLockRec.setFont(font)
        self.cBoxLockRec.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.cBoxLockRec.setObjectName("cBoxLockRec")
        self.cBoxOneShotClip = QtWidgets.QCheckBox(self.groupBoxClip)
        self.cBoxOneShotClip.setGeometry(QtCore.QRect(0, 30, 121, 31))
        self.cBoxOneShotClip.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.cBoxOneShotClip.setObjectName("cBoxOneShotClip")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.emptyButton.setText(_translate("Dialog", "Empty clip"))
        self.newButton.setText(_translate("Dialog", "Load new file..."))
        self.useButton.setText(_translate("Dialog", "Use file"))
        self.groupBoxClip.setTitle(_translate("Dialog", "Clip behaviour"))
        self.cBoxLockRec.setText(_translate("Dialog", "Lock clip (no recording)"))
        self.cBoxOneShotClip.setText(_translate("Dialog", "One-shot clip"))
