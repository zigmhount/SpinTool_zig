from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings
from superboucle.preferences_ui import Ui_Dialog
   
class Preferences(QDialog, Ui_Dialog):
    
    COMPANY = "MeltinPop"
    APPLICATION = "SpinTool"
    DEVICES = "Devices"
    
    COLOR_RED = "RED"
    COLOR_AMBER = "AMBER"
    
    MESSAGE_RESTART_SB = "Please restart SpinTool to apply these changes."
    MESSAGE_RE_OPEN_PLAYLIST = "Please restart playlist window to apply these changes"
    MESSAGE_RE_OPEN_SCENES = "Please restart scenes manager window to apply these changes"

    def __init__(self, parent):
        super(Preferences, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        
        settings = QSettings(self.COMPANY, self.APPLICATION)
        # reading preferred grid size
        self.spinRows.setValue(int(settings.value('grid_rows', 8)))
        self.spinColumns.setValue(int(settings.value('grid_columns', 8)))
            
        # reading preferred recording color 
        if str(settings.value('rec_color', self.COLOR_AMBER)) == self.COLOR_RED:
#            self.rButtonAmberRecColor.checked = False
            self.rButtonRedRecColor.setChecked(True)     
        else:
#            self.rButtonRedRecColor.checked = False
            self.rButtonAmberRecColor.setChecked(True)
        
        self.cBoxShowScenesManager.setChecked(self.gui.show_scenes_on_start)
        self.cBoxShowScenesManager.stateChanged.connect(self.onCheckShowScenesOnStart)
        
        self.cBoxShowPlaylistManager.setChecked(self.gui.show_playlist_on_start)
        self.cBoxShowPlaylistManager.stateChanged.connect(self.onCheckShowPlaylistOnStart)    
        
        self.cBoxShowSongAnnotation.setChecked(self.gui.show_song_annotation_on_load)
        self.cBoxShowSongAnnotation.stateChanged.connect(self.onCheckShowSongAnnotation)        
        
        self.cBoxAutoconnectOutput.setChecked(self.gui.auto_connect_output)
        self.cBoxAutoconnectOutput.stateChanged.connect(self.onCheckAutoconnectOutput)

        self.cBoxAutoconnectInput.setChecked(self.gui.auto_connect_input)
        self.cBoxAutoconnectInput.stateChanged.connect(self.onCheckAutoconnectInput)        
        
        self.cBoxShowDetailsWhenTriggered.setChecked(self.gui.show_clip_details_on_trigger)
        self.cBoxShowDetailsWhenTriggered.stateChanged.connect(self.onCheckShowClipDetails)   
        
        self.cBoxShowDetailsWhenVolumeChanged.setChecked(self.gui.show_clip_details_on_volume)
        self.cBoxShowDetailsWhenVolumeChanged.stateChanged.connect(self.onCheckShowClipDetailsWhenVolume)
        
        self.cBoxPlayAfterRecord.setChecked(self.gui.play_clip_after_record)
        self.cBoxPlayAfterRecord.stateChanged.connect(self.onCheckPlayClipAfterRecord) 
        
        self.rButtonAmberRecColor.toggled.connect(self.onAmberRecColor)
        self.rButtonRedRecColor.toggled.connect(self.onRedRecColor)

        self.cBoxBigFontPlaylist.setChecked(self.gui.use_big_fonts_playlist)
        self.cBoxBigFontPlaylist.stateChanged.connect(self.onUseBigFontsPlaylist)  

        self.cBoxBigFontScenes.setChecked(self.gui.use_big_fonts_scenes)
        self.cBoxBigFontScenes.stateChanged.connect(self.onUseBigFontsScenes)

        self.cBoxAllowRecordEmptyClip.setChecked(self.gui.allow_record_empty_clip)
        self.cBoxAllowRecordEmptyClip.stateChanged.connect(self.onAllowRecordEmptyClip)

        self.labelMessage.setText("")
        
        self.setModal(True)
        self.show()

    def onAmberRecColor(self):
        self.labelMessage.setText(self.MESSAGE_RESTART_SB)
        
    def onRedRecColor(self):        
        self.labelMessage.setText(self.MESSAGE_RESTART_SB)
        
    def onCheckShowScenesOnStart(self):
        self.gui.show_scenes_on_start = self.cBoxShowScenesManager.isChecked()
    
    def onCheckShowPlaylistOnStart(self):
        self.gui.show_playlist_on_start = self.cBoxShowPlaylistManager.isChecked()
        
    def onCheckAutoconnectOutput(self):
        self.gui.auto_connect_output = self.cBoxAutoconnectOutput.isChecked()

    def onCheckAutoconnectInput(self):
        self.gui.auto_connect_input = self.cBoxAutoconnectInput.isChecked()

    def onCheckShowSongAnnotation(self):
        self.gui.show_song_annotation_on_load = self.cBoxShowSongAnnotation.isChecked()

    def onUseBigFontsPlaylist(self):
        self.labelMessage.setText(self.MESSAGE_RE_OPEN_PLAYLIST)
        self.gui.use_big_fonts_playlist = self.cBoxBigFontPlaylist.isChecked()   

    def onUseBigFontsScenes(self):
        self.labelMessage.setText(self.MESSAGE_RE_OPEN_SCENES)
        self.gui.use_big_fonts_scenes = self.cBoxBigFontScenes.isChecked()

    def onAllowRecordEmptyClip(self):
        self.gui.allow_record_empty_clip = self.cBoxAllowRecordEmptyClip.isChecked()

    def onCheckShowClipDetails(self):
        self.gui.show_clip_details_on_trigger = self.cBoxShowDetailsWhenTriggered.isChecked()
        
    def onCheckShowClipDetailsWhenVolume(self):
        self.gui.show_clip_details_on_volume = self.cBoxShowDetailsWhenVolumeChanged.isChecked()
        
    def onCheckPlayClipAfterRecord(self):
        self.gui.play_clip_after_record = self.cBoxPlayAfterRecord.isChecked()        

    def closeEvent(self, event):
        settings = QSettings(self.COMPANY, self.APPLICATION)
        # saving preferred grid size
        settings.setValue('grid_columns', str(self.spinColumns.value()))   # Width
        settings.setValue('grid_rows', str(self.spinRows.value()))         # Heigh
        # saving recording color
        if self.rButtonRedRecColor.isChecked():
            settings.setValue('rec_color', self.COLOR_RED)
        else:
            settings.setValue('rec_color', self.COLOR_AMBER)
        
        #settings.sync()

    def onFinished(self):
        pass
