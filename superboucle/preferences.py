from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QSettings
from superboucle.preferences_ui import Ui_Dialog
import settings
import common

class Preferences(QDialog, Ui_Dialog):

    MESSAGE_RESTART_SB = "Please restart SpinTool to apply these changes."
    MESSAGE_RE_OPEN_PLAYLIST = "Please restart playlist window to apply these changes"
    MESSAGE_RE_OPEN_SCENES = "Please restart scenes manager window to apply these changes"

    def __init__(self, parent):
        super(Preferences, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)

        # reading preferred grid size
        self.spinRows.setValue(settings.grid_rows)
        self.spinColumns.setValue(settings.grid_columns)

        # reading preferred new song master volume
        self.spinDefaultMasterVolume.setValue(settings.new_song_master_volume)

        # reading preferred new song BPM
        self.spinDefaultBPM.setValue(settings.new_song_bpm)

        # reading preferred new song beats
        self.spinDefaultBeats.setValue(settings.new_song_beats)

        # reading preferred recording color
        if settings.rec_color == settings.COLOR_RED:
            self.rButtonRedRecColor.setChecked(True)
        else:
            self.rButtonAmberRecColor.setChecked(True)

        # set big font size
        self.cBigFontSize.setValue(settings.bigFontSize)

        # Experimental: slower processing
        self.cBoxApplySlowerProcessing.setChecked(settings.slower_processing)
        self.cBoxApplySlowerProcessing.stateChanged.connect(self.onCheckSlowerProcessing)

        self.cBoxShowScenesManager.setChecked(settings.show_scenes_on_start)
        self.cBoxShowScenesManager.stateChanged.connect(self.onCheckShowScenesOnStart)

        self.cBoxShowPlaylistManager.setChecked(settings.show_playlist_on_start)
        self.cBoxShowPlaylistManager.stateChanged.connect(self.onCheckShowPlaylistOnStart)

        self.cBoxShowSongAnnotation.setChecked(settings.show_song_annotation_on_load)
        self.cBoxShowSongAnnotation.stateChanged.connect(self.onCheckShowSongAnnotation)

        self.cBoxAutoconnectOutput.setChecked(settings.auto_connect_output)
        self.cBoxAutoconnectOutput.stateChanged.connect(self.onCheckAutoconnectOutput)

        self.cBoxAutoconnectInput.setChecked(settings.auto_connect_input)
        self.cBoxAutoconnectInput.stateChanged.connect(self.onCheckAutoconnectInput)

        # save mixer settings
        
        self.cBoxSaveMixerstripGain.setChecked(settings.save_mixerstrip_gain)
        self.cBoxSaveMixerstripGain.stateChanged.connect(self.onSaveMixerstripGain)

        self.cBoxSaveMixerstripSend1.setChecked(settings.save_mixerstrip_send1)
        self.cBoxSaveMixerstripSend1.stateChanged.connect(self.onSaveMixerstripSend1)

        self.cBoxSaveMixerstripSend2.setChecked(settings.save_mixerstrip_send2)
        self.cBoxSaveMixerstripSend2.stateChanged.connect(self.onSaveMixerstripSend2)

        self.cBoxSaveMixerstripVolume.setChecked(settings.save_mixerstrip_volume)
        self.cBoxSaveMixerstripVolume.stateChanged.connect(self.onSaveMixerstripVolume)

        self.cBoxSaveMixerstripMute.setChecked(settings.save_mixerstrip_mute)
        self.cBoxSaveMixerstripMute.stateChanged.connect(self.onSaveMixerstripMute)


        # custom reset
        self.cBoxCustomResetMixerstripGain.setChecked(settings.customreset_mixerstrip_gain)
        self.cBoxCustomResetMixerstripGain.stateChanged.connect(self.onCustomResetMixerstripGain)

        self.cBoxCustomResetMixerstripSend1.setChecked(settings.customreset_mixerstrip_send1)
        self.cBoxCustomResetMixerstripSend1.stateChanged.connect(self.onCustomResetMixerstripSend1)

        self.cBoxCustomResetMixerstripSend2.setChecked(settings.customreset_mixerstrip_send2)
        self.cBoxCustomResetMixerstripSend2.stateChanged.connect(self.onCustomResetMixerstripSend2)

        self.cBoxCustomResetMixerstripVolume.setChecked(settings.customreset_mixerstrip_volume)
        self.cBoxCustomResetMixerstripVolume.stateChanged.connect(self.onCustomResetMixerstripVolume)

        self.cBoxCustomResetMixerstripMute.setChecked(settings.customreset_mixerstrip_mute)
        self.cBoxCustomResetMixerstripMute.stateChanged.connect(self.onCustomResetMixerstripMute)

        

        self.cBoxUnshiftAfterProcessing.setChecked(settings.disable_shift_after_processing)
        self.cBoxUnshiftAfterProcessing.stateChanged.connect(self.onDisableShiftAfterProcessing)        

        self.cBoxShowDetailsWhenTriggered.setChecked(settings.show_clip_details_on_trigger)
        self.cBoxShowDetailsWhenTriggered.stateChanged.connect(self.onCheckShowClipDetails)

        self.cBoxPlayAfterRecord.setChecked(settings.play_clip_after_record)
        self.cBoxPlayAfterRecord.stateChanged.connect(self.onCheckPlayClipAfterRecord)

        self.rButtonAmberRecColor.toggled.connect(self.onAmberRecColor)
        self.rButtonRedRecColor.toggled.connect(self.onRedRecColor)

        self.cBoxBigFontPlaylist.setChecked(settings.use_big_fonts_playlist)
        self.cBoxBigFontPlaylist.stateChanged.connect(self.onUseBigFontsPlaylist)

        self.cBoxBigFontScenes.setChecked(settings.use_big_fonts_scenes)
        self.cBoxBigFontScenes.stateChanged.connect(self.onUseBigFontsScenes)

        self.cBoxAllowRecordEmptyClip.setChecked(settings.allow_record_empty_clip)
        self.cBoxAllowRecordEmptyClip.stateChanged.connect(self.onAllowRecordEmptyClip)

        self.cBoxAutoAssignNewClipsColumn.setChecked(settings.auto_assign_new_clip_column)
        self.cBoxAutoAssignNewClipsColumn.stateChanged.connect(self.onAutoAssignNewClipsColumn)

        self.cBoxPreventSongSave.setChecked(settings.prevent_song_save)
        self.cBoxPreventSongSave.stateChanged.connect(self.onPreventSongSave)        

        self.labelMessage.setText("")

        self.btn_prefs_ok.clicked.connect(self.close)

        self.setModal(True)
        self.tabPreferences.setCurrentIndex(0)
        self.show()


    def onAmberRecColor(self):
        self.labelMessage.setText(self.MESSAGE_RESTART_SB)

    def onRedRecColor(self):
        self.labelMessage.setText(self.MESSAGE_RESTART_SB)

    def onCheckShowScenesOnStart(self):
        settings.show_scenes_on_start = self.cBoxShowScenesManager.isChecked()

    def onCheckSlowerProcessing(self):
        settings.slower_processing = self.cBoxApplySlowerProcessing.isChecked()

    def onCheckShowPlaylistOnStart(self):
        settings.show_playlist_on_start = self.cBoxShowPlaylistManager.isChecked()

    def onCheckAutoconnectOutput(self):
        settings.auto_connect_output = self.cBoxAutoconnectOutput.isChecked()

    def onCheckAutoconnectInput(self):
        settings.auto_connect_input = self.cBoxAutoconnectInput.isChecked()


    # save mixer settings
    def onSaveMixerstripGain(self):
        settings.save_mixerstrip_gain = self.cBoxSaveMixerstripGain.isChecked()

    def onSaveMixerstripSend1(self):
        settings.save_mixerstrip_send1 = self.cBoxSaveMixerstripSend1.isChecked()

    def onSaveMixerstripSend2(self):
        settings.save_mixerstrip_send2 = self.cBoxSaveMixerstripSend2.isChecked()

    def onSaveMixerstripVolume(self):
        settings.save_mixerstrip_volume = self.cBoxSaveMixerstripVolume.isChecked()

    def onSaveMixerstripMute(self):
        settings.save_mixerstrip_mute = self.cBoxSaveMixerstripMute.isChecked()


    # reset all
    def onCustomResetMixerstripGain(self):
        settings.customreset_mixerstrip_gain = self.cBoxCustomResetMixerstripGain.isChecked()

    def onCustomResetMixerstripSend1(self):
        settings.customreset_mixerstrip_send1 = self.cBoxCustomResetMixerstripSend1.isChecked()

    def onCustomResetMixerstripSend2(self):
        settings.customreset_mixerstrip_send2 = self.cBoxCustomResetMixerstripSend2.isChecked()

    def onCustomResetMixerstripVolume(self):
        settings.customreset_mixerstrip_volume = self.cBoxCustomResetMixerstripVolume.isChecked()

    def onCustomResetMixerstripMute(self):
        settings.customreset_mixerstrip_mute = self.cBoxCustomResetMixerstripMute.isChecked()


    

    def onCheckShowSongAnnotation(self):
        settings.show_song_annotation_on_load = self.cBoxShowSongAnnotation.isChecked()

    def onUseBigFontsPlaylist(self):
        self.labelMessage.setText(self.MESSAGE_RE_OPEN_PLAYLIST)
        settings.use_big_fonts_playlist = self.cBoxBigFontPlaylist.isChecked()

    def onUseBigFontsScenes(self):
        self.labelMessage.setText(self.MESSAGE_RE_OPEN_SCENES)
        settings.use_big_fonts_scenes = self.cBoxBigFontScenes.isChecked()

    def onAllowRecordEmptyClip(self):
        settings.allow_record_empty_clip = self.cBoxAllowRecordEmptyClip.isChecked()

    def onAutoAssignNewClipsColumn(self):
        settings.auto_assign_new_clip_column = self.cBoxAutoAssignNewClipsColumn.isChecked()

    def onPreventSongSave(self):
        settings.prevent_song_save = self.cBoxPreventSongSave.isChecked()

    def onCheckShowClipDetails(self):
        settings.show_clip_details_on_trigger = self.cBoxShowDetailsWhenTriggered.isChecked()

    def onDisableShiftAfterProcessing(self):
        settings.disable_shift_after_processing = self.cBoxUnshiftAfterProcessing.isChecked()

    def onCheckPlayClipAfterRecord(self):
        settings.play_clip_after_record = self.cBoxPlayAfterRecord.isChecked()

    def closeEvent(self, event):

        # saving preferred grid size
        settings.grid_columns = self.spinColumns.value()  # Width
        settings.grid_rows = self.spinRows.value()        # Heigh

        # saving preferred new song master volume
        settings.new_song_master_volume = self.spinDefaultMasterVolume.value()

        # saving preferred new song BPM
        settings.new_song_bpm = self.spinDefaultBPM.value()

        # saving preferred new song beats
        settings.new_song_beats = self.spinDefaultBeats.value()

        # saving recording color
        if self.rButtonRedRecColor.isChecked():
            settings.rec_color = settings.COLOR_RED
        else:
            settings.rec_color = settings.COLOR_AMBER

        # save big font size
        settings.bigFontSize = self.cBigFontSize.value()

    def onFinished(self):
        pass

