# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manu/Sviluppo/SpinTool/superboucle/mixer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(872, 470)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(72, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(72, 16777215))
        self.frame_2.setBaseSize(QtCore.QSize(72, 0))
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.port_name_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.port_name_label.setFont(font)
        self.port_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.port_name_label.setObjectName("port_name_label")
        self.verticalLayout_2.addWidget(self.port_name_label)
        self.song_vol_label = QtWidgets.QLabel(self.frame_2)
        self.song_vol_label.setAlignment(QtCore.Qt.AlignCenter)
        self.song_vol_label.setObjectName("song_vol_label")
        self.verticalLayout_2.addWidget(self.song_vol_label)
        self.song_vol_slider = QtWidgets.QSlider(self.frame_2)
        self.song_vol_slider.setMinimumSize(QtCore.QSize(50, 0))
        self.song_vol_slider.setToolTip("")
        self.song_vol_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.song_vol_slider.setAutoFillBackground(True)
        self.song_vol_slider.setStyleSheet("QSlider::groove:vertical {\n"
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
"background:  #A00659;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: grey;\n"
"width: 2px;\n"
"}")
        self.song_vol_slider.setMaximum(256)
        self.song_vol_slider.setSingleStep(1)
        self.song_vol_slider.setPageStep(10)
        self.song_vol_slider.setProperty("value", 100)
        self.song_vol_slider.setOrientation(QtCore.Qt.Vertical)
        self.song_vol_slider.setInvertedAppearance(False)
        self.song_vol_slider.setInvertedControls(False)
        self.song_vol_slider.setObjectName("song_vol_slider")
        self.verticalLayout_2.addWidget(self.song_vol_slider)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(72, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(72, 16777215))
        self.frame_4.setBaseSize(QtCore.QSize(72, 0))
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(9, -1, 2, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.port_name_label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.port_name_label_3.setFont(font)
        self.port_name_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.port_name_label_3.setObjectName("port_name_label_3")
        self.verticalLayout_4.addWidget(self.port_name_label_3)
        self.vol_label_3 = QtWidgets.QLabel(self.frame_4)
        self.vol_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.vol_label_3.setObjectName("vol_label_3")
        self.verticalLayout_4.addWidget(self.vol_label_3)
        self.masterport_vol_slider = QtWidgets.QSlider(self.frame_4)
        self.masterport_vol_slider.setMinimumSize(QtCore.QSize(50, 0))
        self.masterport_vol_slider.setToolTip("")
        self.masterport_vol_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.masterport_vol_slider.setAutoFillBackground(True)
        self.masterport_vol_slider.setStyleSheet("QSlider::groove:vertical {\n"
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
"background:  #A00659;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: grey;\n"
"width: 2px;\n"
"}")
        self.masterport_vol_slider.setMaximum(100)
        self.masterport_vol_slider.setSingleStep(1)
        self.masterport_vol_slider.setPageStep(10)
        self.masterport_vol_slider.setProperty("value", 100)
        self.masterport_vol_slider.setOrientation(QtCore.Qt.Vertical)
        self.masterport_vol_slider.setInvertedAppearance(False)
        self.masterport_vol_slider.setInvertedControls(False)
        self.masterport_vol_slider.setObjectName("masterport_vol_slider")
        self.verticalLayout_4.addWidget(self.masterport_vol_slider)
        self.masterport_mute_checkbox = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.masterport_mute_checkbox.sizePolicy().hasHeightForWidth())
        self.masterport_mute_checkbox.setSizePolicy(sizePolicy)
        self.masterport_mute_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.masterport_mute_checkbox.setTristate(False)
        self.masterport_mute_checkbox.setObjectName("masterport_mute_checkbox")
        self.verticalLayout_4.addWidget(self.masterport_mute_checkbox)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(72, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(72, 16777215))
        self.frame_5.setBaseSize(QtCore.QSize(72, 0))
        self.frame_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.port_name_label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.port_name_label_4.setFont(font)
        self.port_name_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.port_name_label_4.setObjectName("port_name_label_4")
        self.verticalLayout_5.addWidget(self.port_name_label_4)
        self.custom_reset_btn = QtWidgets.QPushButton(self.frame_5)
        self.custom_reset_btn.setObjectName("custom_reset_btn")
        self.verticalLayout_5.addWidget(self.custom_reset_btn)
        self.reset_gain_btn = QtWidgets.QPushButton(self.frame_5)
        self.reset_gain_btn.setObjectName("reset_gain_btn")
        self.verticalLayout_5.addWidget(self.reset_gain_btn)
        self.reset_send1_btn = QtWidgets.QPushButton(self.frame_5)
        self.reset_send1_btn.setObjectName("reset_send1_btn")
        self.verticalLayout_5.addWidget(self.reset_send1_btn)
        self.reset_send2_btn = QtWidgets.QPushButton(self.frame_5)
        self.reset_send2_btn.setObjectName("reset_send2_btn")
        self.verticalLayout_5.addWidget(self.reset_send2_btn)
        self.reset_vol_btn = QtWidgets.QPushButton(self.frame_5)
        self.reset_vol_btn.setObjectName("reset_vol_btn")
        self.verticalLayout_5.addWidget(self.reset_vol_btn)
        self.reset_mute_btn = QtWidgets.QPushButton(self.frame_5)
        self.reset_mute_btn.setObjectName("reset_mute_btn")
        self.verticalLayout_5.addWidget(self.reset_mute_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.unlink_stripes_btn = QtWidgets.QPushButton(self.frame_5)
        self.unlink_stripes_btn.setStyleSheet("")
        self.unlink_stripes_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/sliders.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unlink_stripes_btn.setIcon(icon)
        self.unlink_stripes_btn.setIconSize(QtCore.QSize(27, 27))
        self.unlink_stripes_btn.setObjectName("unlink_stripes_btn")
        self.verticalLayout_5.addWidget(self.unlink_stripes_btn)
        self.advanced_checkbox = QtWidgets.QCheckBox(self.frame_5)
        self.advanced_checkbox.setObjectName("advanced_checkbox")
        self.verticalLayout_5.addWidget(self.advanced_checkbox)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 616, 424))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mixerLayout = QtWidgets.QHBoxLayout()
        self.mixerLayout.setObjectName("mixerLayout")
        self.horizontalLayout_2.addLayout(self.mixerLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.masterport_vol_slider.valueChanged['int'].connect(self.vol_label_3.setNum)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mixer"))
        self.frame_2.setAccessibleName(_translate("Dialog", "Help_Mixer_SongVolume"))
        self.port_name_label.setAccessibleName(_translate("Dialog", "Help_Mixer_SongVolume"))
        self.port_name_label.setText(_translate("Dialog", "Song"))
        self.song_vol_label.setText(_translate("Dialog", "100"))
        self.song_vol_slider.setAccessibleName(_translate("Dialog", "Help_Mixer_SongVolume"))
        self.frame_4.setAccessibleName(_translate("Dialog", "Help_Mixer_MasterVolume"))
        self.port_name_label_3.setAccessibleName(_translate("Dialog", "Help_Mixer_MasterVolume"))
        self.port_name_label_3.setText(_translate("Dialog", "Master"))
        self.vol_label_3.setText(_translate("Dialog", "100"))
        self.masterport_vol_slider.setAccessibleName(_translate("Dialog", "Help_Mixer_MasterVolume"))
        self.masterport_mute_checkbox.setToolTip(_translate("Dialog", "Mute Master"))
        self.masterport_mute_checkbox.setText(_translate("Dialog", "Mute"))
        self.port_name_label_4.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.port_name_label_4.setText(_translate("Dialog", "Reset"))
        self.custom_reset_btn.setToolTip(_translate("Dialog", "Custom reset"))
        self.custom_reset_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.custom_reset_btn.setText(_translate("Dialog", "Custom"))
        self.reset_gain_btn.setToolTip(_translate("Dialog", "Reset all Gains"))
        self.reset_gain_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.reset_gain_btn.setText(_translate("Dialog", "Gain"))
        self.reset_send1_btn.setToolTip(_translate("Dialog", "Resent all Send1s"))
        self.reset_send1_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.reset_send1_btn.setText(_translate("Dialog", "Send1"))
        self.reset_send2_btn.setToolTip(_translate("Dialog", "Reset all Send2s"))
        self.reset_send2_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.reset_send2_btn.setText(_translate("Dialog", "Send2"))
        self.reset_vol_btn.setToolTip(_translate("Dialog", "Reset all Volumes"))
        self.reset_vol_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.reset_vol_btn.setText(_translate("Dialog", "Vol"))
        self.reset_mute_btn.setToolTip(_translate("Dialog", "Reset all Mutes"))
        self.reset_mute_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Reset"))
        self.reset_mute_btn.setText(_translate("Dialog", "Mute"))
        self.unlink_stripes_btn.setToolTip(_translate("Dialog", "Interrupt the connection between MIDI device and SpinTool mixer stripes (output ports)"))
        self.unlink_stripes_btn.setAccessibleName(_translate("Dialog", "Help_Mixer_Unlink"))
        self.advanced_checkbox.setToolTip(_translate("Dialog", "Show Advanced Mixer"))
        self.advanced_checkbox.setText(_translate("Dialog", "ADV"))
        self.label.setAccessibleName(_translate("Dialog", "Help_Mixer_OutputPorts"))
        self.label.setText(_translate("Dialog", "Output Ports"))
        self.scrollArea.setAccessibleName(_translate("Dialog", "Help_Mixer_OutputPorts"))
import gui_rc
