# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mixerstrip_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mixerstrip(object):
    def setupUi(self, Mixerstrip):
        Mixerstrip.setObjectName("Mixerstrip")
        Mixerstrip.resize(82, 457)
        Mixerstrip.setMaximumSize(QtCore.QSize(82, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Mixerstrip)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Mixerstrip)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(72, 0))
        self.frame.setMaximumSize(QtCore.QSize(72, 16777215))
        self.frame.setBaseSize(QtCore.QSize(72, 0))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(2, 9, 2, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.port_name_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.port_name_label.setFont(font)
        self.port_name_label.setStyleSheet("font: bold 9pt \"Noto Sans\";")
        self.port_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.port_name_label.setObjectName("port_name_label")
        self.verticalLayout.addWidget(self.port_name_label)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(72, 320))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.gain_knob = QtWidgets.QDial(self.frame_3)
        self.gain_knob.setMaximumSize(QtCore.QSize(40, 40))
        self.gain_knob.setAutoFillBackground(False)
        self.gain_knob.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.gain_knob.setMaximum(200)
        self.gain_knob.setProperty("value", 100)
        self.gain_knob.setObjectName("gain_knob")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gain_knob)
        self.send1_knob = QtWidgets.QDial(self.frame_3)
        self.send1_knob.setEnabled(True)
        self.send1_knob.setMaximumSize(QtCore.QSize(40, 40))
        self.send1_knob.setMouseTracking(False)
        self.send1_knob.setAutoFillBackground(False)
        self.send1_knob.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.send1_knob.setMaximum(100)
        self.send1_knob.setProperty("value", 0)
        self.send1_knob.setObjectName("send1_knob")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.send1_knob)
        self.send2_knob = QtWidgets.QDial(self.frame_3)
        self.send2_knob.setMaximumSize(QtCore.QSize(40, 40))
        self.send2_knob.setAutoFillBackground(False)
        self.send2_knob.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.send2_knob.setMaximum(100)
        self.send2_knob.setProperty("value", 0)
        self.send2_knob.setObjectName("send2_knob")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.send2_knob)
        self.gain_label = QtWidgets.QLabel(self.frame_3)
        self.gain_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gain_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gain_label.setObjectName("gain_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gain_label)
        self.send1_label = QtWidgets.QLabel(self.frame_3)
        self.send1_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.send1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.send1_label.setObjectName("send1_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.send1_label)
        self.send2_label = QtWidgets.QLabel(self.frame_3)
        self.send2_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.send2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.send2_label.setObjectName("send2_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.send2_label)
        self.verticalLayout.addWidget(self.frame_3)
        self.vol_label = QtWidgets.QLabel(self.frame)
        self.vol_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vol_label.setObjectName("vol_label")
        self.verticalLayout.addWidget(self.vol_label)
        self.vol_slider = QtWidgets.QSlider(self.frame)
        self.vol_slider.setMinimumSize(QtCore.QSize(50, 0))
        self.vol_slider.setToolTip("")
        self.vol_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vol_slider.setAutoFillBackground(True)
        self.vol_slider.setStyleSheet("QSlider::groove:vertical {\n"
"background:  #A00659;\n"
"position: absolute;\n"
"left: 21px; right: 21px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"height: 39px;\n"
"width: 30px;\n"
"image: url(:/icons/icons/fader.png);\n"
"/*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #AAAAAA, stop : 0.05 #0A0A0A, stop: 0.3 #101010, stop : 0.90 #AAAAAA, stop: 0.91 #000000);*/\n"
"margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"background:  #179CAD;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: grey;\n"
"width: 2px;\n"
"}")
        self.vol_slider.setMaximum(100)
        self.vol_slider.setSingleStep(1)
        self.vol_slider.setPageStep(10)
        self.vol_slider.setProperty("value", 100)
        self.vol_slider.setOrientation(QtCore.Qt.Vertical)
        self.vol_slider.setInvertedAppearance(False)
        self.vol_slider.setInvertedControls(False)
        self.vol_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.vol_slider.setTickInterval(0)
        self.vol_slider.setObjectName("vol_slider")
        self.verticalLayout.addWidget(self.vol_slider)
        self.mute_checkbox = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mute_checkbox.sizePolicy().hasHeightForWidth())
        self.mute_checkbox.setSizePolicy(sizePolicy)
        self.mute_checkbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mute_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mute_checkbox.setTristate(False)
        self.mute_checkbox.setObjectName("mute_checkbox")
        self.verticalLayout.addWidget(self.mute_checkbox)
        self.drop_checkbox = QtWidgets.QCheckBox(self.frame)
        self.drop_checkbox.setObjectName("drop_checkbox")
        self.verticalLayout.addWidget(self.drop_checkbox)
        self.to_master_checkbox = QtWidgets.QCheckBox(self.frame)
        self.to_master_checkbox.setChecked(False)
        self.to_master_checkbox.setObjectName("to_master_checkbox")
        self.verticalLayout.addWidget(self.to_master_checkbox)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Mixerstrip)
        self.send1_knob.valueChanged['int'].connect(self.send1_label.setNum)
        self.send2_knob.valueChanged['int'].connect(self.send2_label.setNum)
        self.vol_slider.valueChanged['int'].connect(self.vol_label.setNum)
        QtCore.QMetaObject.connectSlotsByName(Mixerstrip)

    def retranslateUi(self, Mixerstrip):
        _translate = QtCore.QCoreApplication.translate
        Mixerstrip.setWindowTitle(_translate("Mixerstrip", "Mixerstrip"))
        self.port_name_label.setText(_translate("Mixerstrip", "Name"))
        self.gain_knob.setToolTip(_translate("Mixerstrip", "Gain"))
        self.send1_knob.setToolTip(_translate("Mixerstrip", "Send1"))
        self.send2_knob.setToolTip(_translate("Mixerstrip", "Send2"))
        self.gain_label.setText(_translate("Mixerstrip", "0"))
        self.send1_label.setText(_translate("Mixerstrip", "0"))
        self.send2_label.setText(_translate("Mixerstrip", "0"))
        self.vol_label.setText(_translate("Mixerstrip", "100"))
        self.mute_checkbox.setToolTip(_translate("Mixerstrip", "Mute"))
        self.mute_checkbox.setText(_translate("Mixerstrip", "Mute"))
        self.drop_checkbox.setText(_translate("Mixerstrip", "Drop"))
        self.to_master_checkbox.setToolTip(_translate("Mixerstrip", "Send port to Master"))
        self.to_master_checkbox.setText(_translate("Mixerstrip", "Master"))
import gui_rc
