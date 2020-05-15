from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings
from superboucle.preferences_ui import Ui_Dialog
import settings
   
class Preferences(QDialog, Ui_Dialog):
    
    #COMPANY = "MeltinPop"
    #APPLICATION = "SpinTool"
    #DEVICES = "Devices"
    
    #COLOR_RED = "RED"
    #COLOR_AMBER = "AMBER"
    
    MESSAGE_RESTART_SB = "Please restart SpinTool to apply these changes."
    MESSAGE_RE_OPEN_PLAYLIST = "Please restart playlist window to apply these changes"
    MESSAGE_RE_OPEN_SCENES = "Please restart scenes manager window to apply these changes"

    def __init__(self, parent):
        super(Preferences, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        
        # settings = QSettings(self.COMPANY, self.APPLICATION)

        # reading preferred grid size
        self.spinRows.setValue(settings.grid_rows)
        self.spinColumns.setValue(settings.grid_columns)
        
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
        
        self.cBoxShowDetailsWhenTriggered.setChecked(settings.show_clip_details_on_trigger)
        self.cBoxShowDetailsWhenTriggered.stateChanged.connect(self.onCheckShowClipDetails)   
        
        self.cBoxShowDetailsWhenVolumeChanged.setChecked(settings.show_clip_details_on_volume)
        self.cBoxShowDetailsWhenVolumeChanged.stateChanged.connect(self.onCheckShowClipDetailsWhenVolume)
        
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

        self.labelMessage.setText("")
        
        self.setModal(True)
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

    def onCheckShowClipDetails(self):
        settings.show_clip_details_on_trigger = self.cBoxShowDetailsWhenTriggered.isChecked()
        
    def onCheckShowClipDetailsWhenVolume(self):
        settings.show_clip_details_on_volume = self.cBoxShowDetailsWhenVolumeChanged.isChecked()
        
    def onCheckPlayClipAfterRecord(self):
        settings.play_clip_after_record = self.cBoxPlayAfterRecord.isChecked()        

    def closeEvent(self, event):
        # settings = QSettings(self.COMPANY, self.APPLICATION)
        # settings.setValue('grid_columns', str(self.spinColumns.value()))   # Width
        # settings.setValue('grid_rows', str(self.spinRows.value()))         # Heigh

        # saving preferred grid size
        settings.grid_columns = self.spinColumns.value()  # Width
        settings.grid_rows = self.spinRows.value()        # Heigh

        # saving recording color
        if self.rButtonRedRecColor.isChecked():
            settings.rec_color = settings.COLOR_RED
        else:
            settings.rec_color = settings.COLOR_AMBER

        # save big font size
        settings.bigFontSize = self.cBigFontSize.value()

    def onFinished(self):
        pass
