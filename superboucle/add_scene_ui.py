# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Sviluppo/SpinTool/superboucle/add_scene_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 171)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 0, 111, 91))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(130, 12, 211, 31))
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(17, 20, 111, 16))
        self.label.setObjectName("label")
        self.checkBoxIncludeSelected = QtWidgets.QCheckBox(Dialog)
        self.checkBoxIncludeSelected.setGeometry(QtCore.QRect(10, 70, 341, 29))
        self.checkBoxIncludeSelected.setObjectName("checkBoxIncludeSelected")
        self.checkBoxIncludeStart = QtWidgets.QCheckBox(Dialog)
        self.checkBoxIncludeStart.setGeometry(QtCore.QRect(10, 110, 341, 29))
        self.checkBoxIncludeStart.setObjectName("checkBoxIncludeStart")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add new Scene..."))
        self.label.setText(_translate("Dialog", "New Scene name :"))
        self.checkBoxIncludeSelected.setAccessibleName(_translate("Dialog", "Help_Scene_Include"))
        self.checkBoxIncludeSelected.setText(_translate("Dialog", "include selected clips"))
        self.checkBoxIncludeStart.setAccessibleName(_translate("Dialog", "Help_Scene_Include"))
        self.checkBoxIncludeStart.setText(_translate("Dialog", "include playing / starting clips"))
