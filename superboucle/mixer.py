from PyQt5.QtCore import Qt
from superboucle.assistant import Assistant
from PyQt5.QtGui import QCursor
import help
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QWidget, QSpacerItem, QSizePolicy, QApplication
from superboucle.mixer_ui import Ui_Dialog
from superboucle.mixerstrip import Mixerstrip
from PyQt5 import QtGui
import json
import sys
import copy
import common
import settings

class Mixer(QDialog, Ui_Dialog):

    def __init__(self, parent):
        super(Mixer, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)

        # signals
        self.song_vol_slider.valueChanged.connect(self.setSongVolume)

        self.masterport_vol_slider.valueChanged.connect(self.setMasterPortFinalVolume)
        self.masterport_mute_checkbox.clicked.connect(self.setMasterPortMute)
        
        self.custom_reset_btn.clicked.connect(self.onCustomReset)
        self.reset_gain_btn.clicked.connect(self.onResetGain)
        self.reset_send1_btn.clicked.connect(self.onResetSend1)
        self.reset_send2_btn.clicked.connect(self.onResetSend2)
        self.reset_vol_btn.clicked.connect(self.onResetVolume)
        self.reset_mute_btn.clicked.connect(self.onResetMute)
        self.unlink_stripes_btn.clicked.connect(self.onUnlinkStripes)

        self.advanced_checkbox.clicked.connect(self.onAdvancedMode)

        self.updateMasterMuteGui(settings.master_port_mute)
        self.updateSongVolumeGui(self.gui.song.volume * 256)
        self.updateMasterVolumeGui(settings.master_port_final_volume * 100)
        

        # overwrite finished signal?
        self.finished.connect(self.onFinished)


    def showEvent(self, event):
        if settings.mixer_geometry:
            self.restoreGeometry(settings.mixer_geometry)

        self.updateGui(settings.output_ports)
        self.UpdateStripesLinkGui()

    def moveEvent(self, event):
        self.geometry = self.saveGeometry()
        settings.mixer_geometry = copy.deepcopy(self.geometry)

    # setup the port mixer gui (create one mixerstrip for each port)
    def updateGui(self, output_ports):

        #reset / clear mixerstrip layout
        while self.mixerLayout.count():
            child = self.mixerLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        index = 0

        self.portlist = common.toPortsList(output_ports)
        # create mixerstrips
        for i in self.portlist:
            # add one strip
            strip = Mixerstrip(self, i, index)
            self.mixerLayout.addWidget(strip)
            index = index + 1

        # add spacer
        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mixerLayout.addItem(spacer)

        # set dialog size according to mixerstrip amount
        mixerxsize = len(self.portlist)*(95)
        self.resize(220 + mixerxsize, 500)

        # update song volume fader
        self.updateSongVolumeGui(common.toControllerVolumeValue(self.gui.song.volume)) # = * 256


    def updateStripVolume(self, stripName):
        strip = self.findChild(Mixerstrip, stripName)
        if strip:
            strip.updateGuiVolume()

    def updateStripSend1(self, stripName):
        strip = self.findChild(Mixerstrip, stripName)
        if strip:
            strip.updateGuiSend1()

    def updateStripSend2(self, stripName):
        strip = self.findChild(Mixerstrip, stripName)
        if strip:
            strip.updateGuiSend2()

    def updateStripMute(self, stripName):

        strip = self.findChild(Mixerstrip, stripName)
        if strip:
            strip.updateGuiMute()
    
    # used by mixerstrip to notify mute value updated
    def muteUpdated(self, port, index):
        self.gui.updateMidiMute(port, index)

    def UpdateStripesLinkGui(self):
        if self.gui.mixer_stripes_midi_linked == True:
            self.unlink_stripes_btn.setIcon(QtGui.QIcon(":/icons/icons/sliders.png"))
        else:
            self.unlink_stripes_btn.setIcon(QtGui.QIcon(":/icons/icons/warning.png"))
        
        self.unlink_stripes_btn.update()


    # update SONG VOLUME GUI
    def updateSongVolumeGui(self, value):
        self.song_vol_slider.setValue(value)
        self.song_vol_label.setText(str(int(common.toAnalogVolumeValue(value)*100*2))) # =  / 256


    # set SONG VOLUME
    def setSongVolume(self):
        self.gui.song.volume = common.toAnalogVolumeValue(self.song_vol_slider.value()) # =  / 256
        self.gui.song_volume_knob.setValue(common.toControllerVolumeValue(self.gui.song.volume)) # = * 256)



    # MASTER PORT FINAL VOLUME
    def updateMasterVolumeGui(self, value):
        self.masterport_vol_slider.setValue(value)

    # MASTER PORT MUTE
    def updateMasterMuteGui(self, value):
        self.masterport_mute_checkbox.setChecked(not(value))



    # set MASTER PORT FINAL VOLUME
    def setMasterPortFinalVolume(self):
        settings.master_port_final_volume = (self.masterport_vol_slider.value() / 100) 
        # (self.masterport_vol_slider.value() / 100) * (1-bool(self.master_mute_checkbox.checkState()))
    
    # set MASTER PORT MUTE
    def setMasterPortMute(self):
        settings.master_port_mute = not(self.masterport_mute_checkbox.checkState())
        # (1-bool(self.master_mute_checkbox.checkState()))
        # self.master_mute_checkbox.isChecked()


    # RESETS
    def onCustomReset(self):
        if settings.customreset_mixerstrip_gain == False:
            self.onResetGain()
        if settings.customreset_mixerstrip_send1 == False:
            self.onResetSend1()
        if settings.customreset_mixerstrip_send2 == False:
            self.onResetSend2()
        if settings.customreset_mixerstrip_volume == False:
            self.onResetVolume()
        if settings.customreset_mixerstrip_mute == False:
            self.onResetMute()

    def onResetGain(self):
        common.resetGain(settings.output_ports)
        self.updateGui(settings.output_ports)

    def onResetSend1(self):
        common.resetSend1(settings.output_ports)
        self.updateGui(settings.output_ports)

    def onResetSend2(self):
        common.resetSend2(settings.output_ports)
        self.updateGui(settings.output_ports)

    def onResetVolume(self):
        common.resetVolume(settings.output_ports)
        self.updateGui(settings.output_ports)

    def onResetMute(self):
        common.resetMute(settings.output_ports)
        self.updateGui(settings.output_ports)
        self.gui.resetMidiMute()

    
    def onUnlinkStripes(self):
        self.gui.mixer_stripes_midi_linked = not self.gui.mixer_stripes_midi_linked
        self.UpdateStripesLinkGui()


    def onAdvancedMode(self):
        common.mixer_mode = self.advanced_checkbox.isChecked()
        self.updateGui(settings.output_ports)



    # overwrite hideEvend method - can be also used with onFinished
    def hideEvent(self, event):
        self.gui.actionMixer.setEnabled(True)

    # triggered if dialog is closed
    def onFinished(self):
        pass


    # HELP management ---------------------------------------------------------

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_H:  # if pressed key is H (help)

            pos = QCursor.pos()
            widget = QApplication.widgetAt(pos)   # this is widget under cursor

            if widget is None: return
            accName = widget.accessibleName()     # this is widget accessible name
            
            if accName != "":
                wantedHelp = help.Context(accName)  # Conversion of string accessible name to Context enum
                self.showContextHelp(wantedHelp)
                

    def showContextHelp(self, wantedHelp):
        helpText = help.getContextHelp(wantedHelp)
        Assistant(self, helpText, Assistant.MODE_CONTEXT)