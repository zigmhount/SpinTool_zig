# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_song_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(592, 206)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 160, 571, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelGridSize = QtWidgets.QLabel(Dialog)
        self.labelGridSize.setGeometry(QtCore.QRect(20, 10, 121, 18))
        self.labelGridSize.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: bold 10pt \"Noto Sans\";")
        self.labelGridSize.setObjectName("labelGridSize")
        self.labelMasterVolume = QtWidgets.QLabel(Dialog)
        self.labelMasterVolume.setGeometry(QtCore.QRect(180, 10, 111, 21))
        self.labelMasterVolume.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: bold 10pt \"Noto Sans\";")
        self.labelMasterVolume.setObjectName("labelMasterVolume")
        self.spinMasterVolume = QtWidgets.QSpinBox(Dialog)
        self.spinMasterVolume.setGeometry(QtCore.QRect(180, 40, 71, 31))
        self.spinMasterVolume.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Noto Sans\";")
        self.spinMasterVolume.setMinimum(0)
        self.spinMasterVolume.setMaximum(200)
        self.spinMasterVolume.setProperty("value", 100)
        self.spinMasterVolume.setObjectName("spinMasterVolume")
        self.heightSpinBox = QtWidgets.QSpinBox(Dialog)
        self.heightSpinBox.setGeometry(QtCore.QRect(67, 80, 72, 31))
        self.heightSpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Noto Sans\";")
        self.heightSpinBox.setMaximum(16)
        self.heightSpinBox.setProperty("value", 8)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.widthSpinBox = QtWidgets.QSpinBox(Dialog)
        self.widthSpinBox.setGeometry(QtCore.QRect(67, 39, 72, 31))
        self.widthSpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Noto Sans\";")
        self.widthSpinBox.setMaximum(16)
        self.widthSpinBox.setProperty("value", 8)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 39, 37, 25))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 41, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.labelBeats = QtWidgets.QLabel(Dialog)
        self.labelBeats.setGeometry(QtCore.QRect(470, 10, 101, 21))
        self.labelBeats.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: bold 10pt \"Noto Sans\";")
        self.labelBeats.setObjectName("labelBeats")
        self.spinBeats = QtWidgets.QSpinBox(Dialog)
        self.spinBeats.setGeometry(QtCore.QRect(470, 40, 71, 31))
        self.spinBeats.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Noto Sans\";")
        self.spinBeats.setMinimum(1)
        self.spinBeats.setMaximum(99)
        self.spinBeats.setProperty("value", 4)
        self.spinBeats.setObjectName("spinBeats")
        self.spinBPM = QtWidgets.QSpinBox(Dialog)
        self.spinBPM.setGeometry(QtCore.QRect(345, 40, 71, 31))
        self.spinBPM.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Noto Sans\";")
        self.spinBPM.setMinimum(1)
        self.spinBPM.setMaximum(260)
        self.spinBPM.setProperty("value", 120)
        self.spinBPM.setObjectName("spinBPM")
        self.labelBPM = QtWidgets.QLabel(Dialog)
        self.labelBPM.setGeometry(QtCore.QRect(345, 10, 41, 21))
        self.labelBPM.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: bold 10pt \"Noto Sans\";")
        self.labelBPM.setObjectName("labelBPM")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Song"))
        self.labelGridSize.setText(_translate("Dialog", "Grid size"))
        self.labelMasterVolume.setText(_translate("Dialog", "Master volume"))
        self.label.setText(_translate("Dialog", "Width"))
        self.label_2.setText(_translate("Dialog", "Height"))
        self.labelBeats.setText(_translate("Dialog", "Beats per bar"))
        self.labelBPM.setText(_translate("Dialog", "BPM"))
