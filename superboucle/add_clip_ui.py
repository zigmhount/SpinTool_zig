# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Sviluppo/SpinTool/superboucle/add_clip_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 240)
        Dialog.setMinimumSize(QtCore.QSize(350, 240))
        Dialog.setMaximumSize(QtCore.QSize(350, 240))
        Dialog.setStyleSheet("/* background-color: rgb(242, 242, 242);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.newButton = QtWidgets.QRadioButton(Dialog)
        self.newButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Noto Sans\";")
        self.newButton.setObjectName("newButton")
        self.verticalLayout_2.addWidget(self.newButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.useButton = QtWidgets.QRadioButton(Dialog)
        self.useButton.setStyleSheet("/*color: rgb(0, 0, 0);\n"
"font: 10pt \"Noto Sans\";")
        self.useButton.setObjectName("useButton")
        self.horizontalLayout_2.addWidget(self.useButton)
        self.fileList = QtWidgets.QComboBox(Dialog)
        self.fileList.setMinimumSize(QtCore.QSize(250, 0))
        self.fileList.setStyleSheet("/*color: rgb(0, 0, 0);")
        self.fileList.setObjectName("fileList")
        self.horizontalLayout_2.addWidget(self.fileList)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.emptyButton = QtWidgets.QRadioButton(Dialog)
        self.emptyButton.setStyleSheet("/*color: rgb(0, 0, 0);\n"
"font: 10pt \"Noto Sans\";")
        self.emptyButton.setObjectName("emptyButton")
        self.verticalLayout_2.addWidget(self.emptyButton)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.groupBoxClip = QtWidgets.QGroupBox(Dialog)
        self.groupBoxClip.setStyleSheet("/*font: italic 9pt \"Noto Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border: 1;")
        self.groupBoxClip.setFlat(False)
        self.groupBoxClip.setObjectName("groupBoxClip")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxClip)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cBoxMetronomeClip = QtWidgets.QCheckBox(self.groupBoxClip)
        self.cBoxMetronomeClip.setStyleSheet("/*color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.cBoxMetronomeClip.setObjectName("cBoxMetronomeClip")
        self.verticalLayout.addWidget(self.cBoxMetronomeClip)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cBoxOneShotClip = QtWidgets.QCheckBox(self.groupBoxClip)
        self.cBoxOneShotClip.setStyleSheet("/*color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.cBoxOneShotClip.setObjectName("cBoxOneShotClip")
        self.horizontalLayout.addWidget(self.cBoxOneShotClip)
        self.cBoxLockRec = QtWidgets.QCheckBox(self.groupBoxClip)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cBoxLockRec.setFont(font)
        self.cBoxLockRec.setStyleSheet("/*color: rgb(0, 0, 0);\n"
"background-color: rgb(242, 242, 242);\n"
"font: 10pt \"Noto Sans\";")
        self.cBoxLockRec.setObjectName("cBoxLockRec")
        self.horizontalLayout.addWidget(self.cBoxLockRec)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBoxClip)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.useButton.toggled['bool'].connect(self.fileList.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create new clip"))
        self.newButton.setText(_translate("Dialog", "Load new file..."))
        self.useButton.setText(_translate("Dialog", "Use file:"))
        self.emptyButton.setText(_translate("Dialog", "Empty clip"))
        self.groupBoxClip.setTitle(_translate("Dialog", "Clip behaviour"))
        self.cBoxMetronomeClip.setAccessibleName(_translate("Dialog", "Help_Clip_Metronome"))
        self.cBoxMetronomeClip.setText(_translate("Dialog", "Create a Click (metronome) clip"))
        self.cBoxOneShotClip.setText(_translate("Dialog", "One-shot clip"))
        self.cBoxLockRec.setText(_translate("Dialog", "Lock clip (no recording)"))
