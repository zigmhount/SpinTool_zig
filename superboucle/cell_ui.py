# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Sviluppo/SpinTool/superboucle/cell_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cell(object):
    def setupUi(self, Cell):
        Cell.setObjectName("Cell")
        Cell.resize(255, 225)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Cell.sizePolicy().hasHeightForWidth())
        Cell.setSizePolicy(sizePolicy)
        Cell.setMinimumSize(QtCore.QSize(120, 112))
        font = QtGui.QFont()
        font.setFamily("Lato")
        Cell.setFont(font)
        self.cell_frame = QtWidgets.QFrame(Cell)
        self.cell_frame.setGeometry(QtCore.QRect(0, 0, 110, 102))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cell_frame.sizePolicy().hasHeightForWidth())
        self.cell_frame.setSizePolicy(sizePolicy)
        self.cell_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cell_frame.setStyleSheet("#frame {border: 0px;\n"
"    background-color: rgb(190, 190, 190);\n"
"border-radius: 10px;}")
        self.cell_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cell_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cell_frame.setObjectName("cell_frame")
        self.clip_name = QtWidgets.QLabel(self.cell_frame)
        self.clip_name.setGeometry(QtCore.QRect(3, 2, 105, 46))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clip_name.setFont(font)
        self.clip_name.setStyleSheet("font: bold 14pt \"Noto Sans\";\n"
"color: rgb(0, 0, 0);\n"
"text-align: center;")
        self.clip_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.clip_name.setText("")
        self.clip_name.setAlignment(QtCore.Qt.AlignCenter)
        self.clip_name.setWordWrap(True)
        self.clip_name.setObjectName("clip_name")
        self.clip_position = QtWidgets.QProgressBar(self.cell_frame)
        self.clip_position.setGeometry(QtCore.QRect(5, 85, 99, 13))
        self.clip_position.setStyleSheet("color: rgb(0, 85, 255);\n"
"background-color: rgb(190, 190, 190);")
        self.clip_position.setMaximum(97)
        self.clip_position.setProperty("value", 0)
        self.clip_position.setTextVisible(False)
        self.clip_position.setObjectName("clip_position")
        self.edit = QtWidgets.QPushButton(self.cell_frame)
        self.edit.setGeometry(QtCore.QRect(70, 49, 33, 33))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.edit.setFont(font)
        self.edit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.edit.setStyleSheet("font: italic 10pt \"Noto Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"text-align: center;")
        self.edit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/clip-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit.setIcon(icon)
        self.edit.setIconSize(QtCore.QSize(35, 35))
        self.edit.setAutoDefault(False)
        self.edit.setDefault(False)
        self.edit.setFlat(False)
        self.edit.setObjectName("edit")
        self.start_stop = QtWidgets.QPushButton(self.cell_frame)
        self.start_stop.setGeometry(QtCore.QRect(5, 49, 33, 33))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.start_stop.setFont(font)
        self.start_stop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_stop.setStyleSheet("font: italic 10pt \"Noto Sans\";\n"
"background-color: rgb(190, 190, 190);\n"
"color: rgb(0, 0, 0);\n"
"text-align: center;")
        self.start_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/clip-start-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_stop.setIcon(icon1)
        self.start_stop.setIconSize(QtCore.QSize(27, 27))
        self.start_stop.setObjectName("start_stop")
        self.labelVolume = QtWidgets.QLabel(self.cell_frame)
        self.labelVolume.setGeometry(QtCore.QRect(0, 49, 111, 33))
        self.labelVolume.setStyleSheet("font: bold 12pt \"Noto Sans\";")
        self.labelVolume.setTextFormat(QtCore.Qt.PlainText)
        self.labelVolume.setScaledContents(False)
        self.labelVolume.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVolume.setWordWrap(True)
        self.labelVolume.setIndent(0)
        self.labelVolume.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelVolume.setObjectName("labelVolume")
        self.labelVolume.raise_()
        self.clip_name.raise_()
        self.clip_position.raise_()
        self.edit.raise_()
        self.start_stop.raise_()

        self.retranslateUi(Cell)
        QtCore.QMetaObject.connectSlotsByName(Cell)

    def retranslateUi(self, Cell):
        _translate = QtCore.QCoreApplication.translate
        Cell.setWindowTitle(_translate("Cell", "Form"))
        self.cell_frame.setAccessibleName(_translate("Cell", "Help_Cell_Info"))
        self.clip_name.setAccessibleName(_translate("Cell", "Help_Cell_Info"))
        self.clip_position.setAccessibleName(_translate("Cell", "Help_Cell_Info"))
        self.edit.setAccessibleName(_translate("Cell", "Help_Cell_Info"))
        self.start_stop.setAccessibleName(_translate("Cell", "Help_Cell_Info"))
        self.labelVolume.setAccessibleName(_translate("Cell", "Help_Cell_Info"))
        self.labelVolume.setText(_translate("Cell", "5"))
import gui_rc
