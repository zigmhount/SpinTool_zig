from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from superboucle.edit_clips_ui import Ui_Dialog
from PyQt5 import QtGui
import common

EDIT_ALL_SELECTED_CLIPS_MESSAGE = "Check the details you want to massively change, then fill the values and press Ok"
EDIT_BY_OUTPUT_PORT_MESSAGE = "Select an output port, then check the details and fill the values you want to massively change for all the clips belonging to that port"
EDIT_BY_MUTE_GROUP_MESSAGE = "Select a mute group, then check the details and fill the values you want to massively change for all the clips belonging to that mute group"

EDIT_ALL_SELECTED_LABEL_STYLE = ('font: bold 11pt "Noto Sans";background-color: rgb(255, 255, 0);')
EDIT_OTHER_LABEL_STYLE = ('font: bold 10pt "Noto Sans";')

class EditClipsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, edit_mode = 0, selected_clips = None):
        super(EditClipsDialog, self).__init__(parent)

        self.gui = parent
        self.setupUi(self)
        self.initializeUI()
        
        self.proceed = False
        self.volume = 0
        self.volume_change_mode = common.SET_VOLUME
        self.accepted.connect(self.onOk)        

        self.checkBoxEnableOutPortsChanges.clicked.connect(self.onEnablePortsChangeClicked)
        self.checkBoxEnableMutGroupChanges.clicked.connect(self.onEnableMuteGroupsChangeClicked)
        self.checkBoxEnableVolumeChanges.clicked.connect(self.onEnableVolumeChangeClicked)

        self.buttonCopyPortFromCurrentClip.clicked.connect(self.onButtonCopyPortClicked)
        self.buttonCopyMuteGroupFromCurrentClip.clicked.connect(self.onButtonCopyMuteGroupClicked)
        self.buttonCopyVolumeFromCurrentClip.clicked.connect(self.onButtonCopyVolumeClicked)

        self.radioButtonSetVolume.toggled.connect(self.updateVolumeRadioButtons)
        self.radioButtonIncreaseVolume.toggled.connect(self.updateVolumeRadioButtons)
        self.radioButtonDecreaseVolume.toggled.connect(self.updateVolumeRadioButtons)

        self.comboBoxOutputPorts.addItems(sorted(self.gui.song.outputsPorts))

        self.edit_mode = edit_mode
        if self.edit_mode == common.CLIPS_EDIT_MODE_ALL_SELECTED:

            self.checkBoxEnableOutPortsChanges.setVisible(True)
            self.checkBoxEnableMutGroupChanges.setVisible(True)
            self.checkBoxEnableVolumeChanges.setVisible(True)

            # I left to GUI the control that selected_clips contains some clips
            # so I won't check again here.
            text = "You have selected " + str(selected_clips.__len__()) + " clips.  "
            self.labelMessage.setText(text + EDIT_ALL_SELECTED_CLIPS_MESSAGE)
            self.labelMessage.setStyleSheet(EDIT_ALL_SELECTED_LABEL_STYLE)

        elif edit_mode == common.CLIPS_EDIT_MODE_BY_MUTE_GROUP:

            self.checkBoxEnableOutPortsChanges.setVisible(True)
            self.checkBoxEnableMutGroupChanges.setVisible(False)
            self.checkBoxEnableVolumeChanges.setVisible(True)

            self.labelMessage.setText(EDIT_BY_MUTE_GROUP_MESSAGE)
            self.labelMessage.setStyleSheet(EDIT_OTHER_LABEL_STYLE)

            self.groupBoxMuteGroup.setEnabled(True)
            self.checkBoxUnselectClips.setVisible(False)

            self.framePorts.setGeometry(230, 70, 291, 111)
            self.frameMuteGroups.setGeometry(10, 70, 211, 111)
        
        elif edit_mode == common.CLIPS_EDIT_MODE_BY_OUTPUT_PORT:

            self.checkBoxEnableOutPortsChanges.setVisible(False)
            self.checkBoxEnableMutGroupChanges.setVisible(True)
            self.checkBoxEnableVolumeChanges.setVisible(True)

            self.labelMessage.setText(EDIT_BY_OUTPUT_PORT_MESSAGE)
            self.labelMessage.setStyleSheet(EDIT_OTHER_LABEL_STYLE)

            self.groupBoxPorts.setEnabled(True)
            self.checkBoxUnselectClips.setVisible(False)

        self.setFixedSize(self.size())
        self.setModal(True)
        self.show()

    def initializeUI(self):
        self.groupBoxPorts.setEnabled(False)
        self.groupBoxMuteGroup.setEnabled(False)
        self.groupBoxVolume.setEnabled(False)
        self.checkBoxEnableMutGroupChanges.setChecked(False)
        self.checkBoxEnableOutPortsChanges.setChecked(False)
        self.checkBoxEnableVolumeChanges.setChecked(False)
        self.radioButtonSetVolume.setChecked(True)

    def showNoClipMessage(self):
        message = QMessageBox(self)
        message.setWindowTitle("Can't read clip details")
        message.setText("No clip is currently selected in Edit details in SpinTool window")
        message.show()

    def onEnablePortsChangeClicked(self):
        self.groupBoxPorts.setEnabled(self.checkBoxEnableOutPortsChanges.isChecked())
    
    def onEnableMuteGroupsChangeClicked(self):
        self.groupBoxMuteGroup.setEnabled(self.checkBoxEnableMutGroupChanges.isChecked())

    def onEnableVolumeChangeClicked(self):
        self.groupBoxVolume.setEnabled(self.checkBoxEnableVolumeChanges.isChecked())

    def onButtonCopyPortClicked(self):
        if self.gui.last_clip:
            self.comboBoxOutputPorts.setCurrentText(self.gui.last_clip.output)
        else:
            self.showNoClipMessage()

    def onButtonCopyMuteGroupClicked(self):
        if self.gui.last_clip:
            self.spinBoxMuteGroups.setValue(self.gui.last_clip.mute_group)
        else:
            self.showNoClipMessage()            

    def onButtonCopyVolumeClicked(self):
        if self.gui.last_clip:
            self.volume = self.gui.last_clip.volume
            self.spinBoxVolumeAmount.setValue(common.toDigitalVolumeValue(self.gui.last_clip.volume))
        else:
            self.showNoClipMessage()    

    def updateVolumeRadioButtons(self):
        self.buttonCopyVolumeFromCurrentClip.setVisible(self.radioButtonSetVolume.isChecked())

        if self.radioButtonSetVolume.isChecked() == True:
            self.volume_change_mode = common.SET_VOLUME

        elif self.radioButtonIncreaseVolume.isChecked() == True:
            self.volume_change_mode = common.INCREASE_VOLUME

        elif self.radioButtonDecreaseVolume.isChecked() == True:
            self.volume_change_mode = common.DECREASE_VOLUME

    def getVolumeAmount(self):
        return self.volume, self.volume_change_mode

    def getOutputPort(self):
        return self.comboBoxOutputPorts.currentText()
    
    def getMuteGroup(self):
        return self.spinBoxMuteGroups.value()

    def getEditVolume(self):
        return self.checkBoxEnableVolumeChanges.isChecked()

    def getEditMuteGroup(self):
        return self.checkBoxEnableMutGroupChanges.isChecked()

    def getEditOutputPort(self):
        return self.checkBoxEnableOutPortsChanges.isChecked()

    def getUnselectClips(self):
        return self.checkBoxUnselectClips.isChecked()

    def onOk(self):
        self.volume = self.spinBoxVolumeAmount.value()
        self.proceed = True

    def onFinished(self):
        pass